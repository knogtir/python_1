#定义一个函数，有两个参数返回参数的积
def discount(old_price,rate):
    new_price = old_price * rate
    return new_price

old_price = float(input("请输入原价："))
rate = float(input("请输入折扣："))
new_price = discount(old_price,rate)
print("打折后的价钱是：",new_price)
