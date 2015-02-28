from Crypto.Cipher import AES
import base64
import os,random
x = int(input("1.Encrypt\n2.Decrypt\nEnter ur choice.."))
BLOCK_SIZE = 16
PADDING = ' '
if x is 1:
    iv = os.urandom(16)
    key = os.urandom(BLOCK_SIZE)
    obj = AES.new(key, AES.MODE_CBC, iv)
    fname = input("Enter Filename to be Encrypted:\n")
    fr = open(fname,'r')
    mes = fr.read().rstrip('\n')
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    encoded = EncodeAES(obj,mes)
    fn = input("Enter Output file name:\n")
    fo = open(fn,'wb')
    fo.write(iv)    
    fo.write(key)    
    fo.write(encoded)
    fr.close()
    fo.close()
else:
    fn= input("Enter filename to decrypt:\n")
    fr = open(fn,"rb")
    lk = fr.read()
    vi = lk[0:16]
    key = lk[16:32]
    encoded = lk[32:]
    obj = AES.new(key, AES.MODE_CBC, vi)
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
    decoded = (DecodeAES(obj, encoded))
    fname = input("Enter Filename to store decrypted data:\n")
    fo = open(fname,'wb')
    fo.write(decoded)
    fo.close()
    
    
