# Inside here we are taking two numbers
def raise_to_power(base_num, pow_num):
    # assigning a variable result where we store the actual result
    result = 1
    # On For we are looping through the power num
    for index in range(pow_num):
    # result will calculate according to the power num
        result = result * base_num
    return result


print(raise_to_power(3, 4))