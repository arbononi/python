from time import sleep as s
print()
for i in range(10, -1, -1):
    print("Irá explodir em", i, "segundos....", sep=" ")
    if i == 5:
       print("Você ainda tem chance de cair fora!")
    s(1)

print("Seu tempo acabou!!!")
print("Booooooommmmmmmmm!!!!!!")