from omegaconf import DictConfig

from syllabus.ports.tasks import SyllabusPort

class SyllabusUAMTask(SyllabusPort):
    def __init__(self, cfg: DictConfig) -> None:
        super().__init__(cfg)
    
    def build(self):
        mock = f"Syllabus de la UAM para el curso {self.cfg.curso.information.name} ({self.cfg.curso.information.clave})"
        print(mock)
        