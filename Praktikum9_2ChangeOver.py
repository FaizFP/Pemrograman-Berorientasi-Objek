#Faiz Firdaus Priyanto 
#064002300005
#Informatika 



class p9e2:
    @staticmethod
    def methodTambahInt(x, y):
        
        if x == float:  # deteck parameter jika float 
            return x + y
        else:             #atau hasil yang lain dia bakal jumlah juga 
            return x + y 

    
    


myNum1 = p9e2.methodTambahInt(8, 5)
myNum2 = p9e2.methodTambahInt(4.5, 6.5)
print("int:", myNum1)
print("float:",myNum2)