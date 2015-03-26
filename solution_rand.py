import ctypes
from client import Server

Crandlib = ctypes.CDLL("./Crandlib.so")

if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")
        global Crandlib

        server = Server("http://pac.bouillaguet.info/TP3/rand/")        
        
        challenge = server.query("challenge/verkyndt")

        print(challenge)

        

        #dico = { 'key': [0, 42, 666, 1337] }

        #status = server.query("prediction/verkyndt/", dico)

        print("\n\n\nRAND resolution done\n\n")
