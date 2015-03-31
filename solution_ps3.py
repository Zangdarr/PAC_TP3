from client import Server

server = Server("http://pac.bouillaguet.info/TP3/PS3/")

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

def signIt(msg):
  return server.query("sign/verkyndt", {"m": msg})['signature']

if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")

        challenge = server.query("PK/verkyndt")
#        print(challenge)

        p = challenge['p']
        g = challenge['g']
        h = challenge['h']
        q = p-1
#        print("p {0}\ng {1}\nh {2}".format(p,g,h))

        msg_2 = 2
        msg_1 = 1
         
        enc1  = signIt(msg_1)
#        print(enc1)
        r1 = enc1[0]
        s1 = enc1[1]
#        print(XGCD(r1,q))
#        print("r1 : {0}\ns1 : {1}".format(r1,s1))
        enc2  = signIt(msg_2)
#        print(enc1)
        r2 = enc2[0]
        s2 = enc2[1]
#        print("r2 : {0}\ns2 : {1}".format(r2,s2)) 

        k = ((msg_1 - msg_2) * (modinv(s1-s2,q))) % q
#        if((r1 % p) == pow(g,k,p)):
#          print("YOOLLLLO") 
#        print(k)

# s0 = (m0 -xr)k⁻¹) => x =  (m0 - (s0 * k))/ r 
        x1 = modinv(r1, q)
        x2 = msg_1
        x3 = (k * s1) %q
        x4 = x3 % q
        x =  (x1 * (x2 - x3)) % q
        
 #       print(x)
 #       if(h==pow(g,x,p)):
 #         print("POW OK")
        status = server.query("validate/verkyndt", {"x":x})

        print(status)
        print("\n\n\nRAND resolution done\n\n")
