class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 构建频率数组
        count = {}
        for num in nums :
            count[num] = 1 + count.get(num,0)
        # 构建一个堆 
        heap = []
        for num in count.keys():
            # heapq 最小堆
            # example [[1,3],[3,1],[2,2]]
            # 推入时候，按照最小频次来直接推倒堆顶
            heapq.heappush(heap , (count[num],num))
            # 如果此时超出k, 就是出发弹出，弹出堆顶，频次最低的
            if len(heap) > k :
                heapq.heappop(heap)
        
        res = []
        for i in range(k) :
            res.append(heapq.heappop(heap)[1])
        return res    
        
        
        
    