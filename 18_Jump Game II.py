def jump(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):  # We don't need to process the last index
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break

    return jumps


# Example usage
nums = [2, 3, 1, 1, 4]
print(jump(nums))  # Output: 2
