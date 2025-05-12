# Unit01 - 06 及格名單
m = {'Michael', 'John', 'Stephanie', 'Arwen', 'Steven'}
e = {'Stephanie', 'Arwen', 'Audrey', 'Ken', 'Joe'}
a = m.intersection(e) # m 與 e的交集
a1 = list(a)
a1.sort()  # 排序
print(a)
print(type(a))
print(a1)
print(type(a1))

b = m.difference(a) # m-a, Math PASS, but English Fail
b1 = list(b)
b1.sort()
print(b1)

c = e.difference(a) # e-a, English PASS, but Math Fail
c1 = list(c)
c1.sort()
print(c1)

full = m.union(e) # All students list
d1 = list(full)
d1.sort()
print(d1)