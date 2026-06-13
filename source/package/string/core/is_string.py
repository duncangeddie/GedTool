#import config
from .config import true_return
from .config import false_return

def is_string(data=None):
    #check if data is string
    is_string = isinstance(data, str)

    #return result based on is_string
    if is_string == True:
        return true_return
    else:
        return false_return