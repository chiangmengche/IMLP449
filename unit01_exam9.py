# unit01 - 09 Is a palindrome 回文判斷
# 轉換輸入文字為字串
def ConvertInputString():
  rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ")
  rawString = rawInput.lower()
  rawList = list(rawString)
  return rawList   # 變數需要回傳值

# 去除標點符號
def stripAnalphabetics(dirtyList):
  analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "`", "\"" ]
  for character in analphabeticList:
    if character in dirtyList:
      dirtyList.remove(character)
      return stripAnalphabetics(dirtyList)
  return dirtyList

# 回文處理
def runPalindromeCheck(straightList):
  reversedList = straightList[::-1] #[::-1]表示反向字串
  if reversedList == straightList:
    return "The text you have entered is a palindrome!"
  else:
    return "The text you have entered is not a palindrome!"

def main():
  print("\nPalindrome checker")
  originalList = ConvertInputString()
  originalList = stripAnalphabetics(originalList)
  palindromeCheck = runPalindromeCheck(originalList)
  print(palindromeCheck)

main()