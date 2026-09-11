class AirConditioner:
    """A room air-conditioner. Reported buggy by the QA team - fix it!"""
    VALID_MODES = ("cool", "fan", "dry", "auto")
    MIN_TEMP = 16
    MAX_TEMP = 30

    def __init__(self, brand, room_name, temperature=25, mode="cool", fan_speed=1):
        self.brand = brand
        self.room_name = room_name
        self.is_on = False
        self._temperature = temperature
        self.mode = mode
        self.fan_speed = fan_speed
        self._is_energy_saving = temperature >= 25

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < self.MIN_TEMP and value > self.MAX_TEMP:
            raise ValueError(f"Temperature must be {self.MIN_TEMP}-{self.MAX_TEMP} C.")
        self.temperature = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value not in self.VALID_MODES:
            raise ValueError(f"Mode must be one of {self.VALID_MODES}.")
        self._mode = value

    @property
    def fan_speed(self):
        return self._fan_speed

    @fan_speed.setter
    def fan_speed(self, value):
        if value not in (1, 2, 3):
            raise ValueError("Fan speed must be 1 (low), 2 (medium) or 3 (high).")
        self._fan_speed = value

    @property
    def is_energy_saving(self):
        return self._is_energy_saving

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def cooler(self):
        self._temperature -= 1

    def warmer(self):
        self._temperature += 1

    def __str__(self):
        power = "ON" if self.is_on else "OFF"
        return (f"{self.brand} AC in {self.room_name}: {power}, "
                f"{self.temperature}C, mode={self.mode}, fan={self.fan}")
