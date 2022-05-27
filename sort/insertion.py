from icecream import ic


def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert
    return nums


if __name__ == "__main__":
    ic(insertion_sort([15, 1, 10, 20, 4]))
    ic(insertion_sort([2, 18, 0, 12, 9]))
    ic(insertion_sort([6, 6, 10, 16, 6]))
    ic(insertion_sort([1, 16, 9, 4, 1]))
    ic(insertion_sort([6, 3, 12, 9, 8]))
    ic(insertion_sort([7, 17, 16, 12, 9]))
