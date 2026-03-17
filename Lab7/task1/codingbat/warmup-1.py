# sleep_in
def sleep_in(weekday, vacation):
  return not weekday or vacation
# monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile
# sum_double
def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  return a + b
# diff21
def diff21(n):
  if n > 21:
    return (n - 21) * 2
  return 21 - n
# parrot_trouble
def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)
# makes10
def makes10(a, b):
  if(a == 10 or b == 10 or a+b == 10):
    return True
  return False
# near_hundred
def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10
# pos_neg
def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  return (a < 0 and b > 0) or (a > 0 and b < 0)
# not_string
def not_string(s):
  if s.startswith("not"):
    return s
  return "not " + s
# missing_char
def missing_char(str, n):
  return str[:n] + str[n+1:]
# front_back
def front_back(s):
  if len(s) <= 1:
    return s
  return s[-1] + s[1:-1] + s[0]
# front3
def front3(str):
  return str[:3]*3

