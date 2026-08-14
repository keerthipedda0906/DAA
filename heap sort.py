def heapify(arr, n, i):
    largest = i
    left = (2 * i) + 1
    right = (2 * i) + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def build_max_heap(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)

    return arr
arr = list(map(int, input("Enter the array elements: ").split()))

print("Original array:", arr)
print("Max Heap:", build_max_heap(arr))

















### Conclusion

The given program successfully converts an array into a **Max Heap** using the heapify method.

.Time Complexity: `O(n)` for building the Max Heap
.Space Complexity:** `O(log n)` due to recursive `heapify()` calls
.Result: The largest element is placed at the root of the heap.




