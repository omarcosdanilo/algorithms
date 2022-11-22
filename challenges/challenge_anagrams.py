def is_anagram(first_string, second_string):
    first_string_ordered = "".join(quick_sort(first_string.lower()))
    second_string_ordered = "".join(quick_sort(second_string.lower()))

    is_anagram = first_string_ordered == second_string_ordered

    if first_string == '' or second_string == '':
        is_anagram = False

    return (
        first_string_ordered,
        second_string_ordered,
        is_anagram
    )


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return (
            quick_sort([x for x in arr[1:] if x < arr[0]])
            + [arr[0]]
            + quick_sort([x for x in arr[1:] if x >= arr[0]])
        )
