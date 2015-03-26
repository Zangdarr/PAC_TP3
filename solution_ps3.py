from client import Server

if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")
        
        server = Server("http://pac.bouillaguet.info/TP3/PS3/")

        challenge = server.query("PK/verkyndt")
        
        print(challenge)


        print("\n\n\nRAND resolution done\n\n")
