"""Dictionary"""

__author__ = "730710295"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the Keys with the Values of a Dictionary"""
    result = {}
    for key in input_dict:
        value = input_dict[key]
        if value in result:
            raise KeyError("Oh no! There's a Dup Key!")
        else:
            result[value] = key
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the Number of Items in Input List"""
    dict_result = {}
    for item in input_list:
        if item in dict_result:
            dict_result[item] += 1
        else:
            dict_result[item] = 1
    return dict_result


def favorite_colors(input_dict: dict[str, str]) -> str:
    """Returns the Most Popular Color"""
    count_color = {}
    for key in input_dict:
        color = input_dict[key]
        if color in count_color:
            count_color[color] += 1
        else:
            count_color[color] = 1

    max_color = None
    max_count = 0
    for color in count_color:
        if count_color[color] > max_count:
            max_color = color
            max_count = count_color[color]
    return max_color


def bins_len(input_list: list[str]) -> dict[int, set[str]]:
    """Bins a list of str into a dict where key is the length of str's and value is a set of str's"""
    result = {}
    idx = 0
    while idx < len(input_list):
        length = len(input_list[idx])
        if length not in result:
            result[length] = []
        if input_list[idx] not in result[length]:
            result[length].append(input_list[idx])
        idx += 1
    return result
