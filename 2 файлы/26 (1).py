# 26.Удалить из файла наименьшее нечетное число
# (см. замечание к пре-дыдущей задаче).

f = open("test.txt", "wb")
for i in range(11, 0, -1):
    f.write(i.to_bytes(2, byteorder='big', signed=True))
f.close()

f2 = open("test.txt", "rb+")

num = f2.read(2)
mn = 0

while num != b'':

    x = int.from_bytes(num, byteorder='big', signed=True)
    if x % 2 != 0:
        if not mn:
            print('Я тут')
            mn = x
            ind = f2.tell() - 2
        elif x < mn:
            print("Я поменял")
            mn = x
            ind = f2.tell() - 2

    num = f2.read(2)

f2.seek(-2, 2)
last_n = f2.read(2)
f2.seek(ind, 0)
f2.write(last_n)
f2.seek(-2, 2)
f2.truncate()
f2.close()