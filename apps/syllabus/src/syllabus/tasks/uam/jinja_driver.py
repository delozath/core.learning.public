from jinja2 import Environment, FileSystemLoader

import pandas as pd
from omegaconf import DictConfig


class JinjaUAMDriver():
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