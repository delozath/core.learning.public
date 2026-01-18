from omegaconf import DictConfig

from syllabus.utils import JinjaDriverEnv


class JinjaUAMSyllabus(JinjaDriverEnv):
    def __init__(self, cfg: DictConfig) -> None:
        super().__init__(cfg, "uam")

    def render_temario(self, topicos: dict) -> str:
        render = self.render("uami_temario.tex.j2", temario=topicos)
        return render
    
    def render_eventos(self, eventos: list) -> str:
        render = self.render("uami_eventos.tex.j2", eventos=eventos)
        return render

    def render_sesiones(self, sesiones: dict) -> str:
        render = self.render("uami_sesiones.tex.j2", sesiones=sesiones)
        return render
