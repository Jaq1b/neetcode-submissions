class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_count = 0

        # Find the product of all non-zero numbers
        # and count how many zeros there are
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        # If there are 2 or more zeros,
        # every answer will be 0
        if zero_count > 1:
            return [0] * len(nums)

        result = [0] * len(nums)

        # Build the result
        for i, num in enumerate(nums):

            # There is exactly one zero
            if zero_count == 1:
                if num == 0:
                    result[i] = product
                else:
                    result[i] = 0

            # There are no zeros
            else:
                result[i] = product // num

        return result