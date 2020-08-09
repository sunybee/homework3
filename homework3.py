__author__ = 'SUN'
##第一次python

##给我和对手赋值血量和攻击力
my_hp = 1000
my_power = 200
your_hp = 1000
your_power = 199

##循环一直为真
while True:
#这次血量=上次血量-对手攻击力
    my_hp = my_hp - your_power
    your_hp = your_hp - my_power
#如果谁的血量先小于等于0，就认定为谁输，跳出循环
    if my_hp <= 0:
        print("我输了")
        print(my_hp)
        break
    elif your_hp <= 0:
        print("你输了")
        print(your_hp)
        break