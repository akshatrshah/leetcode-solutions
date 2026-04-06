class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            difference = abs(x-y)

            if difference > 0:
                heapq.heappush(heap,-difference)

        return -heap[0] if len(heap) == 1 else 0