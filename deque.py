class deque:
    def __init__(self):
        self.__deque=[]
    def add_first(self,e):
        self.__deque.insert(0,e)
    def add_last(self,e):
        self.__deque.append(e)
    


