from input.parse_data import parse_data


def multiply_two_sum(input_file, target):
    nums = parse_data(input_file)
    difference = {}
    for num in nums:
        if num in difference:
            print(num * difference[num])
        else:
            difference[target-num] = num

def multiply_three_sum(input_file, target):
    nums = parse_data(input_file)
    nums.sort()
    for i in range(len(nums)):
        l, r = i + 1, len(nums)-1
        while l < r:
            _sum = nums[i] + nums[l] + nums[r]
            if _sum == target:
                print(nums[i] * nums[l] * nums[r])
                break

            if _sum > target:
                r -= 1
            elif _sum < target:
                l += 1

param={'input_file': 'input/day_01', 'target': 2020}
multiply_two_sum(**param)
multiply_three_sum(**param)
