from tire.tire import Tire

class CarriganTire(Tire):
    
    def __init__(self, array):
        self._array = array
    
    def needs_service(self):
        for i in range(len(self._array)):
            if self._array[i] >= 0.9:
                return True
        return False
            
        
       