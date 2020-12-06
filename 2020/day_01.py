from data import load_day

def parse(lines):
    return list(map(int, lines))

def multiply_two_sum(target, nums):
    difference = {}
    for num in nums:
        if num in difference:
            print(num * difference[num])
        else:
            difference[target-num] = num

def multiply_three_sum(target, nums):
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

lines = load_day(1)
content = parse(lines)

param={'target': 2020, 'nums': content}
multiply_two_sum(**param)
multiply_three_sum(**param)