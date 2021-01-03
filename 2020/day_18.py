from data import load_day


def tokenize(exp):
    return [char for char in exp if char != ' ']


def convert_to_postfix(infix_exp, precedence):
    postfix = []
    op_stack = []
    for token in infix_exp:
        if token.isnumeric():
            postfix.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            top_op = op_stack.pop()
            while top_op != '(':
                postfix.append(top_op)
                top_op = op_stack.pop()
        else:
            while op_stack and not precedence[token] > precedence[op_stack[-1]]:
                postfix.append(op_stack.pop())
            op_stack.append(token)

    while op_stack:
        postfix.append(op_stack.pop())

    return postfix


def calculate(postfix_exp):
    result = []
    for token in postfix_exp:
        if token.isnumeric():
            result.append(token)
        else:
            a = int(result.pop())
            b = int(result.pop())
            c = a * b if token == '*' else a + b
            result.append(c)

    return result.pop()


data = load_day(18)
results_1, results_2 = [], []
for infix_exp in data:
    tokenized_infix_exp = tokenize(infix_exp)
    # part 1 - addition and multiplication have the same presedence
    precedence_1 = {'(': 0, '*': 1, '+': 1}
    postfix_exp_1 = convert_to_postfix(tokenized_infix_exp, precedence=precedence_1)
    results_1.append(calculate(postfix_exp_1))
    # part 2 - addition is evaluated before multiplication
    precedence_2 = {'(': 0, '*': 1, '+': 2}
    postfix_exp_2 = convert_to_postfix(tokenized_infix_exp, precedence=precedence_2)
    results_2.append(calculate(postfix_exp_2))


print(sum(results_1))
print(sum(results_2))