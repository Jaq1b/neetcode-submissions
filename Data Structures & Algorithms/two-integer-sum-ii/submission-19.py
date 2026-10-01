class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            l =0
            r = len(numbers)-1

            while l<r:
                diff = numbers[r]+numbers[l]
                if diff>target:
                    r-=1
                elif diff == target:
                    return [l+1,r+1]
                else:
                    l+=1
        