next = 1

def rand(void): # RAND_MAX assumed to be 32767
    next = next * 1103515245 + 12345
    return (next/65536) % 32768;


def srand( seed ):
    next = seed


if __name__ == '__main__':
        print("RAND resolution starting now...\n\n\n")
        print("\n\n\nRAND resolution done\n\n")
