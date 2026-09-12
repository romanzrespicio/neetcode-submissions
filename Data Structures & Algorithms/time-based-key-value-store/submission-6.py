class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append([timestamp, value])
        else:
            self.table[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""

        l, r = 0, len(self.table[key]) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            val = self.table[key][mid]

            if val[0] < timestamp:
                l = mid + 1
            elif val[0] > timestamp:
                r = mid - 1
            else:
                return val[1]

        mid = (l + r) // 2
        val = self.table[key][mid]
        print(val)
        if val[0] <= timestamp:
            res += val[1]

        return res