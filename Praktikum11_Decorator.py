#Faiz Firdaus Priyanto
#064002300005
#Decorator 


def nama(func):
    def tambah(a, b, c , d ,e):
        print(a+b+c+d)
        

        return func(a, b,c,d,e)
    return tambah

@nama
def divide(a, b,c,d,e):
    pass

divide("FULL NAME :","MR.","Faiz Firdaus Priyanto","","064002300005")

