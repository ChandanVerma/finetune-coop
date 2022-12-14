import os
from pathlib import Path
import sys

sys.path.append(str(Path(os.getcwd())))
sys.path.append(str(Path(os.getcwd()).parent))

from dassl.data.datasets import DATASET_REGISTRY, Datum, DatasetBase

from datasets.oxford_pets import OxfordPets
from datasets.dtd import DescribableTextures as DTD

@DATASET_REGISTRY.register()
class Tagging(DatasetBase):

    dataset_dir = "tagging"

    def __init__(self, cfg):
        root = os.path.abspath(os.path.expanduser(cfg.DATASET.ROOT))
        self.dataset_dir = os.path.join(root, self.dataset_dir)
        self.image_dir = os.path.join(self.dataset_dir)
        self.split_path = os.path.join(self.dataset_dir, "split_zhou_Tagging.json")
        

        if os.path.exists(self.split_path):
            train, val, test = OxfordPets.read_split(self.split_path, self.image_dir)
        else:
            train, val, test = DTD.read_and_split_data(self.image_dir, ignored=IGNORED, new_cnames=NEW_CNAMES)
            OxfordPets.save_split(train, val, test, self.split_path, self.image_dir)

        super().__init__(train_x=train, val=val, test=test)
