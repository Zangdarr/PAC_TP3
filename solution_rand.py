import ctypes
from client import Server

Crandlib = ctypes.CDLL("./Crandlib.so")

def XGCD(a,b):
  u = (1, 0) #representation de a
  v = (0, 1) #representation de b

  while b!= 0:
    q,r = divmod(a, b)
    a = b
    b = r
    tmp = (u[0] - q*v[0], u[1] - q*v[1])
    u = v
    v = tmp
  return a, u[0], u[1]

def modinv(a, b):
  g, x, y = XGCD(a,b)
  return x



def getPreviousNext(next):
        a = 1103515245
        b = 12345
        modinv_a = modinv(a,2**32)
        return (((next - b) * modinv_a)%2**32)

#Return 2 U which is the 15 MSBs of iv with the MST at 0 or 1
def getU(iv):
        print("iv {0}".format(iv))
        iv_bis = iv
        u0 = iv<<16
        u1 =32768 | (iv_bis<<16)
        print("u0 : {0}, u1 : {1}, iv : {2}".format(u0,u1,iv))
        return (u0,u1)


#Test if next_try is the good next value to get good_value
def isThatRightValue(next_try,good_value):
       
        Crandlib.srand(next_try)
        tmp = Crandlib.rand()
        tmp = Crandlib.rand()
        print("try : {0}, IV1 : {1}".format(tmp, good_value))
        if(tmp == good_value):
            return True
        return False

def getL():
   return

if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")
        global Crandlib

        server = Server("http://pac.bouillaguet.info/TP3/rand/")        
 
        challenge = server.query("challenge/verkyndt")
	
#        print(262143>>17)	

        print(challenge)
        print(challenge['IV'][0])
        print(challenge['IV'][1])
        #Récupération du next de IV0, on va vérifié que l'on obtient IV1 à partir des next jusqu'à trouver le bon
        next = -1
        u = getU(challenge['IV'][0])
        for i in range(0,2**16):
            try0 = getPreviousNext(u[0] + i)
            try1 = getPreviousNext(u[1] + i)
            
            
            
            if(isThatRightValue(try0,challenge['IV'][1])):
                next = try0
                break
            if(isThatRightValue(try1,challenge['IV'][1])):
                next = try1           
                break

	
        if(next == -1):
           print("next n'a pas été trouvé.")
            

        for i in range(0,4):
           next = getPreviousNext(next)

        Crandlib.srand(next)
        rand = [-1,-1,-1,-1]
        for i in range(0,4):
           rand[i] = Crandlib.rand()

        print(rand)
        key = ""
        for i in range(0,len(rand)):
            key += ""+str(rand[i])
        dico = { 'key': rand }
        server = Server("http://pac.bouillaguet.info/TP3/rand/")
        status = server.query("validation/verkyndt", dico)
        print(status)
        print("\n\n\nRAND resolution done\n\n")
