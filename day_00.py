#print('------------我爱喵呜-----------')
#temp = input("我想的是哪个数呢，猜猜吧")
#guess = int (temp) #赋值，右边给左边
#if guess == 8: #判断相等
#        print("哇，你是我肚子里的蛔虫吗？！")
#        print("切，猜对了是没有奖励的！")
#else:
#    print("猜错啦，我想的是8")
#print("游戏结束，不玩啦^-^")
#改进版
#print('---------喵呜--------')
#temp = input("猜个数字吧，小哥哥")
#guess = int(temp)
#if guess == 8:
#        print('你是神仙吗')
#        print('恭喜你答对了')
#else :
#        if guess > 8:
#                print('哥，大了大了')
#        else:
#                print('小啦小啦')
#print('游戏结束啦，再见')
#加强版
import random
print('---------喵呜--------')
a = random.randint(1,100)
temp = input("猜个数字吧，小哥哥")
guess = int(temp)
while guess != a :
        temp = input('猜错了，再来一次吧')
        guess = int(temp)
        if guess == a:
                print('恭喜你，答对了')
        else:
                if guess > a:
                        print('哥，大了大了')
                else:
                        print('哥，小了小了')
        
print('游戏结束啦')
