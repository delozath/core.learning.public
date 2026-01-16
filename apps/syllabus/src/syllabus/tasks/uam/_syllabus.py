from omegaconf import DictConfig

from syllabus.ports.tasks import SyllabusPort

from syllabus.data.loader import LoaderResolver

class SyllabusUAMTask(SyllabusPort):
    def __init__(self, cfg: DictConfig) -> None:
        super().__init__(cfg)
    
    def build(self):
        mock = f"Syllabus de la UAM para el curso {self.cfg.curso.information.name} ({self.cfg.curso.information.clave})"
        DB_NAME = self.cfg.curso.data.full.db
        DB_TEMARIO = self.cfg.curso.queries.temario

        database = self._connect_db(DB_NAME)
        temario = database.query(DB_TEMARIO)
        breakpoint()
        print(mock)
    
    def _connect_db(self, db: str):
        database = (
            LoaderResolver().resolve(
                db,
                'sqlite'
             )
         )
        return database
        