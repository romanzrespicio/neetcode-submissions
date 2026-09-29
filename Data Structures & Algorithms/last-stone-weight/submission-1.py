class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        
        while len(maxHeap) > 1:
            pop1 = heapq.heappop_max(maxHeap)
            pop2 = heapq.heappop_max(maxHeap)

            if pop1 == pop2:
                continue
            if pop1 > pop2:
                pop1 -= pop2
                heapq.heappush_max(maxHeap, pop1)
        
        return 0 if len(maxHeap) == 0 else maxHeap[0]