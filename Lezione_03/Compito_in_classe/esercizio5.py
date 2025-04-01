
def rotate_left(elements: list, k: int) -> list:
    if k > 5:
        k -= 5
    
    return elements[k:] + elements[:k]  

print(rotate_left([1, 2, 3, 4, 5], 2))

"""""


def F1(t, F1):
    r = []
    for c in t:
        if c.isalpha():
            o = ord('A') if c.isupper() else ord('a')
            r.append(chr((ord(c) - o + F1) % 26 + o))
        else:
            r.append(c)
    return ''.join(r)
print(F1("ciaocomestai", 3))

"""""
