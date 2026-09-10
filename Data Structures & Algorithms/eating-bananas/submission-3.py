class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        record = max(piles)

        while l <= r:
            print(l)
            print(r)
            k = (l + r) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / k)

            if time <= h:
                if k < record:
                    record = k
                r = k - 1

            else:
                l = k + 1

        return record