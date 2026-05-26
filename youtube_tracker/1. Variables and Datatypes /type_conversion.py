num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
num_bool = bool(num_str)
sum = num_int + num_float
print(sum, type(sum), sep="-")
print(num_bool, type(num_bool))

# Type convert always convert to lower
a = int(100.9)
b = int(100.1)
print(a, b)
