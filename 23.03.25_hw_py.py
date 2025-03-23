def sum_even_squares(numbers):
    def square(x):
        return x ** 2

    total = sum(square(num) for num in numbers if num % 2 == 0)
    return total

my_list = [1, 2, 3, 4, 5, 6]
result = sum_even_squares(my_list)
print(result)
