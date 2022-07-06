from typing import List

from config import SAMPLES_FILE_NAME
import csv


class LocalWriter:
    _instance = None
    keys = None

    @staticmethod
    def get_instance(keys):
        return LocalWriter(keys) if LocalWriter._instance is None else LocalWriter._instance

    def __init__(self, keys: List):
        if LocalWriter._instance is not None:
            raise Exception("Writer class has already its single instance!")
        else:
            LocalWriter._instance = self

        with open(SAMPLES_FILE_NAME) as f:
            features = f.read().split(',')
            if not features:
                self.store_local(keys)
                self.keys = keys
            elif set(features) == set(keys):
                raise Exception("Features keys has changed!")

    def store_local(self, samples):
        with open(SAMPLES_FILE_NAME) as f:
            sample_writer = csv.DictWriter(f, fieldnames=self.keys)
            sample_writer.writerow(samples)
