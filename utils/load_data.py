import os
from datasets import load_dataset

class load:
    def __init__(self):
        self.location = os.path.join("data","raw")
    def load(self):
        dataset = load_dataset("cnamuangtoun/resume-job-description-fit")
        dataset.save_to_disk(self.location)

if __name__ == "__main__":
    loader = load()
    loader.load()
