class CarInfoFileError(Exception):
    def __init__(self, message):
        super(CarInfoFileError, self).__init__(message)
