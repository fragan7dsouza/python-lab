def binary_to_decimal(binary_num):
    decimal_num = 0
    binary_num = str(binary_num)
    for i in range(len(binary_num) - 1, -1, -1):
        decimal_num += int(binary_num[i]) * (2 ** (len(binary_num) - 1 - i))
    return decimal_num
binary_number = '1101'
decimal_result = binary_to_decimal(binary_number)
print(f"Binary: {binary_number} -> Decimal: {decimal_result}")
