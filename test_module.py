from mean_var_std import calculate

input_list = [2, 6, 2, 8, 4, 0, 1, 5, 7]

try:
    result = calculate(input_list)
    print("Calculation Results:")
    print(result)
except ValueError as e:
    print(e)
