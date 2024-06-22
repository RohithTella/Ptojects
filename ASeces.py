import pyaes


class ramznegari():
    def __init__(self):
        self.key = "SaE!d_j@vAd!_uSpS@eid_JaV@d!_U$P"
        self.key = self.key.encode('utf-8')


    def enccc(self,plaintext):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        ciphertext = aes.encrypt(plaintext.encode('utf-8'))
        return ciphertext


    def deccc(self,ciphertext):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        decrypted = aes.decrypt(ciphertext).decode('utf-8')
        return decrypted

