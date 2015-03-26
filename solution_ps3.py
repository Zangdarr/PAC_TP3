from client import Server

server = Server("http://pac.bouillaguet.info/TP3/PS3/")

def signIt(msg):
  return server.query("sign/verkyndt", {"m": msg})['signature']

if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")
        

        challenge = server.query("PK/verkyndt")
        #print(challenge)

        p = challenge['p']
        g = challenge['g']
        h = challenge['h']
#        print("p {0}\ng {1}\nh {2}".format(p,g,h))

        msg_1 = "42"
        msg_2 = "93"
   
        enc1  = signIt(msg_1)
#        print(enc1)
        r1 = enc1[0]
        s1 = enc1[1]
#        print("r1 : {0}\ns1 : {1}".format(r1,s1))
        enc2  = signIt(msg_2)
#        print(enc1)
        r2 = enc2[0]
        s2 = enc2[1]
#        print("r2 : {0}\ns2 : {1}".format(r2,s2)) 

        k_tmp = (int(msg_1) - int(msg_2)) * (s1- s2)
        
        k = k_tmp % (int(p)-1)
#        print(k)

        x1 = (1/k)
        x2 = int(msg_1)
        x3 = k * s1
        x4 = x3 % p
        x =  x1 * (x2 - x4) % p
        
        print(x)
        print("\n\n\nRAND resolution done\n\n")
