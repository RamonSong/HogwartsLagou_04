"""
用类和面向对象的思想，
“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saying(self):
        print("我可以说话")

    def working(self):
        print("我可以工作")

    def thinking(self):
        print('我可以天马行空的想象')



class Cars():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


    def running(self):
        print("我可以代步")

    def lighting(self):
        print("我可以照亮远方")

    def sharing(self):
        print('我可以分享给你音乐')


class Computer():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def jisuan(self):
        print('我可以进行计算')

    def writing(self):
        print('我可以进行写入')

    def online(self):
        print('我可以进行上网')



class Vegetables():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def eating(self):
        print("我可以为你提供营养")

    def juice(self):
        print('我可以变成果汁为你解渴')

    def planting(self):
        print('我可以用来种植')


class Books():
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def reading(self):
        print("读我可以使你平静")

    def testing(self):
        print("我可以用来测试您的学习成绩")

    def present(self):
        print('我可以是有意义的礼品')



if __name__ =="__main__":
    a = Human("小王", 19)
    a.saying()
    a.working()
    a.thinking()

    b = Cars("宝马", 300000)
    b.running()
    b.lighting()
    b.sharing()

    c = Computer("联想", 5000)
    c.jisuan()
    c.online()
    c.writing()

    d = Vegetables("菠菜", 2)
    d.eating()
    d.juice()
    d.planting()

    e = Books("平凡的世界", "路遥")
    e.present()
    e.reading()
    e.testing()