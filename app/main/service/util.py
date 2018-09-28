import stringcase
import string
from random import randint, choice
from typing import Dict


def transform_dict_key(data: Dict,
                       transform_func=stringcase.snakecase) -> Dict:
    """
    Convert a nested dictionary from one convention to another.
    Args:
        data (dict): dictionary (nested or not) to be converted.
        transform_func (func): function that takes the string in one
        convention and returns it in the other one.
    Returns:
        Dictionary with the new keys.
    """
    new = {}
    for k, v in data.items():
        new_v = v
        if isinstance(v, dict):
            new_v = transform_dict_key(v, transform_func)
        elif isinstance(v, list):
            new_v = list()
            for x in v:
                if isinstance(x, dict):
                    new_v.append(transform_dict_key(
                        x, transform_func))
                else:
                    new_v.append(x)
        new[transform_func(k)] = new_v
    return new


def generate_random_string(char_num: int) -> str:
    all_char = string.ascii_letters.upper()
    return "".join(choice(all_char) for x in range(randint(char_num, char_num)))
