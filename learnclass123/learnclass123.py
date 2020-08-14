# 第一个类12
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