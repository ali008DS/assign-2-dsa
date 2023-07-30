def three_sum_closest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum

            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                return target

    return closest_sum

# Test the function with the given example
nums = [-1, 2, 1, -4]
target = 1
result = three_sum_closest(nums, target)
print(result)  # Output: 2
