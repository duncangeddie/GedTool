#import config
from .config import true_value
from .config import false_value

def is_string(data=None):
    #check if data is string
    is_string = isinstance(data, str)

    #return result based on is_string
    if is_string == true_value:
        return true_value
    else:
        return false_value