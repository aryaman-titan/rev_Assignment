def singlechar_xor(input_bytes, key_value):
    output = b''
    for char in input_bytes:
        output += bytes([char ^ key_value])
    return output
print(singlechar_xor('aaaabbbb', ord('@')))
