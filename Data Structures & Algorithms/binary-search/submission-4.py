class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1
        l = 0
        while l<=r:
            m = l+ ((r-l)//2) #midpoint calculation
            if nums[m]>target:  #checks if indice at midpoint is greater than midpoint if so decrease right pointer by midpoint -1
                r = m-1
            elif nums[m]<target: #if value at nums[m] less than target we need to add midpoint +1 to left pointer to cut time
                l = m+1
            else:
                return m # else return value
        return -1 #-1 clause
        


        