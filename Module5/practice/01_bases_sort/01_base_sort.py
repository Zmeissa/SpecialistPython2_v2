nums = [5, 2, 1, 8, 4]
print("before sort = ", nums)
swapped = True
y=0
while swapped:
    swapped = False
    y+=1
    print("*****")
    for i in range(len(nums) - y):
        print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
print("after sort = ", nums)
