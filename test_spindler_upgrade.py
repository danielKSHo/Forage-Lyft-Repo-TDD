import unittest

from datetime import date

from battery.spindler_battery import SpindlerBattery
from battery.better_spindler_battery import BetterSpindlerBattery

class TestSpindlerUpgrade(unittest.TestCase):
    
    def setUp(self):
        current_date = date.fromisoformat("2021-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        self.battery = BetterSpindlerBattery(current_date, last_service_date)
           
    def test_battery_exists(self):
        self.assertIsNotNone(self.battery)
        
    def test_battery_type(self):
        self.assertIsInstance(self.battery, SpindlerBattery)

    def test_requires_3_year_service(self):
        self.assertTrue(self.battery.needs_service())
        
if __name__ == "__main__":
    unittest.main()