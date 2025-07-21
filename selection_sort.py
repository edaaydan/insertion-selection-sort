def selection_sort_partial(arr, steps_to_show=4):
    steps = []
    n = len(arr)
    for i in range(steps_to_show):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
    return steps

arr = [7, 3, 5, 8, 2, 9, 4, 15, 6]
steps = selection_sort_partial(arr.copy())

print("Selection Sort First 4 Steps:")
for i, step in enumerate(steps):
    print(f"Step {i+1}: {step}")
