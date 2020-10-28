def find(search_list, value):
    length = len(search_list)

    if(not length):
        raise ValueError("list can't be empty")
    if(length == 1 and value != search_list[0]):
        raise ValueError("value not found")

    index = length // 2
    middle_value = search_list[index]
    if(value == middle_value):
        return index
    # recursion (tm)
    if(value < middle_value):
        return find(search_list[:index], value)
    else:
        return (index + find(search_list[index:], value))