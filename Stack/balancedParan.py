from stack import Stack

def checkParen(expression):
    stk = Stack()

    for char in expression:
        # print(char, end=' ')
        if char == '(':
            stk.push('(')
        elif char == ')':
            stk.pop()

    if stk.size() == 0:
        print("Expression is balanced")
    else:
        print("Expresssion is not balanced")


if __name__ == "__main__":

    exp_01 = '()'           # Balanced    
    exp_02 = '(()'          # Not Balanced
    exp_03 = '(()()()())'   # Balanced
    exp_04 = '(()()(()'     # Not Balanced

    list_of_expressions = [ exp_01, exp_02, exp_03, exp_04 ]

    for i in range(len(list_of_expressions)):
        checkParen(list_of_expressions[i])
