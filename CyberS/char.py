ascii_values = [102, 108, 97, 103, 123, 99, 53, 118, 95, 104, 49, 100, 100, 51, 110, 125]
decoded_text = ''.join(chr(value) for value in ascii_values)
print(decoded_text)