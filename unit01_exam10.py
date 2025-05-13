# unit01 - 10 總成績計算
# Open File
fin_E = open('C:/Steven/Code/Python/HID_Test/my_venv/Unit01/data/english_list.csv', "r", encoding='UTF-8')
fin_M = open('C:/Steven/Code/Python/HID_Test/my_venv/Unit01/data/math_list.csv', "r", encoding='UTF-8')
#fin_E = open('data/english_list.csv', "r", encoding='UTF-8')
#fin_M = open('data/math_list.csv', "r", encoding='UTF-8')
lisE = []
lisM = []
name = []

for line in fin_E.readlines():
  print(line, end='')
  line = line.strip().split(",")
  print(line)
  name.append(line[0])
  lisE.append(line[1])

for line in fin_M.readlines():
  print(line, end='')
  line = line.strip().split(",")
  print(line)
  lisM.append(line[1])

score = []
fout = open("C:/Steven/Code/Python/HID_Test/my_venv/Unit01/data/Score.csv", "w")
#fout = open("data/Score.csv", "w")
line = ''
  
for i in range(1, len(lisE)):
  score.append(int(lisE[i])+int(lisM[i]))
  list1 = [name[i], str(score[i-1]), "\n"]
  print(name[i], str(score[i-1]))  # 依據data files中首列位置決定score[i-1]
    
  line = ",".join(list1)
  fout.write(line)
fin_E.close()
fin_M.close()
fout.close()    
    