class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 桶排序，最后输出前k个
        # 准备一个频率桶数组
        #  1,2,2,3,3,3, k =2 
        # [1,2,3]
        # [3,2,1]
        # 3,2
        count = {}
        freq = [ [] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)
        # 频率数组
        for num,cnt in count.items():
            freq[cnt].append(num)

        res = []
        # 从最高频率到最低频率来查找
        for i in range(len(freq)-1,0,-1) :
             for num in freq[i]:
                res.append(num)
                if len(res) == k :
                    return res
        
        
        
    