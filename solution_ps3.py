from client import Server

if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")
        
        server = Server("http://pac.bouillaguet.info/TP3/PS3/")

        challenge = server.query("PK/verkyndt")
        
        #print(challenge)

        p = challenge['p']
        g = challenge['g']
        h = challenge['h']

        #print("p {0}\ng {1}\nh {2}".format(p,g,h))

        print("\n\n\nRAND resolution done\n\n")
