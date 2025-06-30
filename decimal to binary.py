def decimal_to_binary(decimal_num):
    binary_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    return binary_num
decimal_number = 13
binary_result = decimal_to_binary(decimal_number)
print(f"Decimal: {decimal_number} -> Binary: {binary_result}")
