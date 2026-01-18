from jinja2 import Environment, FileSystemLoader, Template

import pandas as pd
from omegaconf import DictConfig


class JinjaUAMDriverEnv():
    def __init__(self, cfg: DictConfig) -> None:
        self.cfg = cfg
        self.env = Environment(
            loader=FileSystemLoader(
                f"{self.cfg.constantes.path.root}/syllabus/tasks/uam/templates/"
            )
        )

    def render_temario(self, topicos: pd.DataFrame) -> str:
        template = self.env.get_template("uami_temario.tex.j2")
        render = template.render(
            temario=topicos
        )
        return render
    
    def render_eventos(self, eventos: list) -> str:
        template = self.env.get_template("uami_eventos.tex.j2")
        render = template.render(
            eventos=eventos
        )
        return render
    
    def render_sesiones(self, sesiones: dict) -> str:
        template = self.env.get_template("uami_sesiones.tex.j2")
        render = template.render(
            sesiones=sesiones
        )
        return render
