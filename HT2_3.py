chek=0
while chek==0:
	password1=input("введите сложный пароль: ")
	if len(password1)>8:
		up=0
		lo=0
		for i in range(0,len(password1)):
			up+=int(password1[i].isupper())
			lo+=int(password1[i].islower())
		if up and lo:
			chek=1
	else:
		chek=0
print('пароль успешно введен')