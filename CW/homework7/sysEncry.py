from Crypto.Cipher import AES

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value) 

key = 'This is a key123'
value = 'This is an IV456'


obj = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(value))
data = "Hello World!"

encrypted_data = obj.encrypt(add_to_16(data))
print (encrypted_data)

aesObj1 = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(value))
decrypted_data = aesObj1.decrypt(encrypted_data)
print (decrypted_data)

