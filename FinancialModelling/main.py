import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = (
    'NUMBER', 'NAME',
)

literals = ['=', '+', '-', '*', '/', '(', ')']

# 变量名规则
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

# 数字规则
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # 将字符串转换为整数
    return t

# 忽略空格和制表符
t_ignore = " \t"

# 换行处理
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# 错误处理
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# 构建lexer
lexer = lex.lex()

# 优先级和结合性
precedence = (
    ('left', '+', '-'),    # 加法和减法
    ('left', '*', '/'),    # 乘法和除法
    ('right', 'UMINUS'),   # 一元减法（负号）
)

# 语法规则

def p_statement_expr(t):
    'statement : expression'
    print(t[1])  # 输出表达式结果

def p_expression_binop(t):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

def p_expression_group(t):
    'expression : "(" expression ")"'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    t[0] = t[1]

def p_expression_uminus(t):
    'expression : "-" expression %prec UMINUS'
    t[0] = -t[2]

# 错误处理规则
def p_error(t):
    if t:
        print(f"Syntax error at '{t.value}'")
    else:
        print("Syntax error at EOF")

# 构建解析器
parser = yacc.yacc()

# 测试输入
expression = "2 + 3 * 4 + 4 / 2"

# 执行词法分析
lexer.input(expression)

# 输出词法分析结果
for tok in lexer:
    print(tok)

# 执行语法分析并输出计算结果
result = parser.parse(expression)

