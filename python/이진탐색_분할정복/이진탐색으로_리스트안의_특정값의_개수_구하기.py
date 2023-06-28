from bisect import bisect_left, bisect_right
lst = [1, 2, 2, 2, 3, 4, 5]

left_idx = bisect_left(lst, 2)
right_idx = bisect_right(lst, 2)

print(right_idx - left_idx)