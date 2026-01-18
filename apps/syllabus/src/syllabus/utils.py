import os
from omegaconf import DictConfig


from jinja2 import Environment, FileSystemLoader


class JinjaDriverEnv:
    """
    Driver base para renderizar plantillas Jinja2 específicas de la UAM. Resuelve los paths de las plantillas.

    Attributes
    ----------
    cfg : DictConfig
        Configuración del entorno.
    """
    def __init__(self, cfg: DictConfig, folder: str) -> None:
        self.cfg = cfg
        root = os.getcwd()
        self.env = Environment(
            loader=FileSystemLoader(
                [
                  f"{root}/apps/syllabus/src/syllabus/tasks/{folder}/templates",
                  f"{root}/syllabus/src/syllabus/tasks/{folder}/templates",
                  f"{root}/src/syllabus/tasks/{folder}/templates",
                  f"{root}/syllabus/tasks/{folder}/templates",
                  f"{root}/tasks/{folder}/templates",
                ]
            )
        )
    
    def render(self, plantilla: str, **kwargs) -> str:
        template = self.env.get_template(plantilla)
        render = template.render(**kwargs)
        return render