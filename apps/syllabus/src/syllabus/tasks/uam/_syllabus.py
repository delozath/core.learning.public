from omegaconf import DictConfig


import pandas as pd

from jinja2 import Environment, FileSystemLoader


from syllabus.ports.tasks import SyllabusPort
from syllabus.data.loader import LoaderResolver
from syllabus.tasks.uam.trimestre import Calendario


class SyllabusUAMTask(SyllabusPort):
    def __init__(self, cfg: DictConfig) -> None:
        super().__init__(cfg)
    
    def build(self):
        mock = f"Syllabus de la UAM para el curso {self.cfg.curso.information.name} ({self.cfg.curso.information.clave})"
        DB_NAME = self.cfg.curso.data.full.db
        DB_TEMARIO = self.cfg.curso.queries.temario

        TRIM_INIT = self.cfg.curso.calendario.inicio
        TRIM_END = self.cfg.curso.calendario.fin
        TRIM_OFFSET = self.cfg.curso.calendario.uam_offset
        TRIM_SESSIONS = self.cfg.curso.calendario

        TRANSLATE = self.cfg.constantes.traduccion

        database = self._connect_db(DB_NAME)
        temario = database.query(DB_TEMARIO)
        topicos = self.get_topicos(temario)

        calendar = Calendario()
        calendar.trimestre(
            TRIM_INIT,
            TRIM_END,
            TRANSLATE,
            TRIM_OFFSET
        )
        sesiones = calendar.sesiones(calendar.trim, TRIM_SESSIONS)
        cal_clean = calendar.remover_eventos(sesiones, TRIM_SESSIONS)
        env = Environment(
            loader=FileSystemLoader(
                f"{self.cfg.constantes.path.root}/syllabus/tasks/uam/templates/"
            )
        )

        template = env.get_template("uami_temario.tex.j2")
        temario_render = template.render(
            temario=topicos
        )
        breakpoint()
        print(mock)
        breakpoint()
    
    def _connect_db(self, db: str):
        database = (
            LoaderResolver().resolve(
                db,
                'sqlite'
             )
         )
        return database
    
    def get_topicos(self, temario: pd.DataFrame) -> dict:
        topicos = {}
        for (num_unidad, num_tema), grupo in temario.groupby(['num_unidad', 'num_tema']):
            unidad_titulo = grupo['unidad_titulo'].iloc[0]
            tema_titulo = grupo['tema_titulo'].iloc[0]
            
            subtemas = grupo[['descripcion', 'cobertura']].to_dict('records')
            
            if unidad_titulo not in topicos:
                topicos[unidad_titulo] = {}
            
            topicos[unidad_titulo][tema_titulo] = subtemas
        
        return topicos
    