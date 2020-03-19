class Rational:
    def __init__(self,num=0,den=1):
        self.__coeffnum=num
        self.__coeffden=den

    def __pgcd(self):
        a=self.__coeffnum
        b= self.__coeffden
        reste=1
        while reste!=0:
            reste=a%b
            a=b
            b=reste
        return a

    def produit2(self,fraction2):
        n1=self.__coeffnum
        d1=self.__coeffden
        nres=n1*fraction2.__coeffnum
        dres=d1*fraction2.__coeffden
        fres=Rational(nres,dres)
        return fres

    def __ppcm(self):
        a=self.__coeffnum
        b= self.__coeffden
        return (a*b)/self.__pgcd()

    def setnum(self,a):
        self.__coeffnum=a

    def setden(self,a):
        if a!=0:
            self.__coeffden=a

    def getnum(self):
        return self.__coeffnum

    def getden(self):
        return self.__coeffden

    def affichage(self):
        a=self.__coeffnum
        b= self.__coeffden
        return str(a)+"/"+str(b)

    def simplification(self):
        a=self.__coeffnum
        b= self.__coeffden
        x=a/self.__pgcd()
        y=b/self.__pgcd()
        self.__coeffnum=x
        self.__coeffden=y


    def fractionsEgales(self,f1):
        self.simplification()
        f1.simplification()
        if self.__coeffnum==f1.__coeffnum and self.__coeffden==f1.__coeffden:
            return ("It's good !")
        else:
            return ("It's not good")

    def produit(self, f1):
        num = self.__coeffnum * f1.__coeffnum
        denom = self.__coeffden * f1.__coeffden
        fres = Rational(num, denom)
        return fres

    def division(self,f1):
        num = self.__coeffnum * f1.__coeffden
        denom = self.__coeffden * f1.__coeffnum
        fres=Rational(num, denom)
        fres.simplification()
        return fres

    def somme(self,num,den):
        a=self.__coeffnum
        b=self.__coeffden
        self.__coeffden=den
        k=self.__ppcm()
        self.__coeffden=b
        return (num*(k/den)+a*(k/b))/k



x=Rational(6,4)
y=Rational(6,4)
print(x.fractionsEgales(y))
# fres=x.produit2(y)
# print(fres.getnum(),"/",fres.getden())


