class Pile:
    def __init__(self):
        self.__pile=[]
    def push(self,e):
        self.__pile.append(e)
    def top(self):
        return self.__pile[len(self.__pile)-1]
    def pop(self):
        if len(self.__pile)!=0:
            a=self.__pile[len(self.__pile)-1]
            del self.__pile[len(self.__pile)-1]
            return a
    def isEmpty(self):
        if self.size()==0:
            return True
        else :
            return False

    def size(self):
        return len(self.__pile)



obj1=Pile()
obj1.push(3)
obj1.push(4)
obj1.push(5)
print(obj1.pop())
print(obj1.size())
