def binary_search(array, left, right, value):
    if left == right:
        if value > array[left]:
            return left + 1
        else:
            return left

    if left > right:
        return left

    mid = (left + right) // 2
    if value < array[mid]:
        return binary_search(array, 0, mid - 1, value)
    elif value > array[mid]:
        return binary_search(array, mid + 1, right, value)
    else:
        return mid


def insertion_sort(arr):
    len_arr = len(arr)

    for i in range(1, len_arr):
        if arr[i] < arr[i - 1]:
            k = binary_search(arr, 0, i - 1, arr[i])
            arr = arr[:k] + [arr[i]] + arr[k: i] + arr[i + 1:]

    return arr


print(insertion_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]))
