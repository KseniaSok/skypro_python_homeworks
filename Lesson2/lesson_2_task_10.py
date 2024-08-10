x = int(input('Сумма вклада '))
y = int(input('Срок '))
def bank(x,y):
    for i in range(y):
        x += int(x * 0.1)
    return x
print(bank(x,y))