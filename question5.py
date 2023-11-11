import time
import random
import matplotlib.pyplot as plt

def linear_search(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return i
    return -1

def generate_random_data(size):
    return [random.randint(0, 100) for _ in range(size)]

def run_tests():
    n_values = [10, 100, 1000]
    v_values = list(range(1, 11))
    results = []

    for n in n_values:
        for v in v_values:
            input_data = generate_random_data(n)

            start_time = time.time()
            result = linear_search(input_data, v)
            end_time = time.time()

            results.append((n, v, result, end_time - start_time))

    return results

def plot_results(results):
    for v in range(1, 11):
        subset_results = [(n, time_value) for n, val, result, time_value in results if val == v]
        n_values, time_values = zip(*subset_results)

        plt.plot(n_values, time_values, marker='o', label=f'v = {v}')

    plt.xlabel('Input Size (n)')
    plt.ylabel('Computational Time (seconds)')
    plt.legend()
    plt.title('Linear Search: Computational Time vs Input Size for different v values')
    plt.show()

if __name__ == "__main__":
    test_results = run_tests()

    for n, v, result, time_value in test_results:
        print(f"n = {n}, v = {v}, Result = {result}, Computational Time = {time_value} seconds")

    plot_results(test_results)
