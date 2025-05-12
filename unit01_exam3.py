import random

# 程式變數初始化
max = 100
min = 0
ans = random.randint(1,99) # because max = 100
count = 0

while True:
  print('請輸入',min,'< ? <',max, 'input number ranger:', end='') # end=''表示不換行
  guess = int(input('輸入數值:'))
  # 判斷輸入數值範圍正確性
  if guess < max and guess > min:
    count += 1
    if guess == ans:
      print("Your are right!! %d times you guess."%(count))
      break
    elif guess > ans:
      max = guess
      print("Less, %d times you guessed."%(count))
    else:
      min = guess
      print("More, %d times you guessed."%(count))
  else:
    print("Please input number again.")
  