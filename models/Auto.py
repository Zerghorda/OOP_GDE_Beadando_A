from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij

    def get_rendszam(self):
        return self._rendszam

    def get_tipus(self):
        return self._tipus

    def get_berleti_dij(self):
        return self._berleti_dij

    @abstractmethod
    def info(self):
        pass