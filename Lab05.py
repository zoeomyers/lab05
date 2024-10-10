ip_str = input("Please enter IP Address: ") #192.168.1.10
def is_valid_part(part_str):
    try:
        part_int = int(part_str)
        if part_str[0] == '0' and part_int != 0:
            return False
        if 0 < part_int <= 255: #returns False for 0 and 255
            return True
        return False
    except ValueError:
        print("Invalid part detected.")
        return False
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

def binary_to_decimal(b):
    len_b = len(b)
    if len_b == 1:
        return int(b)
    return 2 ** (len_b - 1) * int(b[0]) + binary_to_decimal(b[1:])

