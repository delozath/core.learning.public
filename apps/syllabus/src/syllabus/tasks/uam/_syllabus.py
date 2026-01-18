import os
from pathlib import Path
from typing import Self
from dotenv import load_dotenv
load_dotenv()


import pandas as pd
from omegaconf import DictConfig
from pylatex import Document, Package, Section, Subsection, Tabular, Command
from pylatex.utils import NoEscape


from syllabus.ports.dbs import DatabasePort
from syllabus.ports.tasks import SyllabusOrchestratorPort, SyllabusPublisherPort

from syllabus.data.loader import LoaderResolver
from syllabus.tasks.uam.trimestre import Calendario
from syllabus.tasks.uam.jinja_driver import JinjaUAMSyllabus


class SyllabusUAMTask(SyllabusOrchestratorPort):
    def __init__(self, cfg: DictConfig) -> None:
        super().__init__(cfg)
    
    def build(self):
        """
        Se consulta la base de datos para obtener el temario y se genera el syllabus en formato LaTeX
        para la clase configurada en el archivo YAML correspondiente, de acuerdo a la llama del script
        
        ejemplo:
            >> python -m syllabus.main institution=uam curso=symp task=syllabus +db_type='csv'
            >> python -m syllabus.main institution=uam curso=symp task=syllabus +db_type='sqlite'
        """
        DB_TYPE = self.cfg.db_type
        DB_NAME = self.cfg.curso.data[DB_TYPE].source
        DB_TEMARIO = self.cfg.curso.data[DB_TYPE].queries.temario

        TRIM_INIT = self.cfg.curso.calendario.inicio
        TRIM_END = self.cfg.curso.calendario.fin
        TRIM_OFFSET = self.cfg.curso.calendario.uam_offset
        TRIM_SESSIONS = self.cfg.curso.calendario

        CURSO_SHORT = self.cfg.curso.information.short_name
        CURSO_TRIM = self.cfg.curso.information.trimestre

        TRANSLATE = self.cfg.constantes.traduccion
        breakpoint()
        database = self._connect_db(DB_NAME, driver=DB_TYPE)
        temario = database.query(DB_TEMARIO)
        topicos = self.topicos_asdict(temario)

        calendar = Calendario()
        calendar.trimestre(
            TRIM_INIT,
            TRIM_END,
            TRIM_OFFSET,
            TRIM_SESSIONS,
            TRANSLATE
        )
        eventos = calendar.check_eventos(TRIM_SESSIONS.eventos)
        
        latex = SyllabusLatexUAM(
            self.cfg,
            topicos,
            eventos
        )

        path = (
            Path(os.getenv("TEX_FILES_PATH"))
            / f"Syllabus-{CURSO_SHORT}-{CURSO_TRIM}.tex"
        )
        latex.compose()
        latex.publish(path)

        database.disconnect()

    def _connect_db(self, db: str, driver: str = 'sqlite') -> DatabasePort:
        database = (
            LoaderResolver().resolve(
                db,
                driver
             )
         )
        return database
    
    def topicos_asdict(self, temario: pd.DataFrame) -> dict:
        topicos = {}
        for (num_unidad, num_tema), grupo in temario.groupby(['num_unidad', 'num_tema']):
            unidad_titulo = grupo['unidad_titulo'].iloc[0]
            tema_titulo = grupo['tema_titulo'].iloc[0]
            
            subtemas = grupo[['descripcion', 'cobertura']].to_dict('records')
            
            if unidad_titulo not in topicos:
                topicos[unidad_titulo] = {}
            
            topicos[unidad_titulo][tema_titulo] = subtemas
        
        return topicos


