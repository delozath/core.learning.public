from omegaconf import DictConfig

import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import pandas as pd


from syllabus.ports.tasks import SyllabusPort
from syllabus.data.loader import LoaderResolver
from syllabus.tasks.uam.trimestre import Calendario
from syllabus.tasks.uam.jinja_driver import JinjaUAMDriverEnv

from pylatex import Document, Package, Section, Subsection, Tabular, Command
from pylatex.utils import NoEscape


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
            TRIM_OFFSET,
            TRIM_SESSIONS,
            TRANSLATE
        )
        eventos = calendar.check_eventos(TRIM_SESSIONS.eventos)

        latex = SyllabusLatexUAMGenerator(
            self.cfg,
            topicos,
            eventos
        )
        render = latex.compose()
        path = (
            Path(os.getenv("TEX_FILES_PATH"))
            / f"Syllabus-{self.cfg.curso.information.short_name}-{self.cfg.curso.information.trimestre}.tex"
        )
        path.write_text(render, encoding="utf-8")
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

class SyllabusLatexUAMGenerator:
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
        jinja = JinjaUAMDriverEnv(self.cfg)
        self.temario = jinja.render_temario(topicos)
        self.sesiones = jinja.render_sesiones(self.cfg.curso.calendario.sesiones)
        self.eventos = jinja.render_eventos(eventos)
    
    def compose(self) -> str:
        self._preamble()
        self._presentacion()
        self._generalidades()
        self._sesiones()
        self._temario()
        self._nota()
        self._referencias()
        latex = self.doc.dumps()
        return latex
    
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