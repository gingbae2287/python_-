class test:
    def __init__(self,num):
        self.a=num
    def change(self, num):
        self.a=num

k=test(8)
t=k
t.change(2)
print(k.a)
