def count_numbers(sorted_list, less_than):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] < less_than:
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) 
