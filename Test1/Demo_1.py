class Animal:
    def __init__(self,name,color,age,sex):
        self.name=name
        self.color=color
        self.age=age
        self.sex=sex
    def canRun(self):
        print(self.name+"正在跑步")
    def canCall(self):
        print(self.name + "正在叫")
class Cat(Animal):
    hair = "短毛"
    # def __init__(self):
    #   super(Cat, self).__init__(self.name,self.color,self.age,self.sex)
    #   Animal.__init__(self.name,self.color,self.age,self.sex)
    def catchMouse(self):
        print(self.name+self.color+self.age+self.sex+self.hair+"正在捉老鼠")
    def canCall(self):
        print(self.name + "正在喵喵叫")
if __name__=="__main__":
    c1=Cat("小七","黑色","0.8","M")
    c1.canCall()
    c1.catchMouse()
    c1.canRun()