class SyllabusLatexUAM(SyllabusPublisherPort):
    def __init__(self, cfg, topicos, eventos) -> None:
        self.cfg = cfg
        self.curso = cfg.curso.information

        self.doc = Document(
            documentclass="article",
            document_options=["11pt", "letterpaper", "spanish"],
            fontenc=None,
            inputenc=None,
            lmodern=False,
            textcomp=False,
            font_size=""
        )
        jinja = JinjaUAMSyllabus(self.cfg)
        self.temario = jinja.render_temario(topicos)
        self.sesiones = jinja.render_sesiones(self.cfg.curso.calendario.sesiones)
        self.eventos = jinja.render_eventos(eventos)
    
    def compose(self) -> str | None | Self:
        self._preamble()
        self._presentacion()
        self._generalidades()
        self._sesiones()
        self._temario()
        self._nota()
        self._referencias()
        self.syllabus = self.doc.dumps()
        return self
    
    def publish(self, path: Path) -> None:
        if hasattr(self, 'syllabus') is False:
            raise ValueError("El syllabus no ha sido renderizado. Llamar al método `compose()` antes.")

        path.write_text(self.syllabus, encoding="utf-8")
        print(f"Syllabus UAM guardado en: {path}")
    
    def _preamble(self) -> None:
        self.doc.packages.append(NoEscape(r"\usepackage{../../../lib/latex/uea_planeacion}"))
        self.doc.packages.append(Package("../../../lib/latex/common"))

        self.doc.packages.append(Package(
            "biblatex",
            options=[
                "backend=biber",
                "style=apa",
                "sorting=none",
                "isbn=true",
                "citestyle=authoryear",
            ],
        ))

        self.doc.preamble.append(NoEscape(r"\addbibresource{../references/bibliografia.bib}"))
        self.doc.preamble.append(NoEscape(r"\AtEveryBibitem{\clearfield{note}}"))
        self.doc.preamble.append(NoEscape(r"\setlength{\bibitemsep}{1em}"))
        self.doc.preamble.append(NoEscape(r"\setlength{\bibhang}{0.5in}"))
        self.doc.preamble.append(NoEscape(rf"\newcommand{{\uea}}{{{self.curso.name}}}"))

    def _presentacion(self) -> None:
        self.doc.append(NoEscape(r"\vspace{2em}"))
        self.doc.append(NoEscape(
            rf"\fecha{{{self.curso.doc_elab.dia}}}{{{self.curso.doc_elab.dia_num}}}{{{self.curso.doc_elab.mes}}}"
          )
        )

        self.doc.append(NoEscape(
rf"""
\begin{{center}}
    \textsc{{\uea, {self.curso.trimestre}}}\\
    \textbf{{{self.curso.tipo}, {self.curso.clave}, {self.curso.grupo}}}\\
\end{{center}}
"""
))
        
    def _generalidades(self) -> None:
        self.doc.append(Section("Generalidades"))
        self.doc.append(Subsection("Datos del profesor", numbering=False))

        with self.doc.create(Tabular(r"l p{0.6\textwidth}")) as t:
            t.add_row((NoEscape(r"\textbf{Profesor:}"),   "Dr. en C. Omar Piña Ramírez"))
            t.add_row((NoEscape(r"\textbf{email:}"),      NoEscape(r"\url{opina.ramirez@izt.uam.mx}")))
            t.add_row((NoEscape(r"\textbf{Cubículo:}"),   "T-227"))
    
    def _sesiones(self) -> None:
        self.doc.append(Section("Sesiones"))
        self.doc.append(NoEscape(self.sesiones))
        self.doc.append(NoEscape(self.eventos))

    def _temario(self) -> None:
        self.doc.append(Section("Temario"))
        self.doc.append(NoEscape(self.temario))
    
    def _nota(self) -> None:
        self.doc.append(Subsection("Calificación y asignación de nota de la UEA", numbering=False))
        self.doc.append(NoEscape(
        r"""
La calificación final $C$ se calculará de la siguiente forma:
\begin{align}
 C &= \begin{bmatrix}
         0.1 \\
         0.1 \\
         3.0 \\
         0.25 \\
         0.25 \\
       \end{bmatrix}
    \begin{bmatrix}
         E_{1}& E_{2}& C_{A}& P_1& P_2
     \end{bmatrix}.
\end{align}

La asignación de nota se realizará de la siguiente forma:
\begin{center}
	\begin{tabular}{rc}
	 \bf Nota en el acta  & \bf Calificación\\
	 MB& [8.6, 10.0]\\
	 B & [7.6, 8.6)\\
	 S & [6.0, 7.6)\\
	 NA& [0.0, 6.0)\\
	\end{tabular}
\end{center}
        """
        ))

    def _referencias(self) -> None:
        self.doc.append(Section("Recursos"))
        self.doc.append(Command("nocite", arguments=NoEscape("*")))
        self.doc.append(Command(
            "printbibliography",
            options=NoEscape("keyword=symp:ip:web, title={Herramientas}")
        ))

        self.doc.append(Section("Bibliografía"))
        self.doc.append(Command(
            "printbibliography",
            options=NoEscape("keyword=ip:main, title={Bibliografía básica}")
        ))
        self.doc.append(Command(
            "printbibliography",
            options=NoEscape("keyword=ip:complement, title={Bibliografía complementaria}")
        ))