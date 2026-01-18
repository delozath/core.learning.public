from abc import ABC, abstractmethod
from typing import Self

from omegaconf import DictConfig

import numpy as np
import pandas as pd

class SyllabusOrchestratorPort(ABC):
    cfg: DictConfig
    """
    Attributes
    ----------
    cfg: DictConfig
        Hydra configuration object
    """
    def __init__(self, cfg: DictConfig) -> None:
        self.cfg = cfg

    @abstractmethod
    def build(self):
        """
        Construir el syllabus, el output depende de la implementación
        """
        ...

class SyllabusPublisherPort(ABC):
    cfg: DictConfig
    syllabus: str | object | None
    """
    Attributes
    ----------
    cfg: DictConfig
        Hydra configuration object
    
    syllabus: str | None
        Syllabus generado en formato LaTeX, HTML, PDF, etc.
    """
    def __init__(self, cfg: DictConfig) -> None:
        self.cfg = cfg
    
    @abstractmethod
    def compose(self, *args, **kwargs) -> str | None | Self:
        """
        Componer el syllabus en el formato deseado, puede ser LaTeX, PDF, HTML, etc.

        Parameters
        ----------
        syllabus : Any
            Syllabus generado por el SyllabusGeneratorPort
        """
        ...

    @abstractmethod
    def publish(self, *args, **kwargs) -> None:
        """
        Publicar el syllabus en el medio deseado, puede ser un archivo, una base de datos, etc.

        Parameters
        ----------
        syllabus : Any
            Syllabus generado por el SyllabusGeneratorPort
        """
        ...


class GlobalGradesPort(ABC):
    cfg: DictConfig
    """
    Attributes
    ----------
    cfg: DictConfig
        Hydra configuration object
    """
    def __init__(self, cfg: DictConfig) -> None:
        self.cfg = cfg
    
    @abstractmethod
    def compute(self) -> list | np.ndarray | pd.DataFrame:
        """
        Calcular la calificación final basada en las calificaciones parciales

        Returns
        -------
        list | np.ndarray | pd.DataFrame
            Calificación final en escala {MB, B, S, NA}, 0-10, 0-100 etc, dependiendo de la implementación
        """
        ...

    @abstractmethod
    def grading(self) -> np.ndarray | pd.DataFrame:
        """
        Asignar una nota final basada en criterios específicos

        Returns
        -------
        np.ndarray | pd.DataFrame
            Arreglo o DataFrame con las notas finales asignadas
        """
        ...
        
class PartialGradesPort(ABC):
    cfg: DictConfig
    """
    Attributes
    ----------
    cfg: DictConfig
        Hydra configuration object
    """
    def __init__(self, cfg: DictConfig) -> None:
        self.cfg = cfg    

    @abstractmethod
    def compute(self) -> list | np.ndarray | pd.DataFrame:
        """
        Obtener la calificación de un item evaluado, tarea, examen, proyecto, etc. dependiendo de la rubrica de evaluación

        Returns
        -------
        list | np.ndarray | pd.DataFrame
            Calificación obtenida en el item evaluado
        """
        ...