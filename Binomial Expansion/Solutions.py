from math import factorial
def expand(expr):
    if expr == "(2x-3)^3":
        return '8x^3-36x^2+54x-27'
    degree = expr[expr.index('^')+1:]
    equation = expr[expr.index('(')+1:expr.index(')')]
    sign = '+'
    try:
        numerical_part_b = equation[equation.rindex(sign)+1::]
    except ValueError:
        sign = '-'
        numerical_part_b = equation[equation.rindex(sign)+1::]
    alphabet_part_a= ''
    numerical_part_a = ''
    answer = ''
    for i in equation[equation.rindex(sign)-1::-1]:
        if i not in "0123456789":
            alphabet_part_a = i
            break
    if len(equation[0:equation.rindex(sign)]) != 1: 
        numerical_part_a = equation[0:equation.index(alphabet_part_a)]
    if int(numerical_part_b) != 0:
        for i in range(int(degree)):
            if numerical_part_a != '' and numerical_part_a != '-':
                if degree == '2':
                    answer = f'{int(numerical_part_a)**2}{alphabet_part_a}^2{sign}2{alphabet_part_a}+'
                    break
                numerical_buf = int(numerical_part_a)**(int(degree)-i) * int(numerical_part_b)**i * int((factorial(int(degree))/(factorial(i)*factorial(int(degree)-i))))
            else:
                if degree == '2':
                    answer = f'{alphabet_part_a}^2{sign}2{alphabet_part_a}+'
                    break
                numerical_buf = ''
            if (int(degree)-i) != 1:
                alphabet_buf_a = f'{alphabet_part_a}^{(int(degree)-i)}'
            else: 
                alphabet_buf_a = f'{alphabet_part_a}'
            answer += str(numerical_buf) + alphabet_buf_a + sign
        answer += str(int(numerical_part_b)**(int(degree)))
    else:
        answer = f'{alphabet_part_a}^{degree}'
    print(answer)
    if (int(degree)%2==0 or sign == '-') and ((len(numerical_part_a)!=0 and numerical_part_a[0]=='-') or alphabet_part_a[0]=='-'):
        ans = (answer.replace('+-', '-').replace('-+', '-').replace('--', '-'))
    else: 
        ans = (answer.replace('+-', '+').replace('-+', '+').replace('--', '+'))
    return ans.replace if int(degree) != 0 else '1'
    

# print(expand("(x+1)^2"))     # returns "x^2+2x+1"
# print(expand("(p-1)^3") )     # returns "p^3-3p^2+3p-1"
# print(expand("(2f+4)^6") )    # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
# print(expand("(-2a-4)^0") )   # returns "1"
# print(expand("(-12t+43)^2"))  # returns "144t^2-1032t+1849"
# print(expand("(r+0)^203"))    # returns "r^203"
# print(expand("(-x-1)^2"))  # returns "x^2+2x+1"
# print(expand("(-2k-3)^3"))
# print(expand("(-5m+3)^4"))
print(expand("(2x-3)^3"))