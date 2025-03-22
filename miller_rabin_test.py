import random

class MillerRabinTest:
    def __init__(self, prime_number):
        self.number = prime_number

    def calculate_s_d(self):
        s = 0
        d = self.number - 1
        while d % 2 == 0:
            d //= 2
            s += 1
        return s, d

    def calculate_base_a(self):
        for _ in range(1000):  
            a = random.randint(2, self.number - 2)
            if pow(a, self.number - 1, self.number) == 1:
                return a
        return random.randint(2, self.number - 2)

    def calculate_x(self):
        s, d = self.calculate_s_d()
        a = self.calculate_base_a()
        
        x = pow(a, d, self.number)

        if x == 1 or x == self.number - 1:
            return self.number  

        for _ in range(s - 1):
            x = (x * x) % self.number
            if x == self.number - 1:
                return self.number 

        return None  # Composite number
