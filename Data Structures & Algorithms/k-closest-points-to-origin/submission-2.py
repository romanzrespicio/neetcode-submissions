class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        dct = {}

        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            dis = math.sqrt((x1)**2 + (y1)**2)
            
            if dis not in dct:
                dct[dis] = []
                distances.append(dis)
            
            dct[dis].append(points[i])

        heapq.heapify(distances)

        res = []
        while len(res) < k:
            minDis = heapq.heappop(distances)
            for i in range(len(dct[minDis])):
                if len(res) == k:
                    break
                res.append(dct[minDis][i])
        
        return res