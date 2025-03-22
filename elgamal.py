import random
from sympy import primitive_root
from generate_large_prime import generate_prime

class ElGamal:
    def __init__(self):
        self.prime_number = generate_prime() 
        self.generator = primitive_root(self.prime_number) 
        self.private_key = random.randint(1, self.prime_number - 2)  
        self.public_key = pow(self.generator, self.private_key, self.prime_number)  

    def generate_keys(self):
        """Returns the public key (p, g, h) and private key (x)."""
        return {
            "public_key": (self.prime_number, self.generator, self.public_key),
            "private_key": self.private_key,
        }

    def encrypt(self, message):
        """Encrypts the message using ElGamal encryption."""
        message = message.encode('utf-8')
        message = int.from_bytes(message, byteorder='big')  # Convert message to int

        if message >= self.prime_number:
            raise ValueError("Message too large for encryption")

        k = random.randint(1, self.prime_number - 2)  # Random ephemeral key
        c1 = pow(self.generator, k, self.prime_number)  # c1 = g^k mod p
        s = pow(self.public_key, k, self.prime_number)  # s = h^k mod p
        c2 = (message * s) % self.prime_number  # c2 = message * s mod p

        return (c1, c2)

    def decrypt(self, ciphertext):
        """Decrypts the ciphertext and retrieves the original message."""
        c1, c2 = ciphertext
        s = pow(c1, self.private_key, self.prime_number)  #  s = c1^x mod p
        s_inv = pow(s, -1, self.prime_number)  #modular inverse of s
        message = (c2 * s_inv) % self.prime_number 

      
        message_bytes = message.to_bytes((message.bit_length() + 7) // 8, byteorder='big')
        return message_bytes.decode('utf-8', errors='ignore')