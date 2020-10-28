def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for list in lists:
        result = append(result, list)

    return result


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    result = 0
    for item in list:
        result = result + 1

    return result


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list):
    return list[::-1]
