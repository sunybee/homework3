# 第一个类1234
class Student:
    name = "小明"
    score = "90"
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def learn(self):
        print("学生%s学习python" % self.name)
    def exercise(self):
        print("学生练习python得分%s" % self.score)
s=Student("小明","90")
s.learn()
s.exercise()

#第二个类
class Teacher:
    name = "小红"
    subject = "python"
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def teach(self):
        print("老师%s教学python" % self.name)
    def exam(self):
        print("老师考试%s" % self.subject)
t=Teacher("小红","python")
t.teach()
t.exam()

#第三个类
class Cat:
    name = "咪咪"
    age = "3"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def call(self):
        print("%s的叫声是喵喵" % self.name)
    def growup(self):
        print("咪咪长大到%s岁了" % self.age)
c=Cat("咪咪","3")
c.call()
c.growup()

#第四个类
class Dog:
    name = "旺旺"
    food = "骨头"
    def __init__(self,name,food):
        self.name = name
        self.food = food
    def protecthome(self):
        print("%s护家看家" % self.name)
    def eat(self):
        print("狗狗吃%s" % self.food)
d=Dog("旺旺","骨头")
d.protecthome()
d.eat()