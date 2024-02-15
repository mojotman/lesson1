a=int(input('введите целое число a: '))
b=int(input('введите целое число b: '))
c=int(input('введите целое число с: '))
print('совпадающих цифр: ',end='')
if a==b==c:
	itog=3
elif a==b or a==c or b==c:
	itog=2
else:
	itog=0
print(itog)
