import time
import sys

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            print(f"Step {i*n+j+1}: {arr}")
        if not swapped:
            break

def analyzeSortPerformance(data, description, time_complexity):
    print(f"\n{description} - Starting array: {data}")
    start = time.time()
    bubbleSort(data.copy())
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    print(f"Time Complexity: {time_complexity}\n")

# Original Data
data_original = [5, 2, 9, 1, 5, 6, 8, 3, 4, 7]

# Best Case (Already Sorted)
#data_best = sorted(data_original)
data_best = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

# Average Case (Manually Shuffled)
data_avg = [3, 7, 4, 6, 5, 2, 8, 1, 9, 5]

# Worst Case (Reverse Sorted)
#data_worst = sorted(data_original, reverse=True)
data_worst = [9, 8, 7, 6, 5, 5, 4, 3, 2, 1]

analyzeSortPerformance(data_original, "Original Data", "O(n^2)")
analyzeSortPerformance(data_best, "Best Case (Sorted)", "O(n)")
analyzeSortPerformance(data_avg, "Average Case (Manually Shuffled)", "O(n^2)")
analyzeSortPerformance(data_worst, "Worst Case (Reverse Sorted)", "O(n^2)")