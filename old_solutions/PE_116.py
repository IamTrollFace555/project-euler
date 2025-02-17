import sys

sys.path.append("../")
from utils import timer, digit_sum

count = [[], [], [1, 1, 1] + [0] * 48, [1, 1, 1, 1] + [0] * 47, [1, 1, 1, 1, 1] + [0] * 46]
# count = [[], [], [1, 1, 1] + [0] * 3, [1, 1, 1, 1] + [0] * 2, [1, 1, 1, 1, 1] + [0] * 1]

max_track_length = 50

for block_length in [2, 3, 4]:
    for track_length in range(block_length + 1, max_track_length + 1):
        for pad in range(track_length - block_length + 1):
            count[block_length][track_length] += count[block_length][pad] * count[block_length][track_length - pad - 2] + 1


def array_sum(arr):
    s = 0
    for elem in arr[2:]:
        s += elem[-1]
    return s/2

print(array_sum(count))