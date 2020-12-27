"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""
import random
# 定义一个fight函数,敌人的血量和攻击力是随机的，属于未知，设置为传参
def fight(enemy_hp, enemy_power):
    # 定义变量存放我的相关数据
    my_hp = 1000
    my_power = 200
    # 展示敌人的生命值与攻击力
    print(f'敌人的血量为{enemy_hp}', f'敌人的攻击力为{enemy_power}')
    # 通过循环增加游戏次数，设置游戏结束判断条件
    while True:
        # 我和敌人的剩余血量
        my_hp = my_hp - enemy_hp
        enemy_hp = enemy_hp - my_hp
        #展开判断
        # 如果我的血量剩余小于0，则我输了，满足结束条件跳出循环
        if my_hp <= 0:
            print('我输了')
            break
        # 如果敌人的剩余血量小于0，则我赢了，满足结束条件跳出循环
        elif enemy_hp <= 0:
            print('我赢了')
            break


if __name__ =="__main__":
    # 设置敌人的血量区间
    hp = [i for i in range(900, 1100)]
    # 敌人的血量从此范围随机选择
    enemy_hp = random.choice(hp)
    # 敌人的攻击力在150-250之间随机选择
    enemy_power = random.randint(150, 250)
    # 调用fight函数开始游戏
    fight(enemy_hp, enemy_power)



