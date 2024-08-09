i = input('Введите год: ')
is_year_leap = int(i)

if (is_year_leap % 4 != 0):
    print('True.')
else:
    print('False.')