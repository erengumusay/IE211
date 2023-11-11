import time
import random

def sum_binary(A, B, n):
    Carry = 0
    C = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        Sum = A[i] + B[i] + Carry
        C[i + 1] = Sum % 2
        Carry = Sum // 2

    C[0] = Carry

    return C


n = 10
A = [random.randint(0, 1) for _ in range(n)]
B = [random.randint(0, 1) for _ in range(n)]

print("Input A:", A)
print("Input B:", B)

start_time = time.time()

result = sum_binary(A, B, n)

end_time = time.time()
computational_time = end_time - start_time

print("Result:", result)
print(f"Computational Time: {computational_time} seconds")
