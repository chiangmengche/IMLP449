num = int(input()) # input string or number
print(type(num))

if num % 2 == 0:
  print('The number is even.')
else:
  print('The number is odd.')

if num>=1 and num <=1000:
  print('The number range is correct')
else:
  print('The number is out of range')


import time

print('UTC Time:', time.gmtime())