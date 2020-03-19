class Equation:
    def __init__(self,a,b,c):
        self.__coeffa=a
        self.__coeffb=b
        self.__coeffc=c

    def getcoeffa(self):
        return self.__coeffa
    def getcoeffb(self):
        return self.__coeffb
    def getcoeffc(self):
        return self.__coeffc
    def setEquation(self,a,b,c):
        if a!=0:
           self.getcoeffa=a
           self.getcoeffb=b
           self.getcoeffc=c
        else:
            print("l'équation n'as pas de solutions réelles")
    def Resolution(self):
        det=self.__coeffb**2-4*self.__coeffa*self.__coeffc
        if det <0:
            print("l'équation n'as pas de solutions réelles" )
        elif det==0:
            resol0=-self.__coeffb/2*self.__coeffa
            return resol0
        else:
            resol1=(-self.__coeffb-det**0.5)/(2*self.__coeffa)
            resol2=(-self.__coeffb+det**0.5)/(2*self.__coeffa)
            return resol1,resol2
    def affichage(self):
        return str(self.__coeffa)+"x²+"+str(self.__coeffb)+"x+"+str(self.__coeffc)+"=0"

    def Calcul(self,x):
        image=self.__coeffa*x**2+self.__coeffb*x+self.__coeffc
        return image



ob=Equation(2,5,2)
#print(ob.Resolution())
print(ob.Calcul(3))

