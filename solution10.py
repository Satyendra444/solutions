def find_two_sum(numbers, target_sum):
    seen = {}
    pairs = []
    for i, num in enumerate(numbers):
        if target_sum - num in seen:
            pairs.append((seen[target_sum - num], i))
        seen[num] = i
    return pairs

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))

