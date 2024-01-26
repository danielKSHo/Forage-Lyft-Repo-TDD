from abc import ABC

class Tire(ABC):
    
    def needs_service(self):
        pass
    
    def getArray(self):
        return self._array