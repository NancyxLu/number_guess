#產生1~100之間的隨機數
#讓使用者猜猜看
#猜對: 恭喜猜對了
#猜錯: 告訴使用者 要更大或更小 

import random
r = random.randint(1,100)

print ('猜數字遊戲開始了!')
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


