# count_evens
def count_evens(nums):
  count = 0
  for n in nums:
    if n % 2 == 0:
      count += 1
  return count
# big_diff
def big_diff(nums):
  return max(nums) - min(nums)
# centered_average
def centered_average(nums):
  nums = sorted(nums)
  return sum(nums[1:-1]) // (len(nums) - 2)
# sum13
def sum13(nums):
    total = 0
    skip = False
    for n in nums:
        if n == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        total += n
    return total
# sum67
def sum67(nums):
  total = 0
  skip = False
  for n in nums:
    if n == 6:
      skip = True
    elif n == 7 and skip:
      skip = False
    elif not skip:
      total += n
  return total
# has22
def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False