import random
import time

def shell_sort(data):
    n = len(data)
    gap = n // 2
    num_comparisons = 0
    num_swaps = 0
    
    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                num_comparisons += 1
                data[j] = data[j - gap]
                j -= gap
                num_swaps += 1
            if j != i:
                data[j] = temp
                num_swaps += 1
        gap //= 2
    
    return num_comparisons, num_swaps

def perform_tests(array_size, num_tests=10):
    total_comparisons = 0
    total_swaps = 0

    for i in range(1, num_tests + 1):
        data = [random.randint(1, 100000) for _ in range(array_size)]
        start_time = time.time()  
        comparisons, swaps = shell_sort(data)
        elapsed_time = time.time() - start_time  
        total_comparisons += comparisons
        total_swaps += swaps
        
        print(f"Test no. {i}:")
        print(f"Performed {comparisons} comparisons and {swaps} swaps.")
        print(f"Test duration: {elapsed_time:.6f} seconds")  

    print(f"Average number of swaps: {total_swaps / num_tests}")

array_size = 35000  
perform_tests(array_size)
