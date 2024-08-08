def bank():
    x = int(input('Сумма вклада '))
    y = int(input('Срок '))
    for i in range(y):
        x += int(x * 0.1)
    return x
print(bank())