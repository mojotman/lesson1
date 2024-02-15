a=float(input('введите любое число a: '))
b=float(input('введите любое число b: '))
maximum=(a>b)*a+(a<b)*b
print('мксимальное число равно: ', end='')
print(maximum)