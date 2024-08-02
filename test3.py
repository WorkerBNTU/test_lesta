def merge_sort(arr):
    # Базовый случай: если массив пустой или содержит один элемент, он считается отсортированным
    if len(arr) <= 1:
        return arr

    # Рекурсивно разбиваем массив на две части
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Объединяем две отсортированные части массива
    merged_arr = merge(left_half, right_half)

    return merged_arr


def merge(left, right):
    merged = []
    i = j = 0

    # Слияние двух отсортированных массивов в один
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из left, если они есть
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Добавляем оставшиеся элементы из right, если они есть
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged
