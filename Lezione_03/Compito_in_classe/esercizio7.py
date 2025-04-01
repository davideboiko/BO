"""""
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
For example:

Test	Result
print(check_parentheses("()()"))
True
print(check_parentheses("(()))("))
False

"""""


def check_parentheses(expression: str) -> bool:
    num ={}
    bo = "("
    bo1 = ")"
    for i in expression:
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    a = num.get(bo, 0)
    b = num.get(bo1, 0)
    if a == b:
        return True
    else:
        return False

print(check_parentheses("(()))("))
