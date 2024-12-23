class Light:
    """Represents a light that can be turned on and off."""

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


class Door:
    """Represents a door that can be opened and closed."""

    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False
