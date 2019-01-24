from crypt import AESCipher

pass_prase = "ndsvndfivndfsvndfsvnldvmdldsf"

cipher = AESCipher(pass_prase)

encryptText = cipher.encrypt("plain text")
print(encryptText)

plainText = cipher.decrypt(encryptText)
print(plainText)

