def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        steps.append(arr.copy())
    return steps

arr = [22, 27, 16, 2, 18, 6]
steps = insertion_sort(arr.copy())

print("Insertion Sort Steps:")
for i, step in enumerate(steps):
    print(f"Step {i+1}: {step}")

