"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def sum_two_numbers(nums, k):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)-1):
            if (k - nums[i]) == nums[j]:
                return True

    return False


test_nums = [1, 2, 3, 4]
test_k = 8
print(sum_two_numbers(test_nums, test_k))
