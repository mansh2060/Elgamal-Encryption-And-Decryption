from numba import jit
@jit(nopython=True)

def generate_1000_primes():
    count_primes = 0
    num = 3
    count = 0
    prime_num_list = []
    prime_num_list.append(2)
    while count_primes < 1000:
        for i in range(2,num,1):
            if num % i == 0:
                count += 1
        if count == 0:
            prime_num_list.append(num)
            count_primes += 1
        num += 1
        count = 0
    return prime_num_list

