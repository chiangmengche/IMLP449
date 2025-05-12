n = int(input('input loop cycle:'))
for i in range(0, n, 1):
  semester = input("輸入課程期數:")
  course = input("輸入課程名稱:")

  # Display the input content
  print("--------------------")
  print("第%s期 - %s"%(semester, course))
  print("--------------------")
