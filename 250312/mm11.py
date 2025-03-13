numbers = list(map(int, input().split()))
odd_index_numbers = numbers[::2]

max_value = max(odd_index_numbers)
min_value = min(odd_index_numbers)
average_value = sum(odd_index_numbers) / len(odd_index_numbers)

print(f"{min_value} {max_value} {average_value:.2f}")
