
from syllabus.ports.tasks import (
    GlobalGradesPort,
    PartialGradesPort,
    SyllabusOrchestratorPort
)


from syllabus.tasks.uam import SyllabusUAMTask

class CoreSyllabus:
    def __init__(self, cfg):
        self.cfg = cfg
        self._wire_tasks()
    
    def _wire_tasks(self):
        """
        Registra las tareas disponibles en el core de syllabus y las asocia a su respectiva clase

        Este diccionario basa el key del diccionario en una tupla (institution, task)
        para facilitar la busqueda de la clase correspondiente a la tarea solicitada
        por el usuario en el archivo de configuración YAML y en la llamada del script.

        En otras palabras, este método es la clave de la extensibilidad del framework,
        permitiendo agregar nuevas instituciones y tareas sin modificar la estructura
        principal del core de syllabus.
        """
        self._register_task = {
            ("UAM-I", "syllabus"): SyllabusUAMTask
        }
    
    def run(self):
        instance = self._caller()(self.cfg)
        if isinstance(instance, SyllabusOrchestratorPort):
            instance.build()
        elif isinstance(instance, (GlobalGradesPort, PartialGradesPort)):
            instance.compute()
        else:
            raise NotImplementedError(f"No method to run found in the selected task instance {instance.__class__.__name__}")
        
        print("CoreSyllabusApp is running")
    
    def _caller(self):
        institution, task = self.cfg.task, self.cfg.institution.information.short_name
        cls_ref = self.register_task.get((task, institution), None)
        if cls_ref is None:
            raise ValueError(f"No task found for {task} and institution {institution}")
        return cls_ref
    
    @property
    def register_task(self) -> dict[tuple[str, str], type]:
        return self._register_task
    
    @register_task.setter
    def register_task(self, _: dict[tuple[str, str], type]) -> None:
        raise NotImplementedError("Register task is read-only")