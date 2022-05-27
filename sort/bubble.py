from icecream import ic


def bubble_sort(nums: list[int]) -> list[int]:
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return nums


if __name__ == "__main__":
    ic(bubble_sort([15, 1, 10, 20, 4]))
    ic(bubble_sort([2, 18, 0, 12, 9]))
    ic(bubble_sort([6, 6, 10, 16, 6]))
    ic(bubble_sort([1, 16, 9, 4, 1]))
    ic(bubble_sort([6, 3, 12, 9, 8]))
    ic(bubble_sort([7, 17, 16, 12, 9]))
