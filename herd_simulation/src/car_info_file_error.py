class CarInfoFileError(Exception):
    """
    Custom exception class for errors related to car information files.
    """

    def __init__(self, message):
        super(CarInfoFileError, self).__init__(message)
