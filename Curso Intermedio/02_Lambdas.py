# Lambdas

# LAs lambdas son como funciones con la peculiaridad de que son anonimas, es decir, que no tienen nombre.

sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(5, 6))

multiply_values = lambda first_value, second_value: first_value * second_value

print(multiply_values(5, 6))

def sum_three_values(first_value):
    return sum_two_values
print(sum_three_values(5)(2,4))

