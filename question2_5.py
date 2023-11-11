import time
import random
import matplotlib.pyplot as plt

def sum_binary(A, B, n):
    Carry = 0
    C = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        Sum = A[i] + B[i] + Carry
        C[i + 1] = Sum % 2
        Carry = Sum // 2

    C[0] = Carry

    return C

# Vary n values
n_values = [100, 500, 1000]

# Collect computational times
computational_times = []

for n in n_values:
    A = [random.randint(0, 1) for _ in range(n)]
    B = [random.randint(0, 1) for _ in range(n)]

    start_time = time.time()
    result = sum_binary(A, B, n)
    end_time = time.time()
    computational_time = end_time - start_time

    computational_times.append(computational_time)

    print(f"For n = {n}, Computational Time: {computational_time} seconds")

# Plotting
plt.plot(n_values, computational_times, marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Computational Time (seconds)')
plt.title('Computational Time vs Input Size for Sum Binary Algorithm')
plt.show()
