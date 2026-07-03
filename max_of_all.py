def max_of_all():
    values = list(
        map(int, input("Enter a list of numbers separated by space: ").split()))
    return max(values)


print(max_of_all())
