import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heapq.heapify(li) rearranges the elements of the list into a valid heap in-place.
        # Output list represents the heap structure and its first element will always be the smallest element (in a min-heap).

        minHeap = []

        # Adding the distance to the first index
        for x,y in points:
            minHeap.append([(x**2)+(y**2),x,y])

        # rearranges the elements of the list into a valid heap in-place.
        heapq.heapify(minHeap)

        res = []

        while k>0:
            # Poping element to the smallest distance first and adding to the result to return
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        
        return res