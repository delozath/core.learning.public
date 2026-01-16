import hydra
from omegaconf import DictConfig

from syllabus.core import CoreSyllabus

@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    core = CoreSyllabus(cfg)
    core.run()
    breakpoint()

if __name__ == "__main__":
    main()