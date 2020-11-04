"""
module contains the main exception for inheritance
"""
class ServiceError(Exception):
    """
    The main exception for inheritance
    """
    service = None

    def __init__(self, *args):
        super().__init__(self.service, *args)