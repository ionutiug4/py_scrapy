from enum import Enum

class OrderStates(Enum):

    CREATED = 'CREATED'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'