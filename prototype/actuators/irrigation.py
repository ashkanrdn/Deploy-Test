class Irrigation:
    def __init__(self):
        self.status = False

    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError
