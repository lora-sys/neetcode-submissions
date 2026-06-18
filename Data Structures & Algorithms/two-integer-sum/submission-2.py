class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx,num in enumerate(nums):
            rest = target - num 
            if  rest in hash_map :
                return  [hash_map[rest] , idx ]
            hash_map[num] = idx

        