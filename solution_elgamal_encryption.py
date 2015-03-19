from client import Server
from random import randint


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


if __name__ == '__main__' :
    print("PROGRAM START")
    
    server = Server("http://pac.bouillaguet.info/TP3//ElGamal-encryption/")
    
    parametre = server.query("parameters/verkyndt")   
    p = parametre['p']
    g = parametre['g']

    x = randint(1,p-1)
    gx = pow(g,x,p)
    
    challenge = server.query("challenge/verkyndt",{'h':str(gx)})

    gy = challenge['ciphertext'][0]
    mgxy = challenge['ciphertext'][1]

    gxy = pow(gy,x,p)

    inv = modinv(gxy, p) 

    m = (inv * mgxy) % p 

    print("Message : {0}".format(m))
    status = server.query("validate/verkyndt", {'plaintext': str(m)})
    
    print(status)
     
   
    print("PROGRAM END")
