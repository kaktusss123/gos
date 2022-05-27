from icecream import ic


def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums


if __name__ == "__main__":
    ic(selection_sort([15, 1, 10, 20, 4]))
    ic(selection_sort([2, 18, 0, 12, 9]))
    ic(selection_sort([6, 6, 10, 16, 6]))
    ic(selection_sort([1, 16, 9, 4, 1]))
    ic(selection_sort([6, 3, 12, 9, 8]))
    ic(selection_sort([7, 17, 16, 12, 9]))
