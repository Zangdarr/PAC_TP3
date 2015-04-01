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
if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")
        global Crandlib

        server = Server("http://pac.bouillaguet.info/TP3/rand/")        
        
        challenge = server.query("challenge/verkyndt")

        print(challenge)

        

        #dico = { 'key': [0, 42, 666, 1337] }

        #status = server.query("prediction/verkyndt/", dico)

        print("\n\n\nRAND resolution done\n\n")
