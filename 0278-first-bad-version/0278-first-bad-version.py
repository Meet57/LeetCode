# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# we have to find the defective one so start with binary search mid then choose left and right accordinginly
# 

# | Step | `first` | `last` | `mid` | `isBadVersion(mid)` | Action                               |
# |------|---------|--------|-------|----------------------|--------------------------------------|
# | 1    | 1       | 10     | 5     | False               | Move `first` to `mid + 1` (6)       |
# | 2    | 6       | 10     | 8     | True                | Move `last` to `mid` (8)            |
# | 3    | 6       | 8      | 7     | True                | Move `last` to `mid` (7)            |
# | 4    | 6       | 7      | 6     | True                | Move `last` to `mid` (6)            |


# | Step | `first` | `last` | `mid` | `isBadVersion(mid)` | Action                               |
# |------|---------|--------|-------|----------------------|--------------------------------------|
# | 1    | 1       | 10     | 5     | True                | Move `last` to `mid` (5)            |
# | 2    | 1       | 5      | 3     | False               | Move `first` to `mid + 1` (4)       |
# | 3    | 4       | 5      | 4     | True                | Move `last` to `mid` (4)            |

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first, last = 1, n

        while first < last:
            mid = (first + last)//2

            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1

        return first