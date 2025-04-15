from abc import ABC, abstractmethod

class Abstract(ABC):


    @abstractmethod
    def add_product(self, *args, **kwargs):
        pass
