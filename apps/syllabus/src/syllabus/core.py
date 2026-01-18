
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
    def register_task(self, value: dict[tuple[str, str], type]) -> None:
        raise NotImplementedError("Register task is read-only")