from battery.spindler_battery import SpindlerBattery
from utils import add_years_to_date


class BetterSpindlerBattery(SpindlerBattery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)
        
    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
