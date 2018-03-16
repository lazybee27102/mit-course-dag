from random import randint


def peek1d_finder(array, left, right):
    middle = (left + right) // 2
    if array[middle] < array[middle - 1]:
        return peek1d_finder(array, left, middle - 1)
    elif array[middle] < array[middle + 1]:
        return peek1d_finder(array, middle + 1, right);
    else:
        return array[middle]


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def find_max_position(array):
    max_position = 0
    temp_max = array[max_position]
    for i in range(1, len(array)):
        if array[i] > temp_max:
            temp_max = array[i]
            max_position = i

    return max_position


def peek2d_finder(matrix, top, bottom, j):
    mid = (top + bottom) // 2
    max_pos = find_max_position(matrix[mid])

    if matrix[mid][max_pos] < matrix[mid - 1][max_pos]:
        return peek2d_finder(matrix, 0, mid - 1, j)
    elif matrix[mid][max_pos] < matrix[mid + 1][max_pos]:
        return peek2d_finder(matrix, mid + 1, bottom, j)
    else:
        return matrix[mid][max_pos]


# Test 1D peek_finder
input = [5, 4, 3, 6, 1]
print(input)
print(peek1d_finder(input, 0, 5))
print("\n")

# Test 2D peek_finder
matrix = [[randint(10, 99) for i in range(5)] for j in range(8)]
print_matrix(matrix)
print("\n")
print(peek2d_finder(matrix, 1, 8, 5))
