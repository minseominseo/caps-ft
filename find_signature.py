import pickle
import sys
import binascii

def findsig(target_dump, extension):
    sig_size = int(len(extension))
    fd = open(target_dump, 'rb')
    while 1:
        context = fd.read(4096)
        con = binascii.b2a_hex(context)
        con = con[0:sig_size].decode()
        if con == '':
            break
        if extension == con:
            print( '%02X', extension ) 

    fd.close()

if __name__ == "__main__":
    target_dump = sys.argv[1]
    extension = sys.argv[2].upper()
    
    findsig(target_dump, extension)


