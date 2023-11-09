#產生1~100之間的隨機數
#讓使用者猜猜看
#猜對: 恭喜猜對了
#猜錯: 告訴使用者 要更大或更小 

import random

print ('猜數字遊戲開始了!')
s = input('請設定範圍最小整數: ')
e = input('請設定範圍最大整數: ')
s = int(s)
e = int(e)
r = random.randint(s,e)
number = input('請輸入你猜的數字: ')
number = int(number)
count = 1

while True:
	if number == r:
		print ('bingo 猜對了，恭喜!')
		break
	else:
		count += 1
		while number != r :
			if number > r:
				print ('猜錯嘍，答案比', number, '更小')
				break
			elif number < r:
				print ('猜錯嘍，答案比', number, '更大')
				break
		print('來猜第', count, '次吧')
		number = input('請重新猜一個數字: ')
		number = int(number)


