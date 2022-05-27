import os.path
f = open('dead.txt', 'w')
f.close()
try:
    os.rename("dead.txt", "new.txt")
except FileExistsError:
    print("Файл уже сущетвует")
print(os.path.exists("new.txt"))
f.close()
