import time
import random

def linear_search(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return i
    return -1

def generate_random_data(size):
    return [random.randint(0, 100) for _ in range(size)]

if __name__ == "__main__":
    n = 1000

    input_data = generate_random_data(n)
    target_value = random.randint(0, 100)

    start_time = time.time()
    result = linear_search(input_data, target_value)
    end_time = time.time()

    print(f"Input Data: {input_data}")
    print(f"Target Value: {target_value}")

    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the array.")

    print(f"Computational Time: {end_time - start_time} seconds")
