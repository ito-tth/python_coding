class BodyCondition:
    def __init__(self,l,t):
        self.l = l
        self.t = t
    def lm(self):
        self.lm = self.l / 100
    def BMI(self):
        BMI = self.t / self.lm / self.lm
        print(BMI)
cls = BodyCondition(163,43)
cls.lm()
cls.BMI()