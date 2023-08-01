from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    r_idx = bisect_right(array, right_value)
    l_idx = bisect_left(array, left_value)
    return r_idx - l_idx