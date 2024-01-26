from tire.tire import Tire

class OctoprimeTire(Tire):
    
    def __init__(self, array):
        self._array = array
    
    def needs_service(self):
        sum = 0
        for i in range(len(self._array)):
            sum += self._array[i]
        if sum >= 3:
            return True
        else:
            return False