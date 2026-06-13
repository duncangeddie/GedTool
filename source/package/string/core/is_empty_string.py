#import config
from .config import true_value
from .config import false_value
from .config import empty_strings

#import is_string
from .is_string import is_string

def is_empty_string(data=None):
    #check if data is string
    is_string_check = is_string(data)

    #if data is string
    if is_string_check == true_value:
        #check if data is empty
        if data in empty_strings:
            return true_value
        else:
            return false_value
    #if data is not string
    else:
        return false_value
