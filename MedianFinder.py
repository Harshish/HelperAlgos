from collections import defaultdict
from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.left, self.right = [], []
        self.lazy = defaultdict(int)
        self.sum_left, self.sum_right, self.lsize, self.rsize = 0, 0, 0, 0

    def _balance(self):
        if self.lsize > self.rsize + 1:
            self._prune(True)
            maxval = -heappop(self.left)
            self.sum_left -= maxval
            self.lsize -= 1
            heappush(self.right, maxval)
            self.sum_right += maxval
            self.rsize += 1
            self._prune(True)
        elif self.rsize > self.lsize:
            self._prune(False)
            minval = heappop(self.right)
            self.sum_right -= minval
            self.rsize -= 1
            heappush(self.left, -minval)
            self.sum_left += minval
            self.lsize += 1
            self._prune(False)

    def _prune(self, is_left):
        l = self.left if is_left else self.right
        sign = -1 if is_left else 1
        while l and self.lazy[sign * l[0]]:
            self.lazy[sign * l[0]] -= 1
            heappop(l)

    def add(self, val):
        if not self.left or val <= -self.left[0]:
            heappush(self.left, -val)
            self.sum_left += val
            self.lsize += 1
        else:
            heappush(self.right, val)
            self.sum_right += val
            self.rsize += 1

        self._balance()

    def remove(self, val):
        sign = -1 if val <= -self.left[0] else 1
        self.lazy[val] += 1
        if sign == -1:
            self.lsize -= 1
            self.sum_left -= val
            if val == -self.left[0]:
                self._prune(True)
        else:
            self.rsize -= 1
            self.sum_right -= val
            if val == self.right[0]:
                self._prune(False)
        self._balance()

    def get_median(self):
        if len(self.left) == 0:
            return None
        return -self.left[0]

    def get_size(self):
        return self.lsize, self.rsize

    def get_sum(self):
        return self.sum_left, self.sum_right
