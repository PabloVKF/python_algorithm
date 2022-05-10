def binary_search(ordered_list: list, wanted_value: any) -> int:
    """
    Do a search with O(log n)

    :param list ordered_list: Ordered list of items
    :param any wanted_value: Value to look for
    :return: index of value
    :raise ValueError: if the value is not in the list
    """
    high: int = len(ordered_list) - 1
    low: int = 0
    while low <= high:
        mid: int = (high + low) // 2
        value: any = ordered_list[mid]
        if value == wanted_value:
            return mid
        if value > wanted_value:
            high = mid - 1
        elif value < wanted_value:
            low = mid + 1
    raise ValueError("Item não encontrado!")


if __name__ == "__main__":
    my_ordered_list = list(range(10))
    print(f"Number of searches: {binary_search(my_ordered_list, 9)}")
