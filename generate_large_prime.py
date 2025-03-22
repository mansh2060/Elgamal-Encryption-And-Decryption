import random
from generate_1000_primes import generate_1000_primes
from miller_rabin_test import MillerRabinTest

prime_number_list = generate_1000_primes()

def generate_prime():
    while True: 
        bin_1024 = [random.randint(0, 1) for _ in range(150)]
        bin_1024.append(1)
        bin_1024 = int("".join(map(str, bin_1024)), 2)

        if bin_1024 % 4 == 3 and bin_1024 % 2 != 0:
            if all(bin_1024 % prime != 0 for prime in prime_number_list):
                miller_rabin_test = MillerRabinTest(bin_1024)
                number = miller_rabin_test.calculate_x()
                if number is not None:
                    return bin_1024 
