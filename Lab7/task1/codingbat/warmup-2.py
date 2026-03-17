# string_times
def string_times(str, n):
  return str*n
# front_times
def front_times(str, n):
  return str[:3]*n
# string_bits
def string_bits(str):
  return str[::2]
# string_splosion
def string_splosion(s):
  result = ""
  for i in range(len(s)):
    result += s[:i+1]
  return result
# last2
def last2(s):
  if len(s) < 2:
    return 0
    
  end = s[-2:]
  count = 0
    
  for i in range(len(s) - 2):
    if s[i:i+2] == end:
      count += 1
    
  return count
# array_count9
def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count = count + 1
  return count
# array_front9
def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):
    if nums[i] == 9:
      return True
  return False
# array123
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
# string_match
def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count

