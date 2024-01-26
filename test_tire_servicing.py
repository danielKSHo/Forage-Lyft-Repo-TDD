import unittest

from datetime import date

from tire.tire import Tire
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestSpindlerUpgrade(unittest.TestCase):
    
    def setUp(self):
        self.tire1 = CarriganTire([0, 0.4, 0.8, 0.9])
        self.tire2 = OctoprimeTire([0.8, 0.5, 0.9, 0.8])
        
    # Carrigan Tire Tests
    def test_carrigan_tire_exists(self):
        self.assertIsNotNone(self.tire1)
        
    def test_carrigan_tire_type(self):
        self.assertIsInstance(self.tire1, Tire)
        
    def test_carrigan_tire_has_array(self):
        self.assertIsNotNone(self.tire1.getArray())
        
    def test_carrigan_tire_requires_service(self):
        self.assertTrue(self.tire1.needs_service())
        
    # Octoprime Tire Tests
    def test_octoprime_tire_exists(self):
        self.assertIsNotNone(self.tire2)
        
    def test_octoprime_tire_type(self):
        self.assertIsInstance(self.tire2, Tire)
        
    def test_octoprime_tire_has_array(self):
        self.assertIsNotNone(self.tire2.getArray())

    def test_octoprime_tire_requires_service(self):
        self.assertTrue(self.tire2.needs_service())
        
if __name__ == "__main__":
    unittest.main()