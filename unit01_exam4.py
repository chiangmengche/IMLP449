#word = input()
#print("你用了幾個%d文字述説内心的想法"%(len(word)))

s = '''一片花飛減卻春，風飄萬點正愁人。
且看欲盡花經眼，莫厭傷多酒入唇。
江上小堂巢翡翠，苑邊高塚臥麒麟。
細推物理須行樂，何用浮名絆此身！
朝回日日典春衣，每日江頭盡醉歸。
酒債尋常行處有，人生七十古來稀。
穿花蛺蝶深深見，點水蜻蜓款款飛。
傳語風光共流轉，暫時相賞莫相違。
'''
'''
print("------------------------------")
# 檢查文字出現在s文章中的次數
string = input("請輸入要檢查次數的文字：")
s_num = s.count(string)
print("此'%s'出現的次數為%d次"%(string, s_num))
'''
print("------------------------------")
# 去除標點符號，。！
for i in '，。！\n ':
  s= s.replace(i,'') # replace(old, new)
print(s)

#目前s出現最多此文字的次數
#目前出現最多次的字
# initial
maxstring_cnt = 0
max_string = ''

print ('s文章的總字數:', len(s))

for astr in s:
  print(astr)
  act = s.count(astr)
  if act > maxstring_cnt:
    maxstring_cnt = act
    maxchar = astr
else:
  print("出現最多次的字是'%s', 出現次數為'%d'次"%(maxchar, maxstring_cnt))
  