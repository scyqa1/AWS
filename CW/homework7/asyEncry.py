from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read

key_size = 1024

key = RSA.generate(key_size, random_generator)

public_key = key.publickey()
print (public_key)

data = "Hello World!!!!!"

encrypted_data = public_key.encrypt(data, 32)
decrypted_data = key.decrypt(encrypted_data)
