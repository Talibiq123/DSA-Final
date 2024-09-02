import math

base = 2
exponent = 3
result = base ** exponent
print(f"{base} to the power of {exponent} is: {result}")

result = pow(base, exponent)
print(f"{base} to the power of {exponent} using pow() is: {result}")


result = math.pow(base, exponent)
print(f"{base} to the power of {exponent} using math.pow() is: {result}")
