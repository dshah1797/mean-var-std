from mean_var_std import calculate

try:
    calculate([1, 2, 3])  
except ValueError as e:
    print("Test Passed:", e)


print(calculate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
