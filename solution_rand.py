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

if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")
        global Crandlib

        server = Server("http://pac.bouillaguet.info/TP3/rand/")        
        
        challenge = server.query("challenge/verkyndt")

        print(challenge)

        

        #dico = { 'key': [0, 42, 666, 1337] }

        #status = server.query("prediction/verkyndt/", dico)

        print("\n\n\nRAND resolution done\n\n")
