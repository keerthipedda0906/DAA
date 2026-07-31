ef partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort Function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Input from user
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Perform Quick Sort
quick_sort(arr, 0, n - 1)

# Display the sorted array
print("\nSorted Array:")
for i in arr:
    print(i, end=" ")

# Print Time and Space Complexity
print("\n\nTime Complexity : O(n log n) (Average), O(n²) (Worst)")
print("Space Complexity: O(log n)")
