from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256

class AttributeEncryption:
    def __init__(self, key):
        self.key = key
    def encrypt(self, plaintext, attributes):
        # Convert the attributes to a string
        attr_str = str(attributes)

        # Hash the attributes to get a fixed-length key
        attr_key = SHA256.new(attr_str.encode()).digest()

        # Use the attribute key to encrypt the plaintext
        cipher = AES.new(attr_key, AES.MODE_CBC)
        iv = cipher.iv
        ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

        # Return the ciphertext, IV, and attributes
        return (ciphertext, iv, attributes)

    def decrypt(self, ciphertext, iv, attributes):
        # Convert the attributes to a string
        attr_str = str(attributes)

        # Hash the attributes to get a fixed-length key
        attr_key = SHA256.new(attr_str.encode()).digest()

        # Use the attribute key to decrypt the ciphertext
        cipher = AES.new(attr_key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        # Return the plaintext
        return plaintext.decode()
# Create an instance of AttributeEncryption with a random key
key = get_random_bytes(16)
key1=get_random_bytes(4)
print(key1)
ae = AttributeEncryption(key)

# Encrypt the plaintext with attributes
plaintext = 'Hello, world!'
attributes = {'name': 'Alice', 'age': 30}
ciphertext, iv, attrs_out = ae.encrypt(plaintext, attributes)

# Decrypt the ciphertext with the same attributes
plaintext_out = ae.decrypt(ciphertext, iv, attributes)

# Print the results
print(f'Plaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')
print(f'IV: {iv}')
print(f'Attributes: {attributes}')
print(f'Attributes Out: {attrs_out}')
print(f'Plaintext Out: {plaintext_out}')
