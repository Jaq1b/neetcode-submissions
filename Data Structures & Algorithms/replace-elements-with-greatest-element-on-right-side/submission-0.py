class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        array = [0] * len(arr)
        
        for i in range(len(arr)):
            highest = 0
            for j in range(i+1,len(arr)):
                if arr[j]>highest:
                    highest = arr[j]
            
            array[i] = highest
        array[-1] = -1
        return array
        