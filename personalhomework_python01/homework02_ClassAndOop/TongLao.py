"""
定义一个天山童姥类 ，类名为TongLao，
属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，
如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“师弟是我的！”，
如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），
调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

"""
# 创建一个童姥类
class TongLao():
    # 初始化，并传入血量与攻击力两个属性
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
    # 定义一个看人的方法
    def say_people(self, name):
        if name == "WYZ":
            print("师弟！！！")
        elif name == "李秋水":
            print('师弟是我的！')
        elif name =="丁春秋":
            print("叛徒！我杀了你")
        else:
            print("何方神圣？")

    # 定义一个攻击方法折梅手
    def fight_zms(self, enemy_hp, enemy_power):
        self.hp = self.hp / 2
        self.power = self.power * 10
        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        if self.hp > enemy_hp:
            print("我赢了")
        else:
            print("我输了")


if __name__ == "__main__":
    QQ = TongLao(1000, 200)
    QQ.say_people("qiaofeng")
    QQ.say_people("WYZ")
    QQ.say_people("李秋水")
    QQ.say_people("丁春秋")
    QQ.fight_zms(900,300)


