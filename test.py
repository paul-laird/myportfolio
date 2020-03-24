class test:
    def __init__(self,greeting):
        self.greeting=greeting
    def greet(self,name):
        print(self.greeting,name)
    def ignore(self,X='q'):
        print('Not doing anything with X')
