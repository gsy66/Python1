import random
secret = random.randint (1,10)
i = 1
temp = input('猜一猜数字是啥：')
guess = int(temp)
if guess > secret:
     print('大了大了')
else:
    print('小了小了')
while guess != secret and int(i)<=3 :
    temp = input('再猜一遍：')
    guess = int(temp)
    i = i+1
    if guess == secret:
        print('牛哇')
    else:
        print('你好菜')
        if guess > secret:
            print('大了大了')
        else:
            print('小了小了')
else:
    if guess == secret:
        print("你真聪明")
    else:
        print('这还猜不出来？')
print("游戏结束")
