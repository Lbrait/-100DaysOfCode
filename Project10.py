def line(tam=42):
    return '-' * tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def sum(n1, n2):
    return n1 + n2


def subs(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


op = {'+': sum, '-': subs, '*': mult, '/': div}
header('\033[1;34mCALCULATOR\033[m')


def calc():
    num1 = int(input('Whats the first number?: '))
    for sym in op:
        print(sym)
    sc = True

    while sc:
        op_sym = input('Pick an operation: ')
        num2 = int(input('Whats the next number?: '))
        cf = op[op_sym]
        ans = cf(num1, num2)

        print('\033[32m' if num1 >= 0 else '\033[31m', num1, '\033[m', op_sym,'\033[32m' if num2 >= 0 else '\033[31m', num2, '\033[m', '=', '\033[32m' if ans >= 0 else '\033[31m', ans, '\033[m')

        r = input(f'Type "y" to continue calculating  with {ans}, or type "n" to start a new calculation: ').lower()[0]
        if r == 'y':
            num1 = ans
        else:
            sc = False
            calc()


calc()
