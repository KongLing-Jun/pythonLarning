from ply import lex, yacc

# 词法分析部分
tokens = (
    'ID', 'NUMBER', 'STRING',
    'INT', 'VOID', 'CHAR', 'RETURN',
    'IF', 'ELSE', 'WHILE', 'FOR',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    'AND', 'OR', 'NOT',
    'ASSIGN',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA'
)

# 保留字
reserved = {
    'int': 'INT',
    'void': 'VOID',
    'char': 'CHAR',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
}

# 词法规则
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','


def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)


# 语法分析部分

# 优先级和结合性
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    ('left', 'AND', 'OR'),
    ('right', 'NOT'),
)


# 语法规则
def p_program(p):
    '''program : fun_decl'''
    print("program")
    p[1]  # 解析的函数声明会调用其中的打印


def p_fun_decl(p):
    '''fun_decl : type ID LPAREN param_list RPAREN compound_stmt'''
    print("    fun_decl")
    print(f"        {p[1]}")  # 打印函数返回类型
    print(f"        {p[2]}")  # 打印函数名
    p[4]  # 输出参数列表
    p[5]  # 输出复合语句


def p_param_list(p):
    '''param_list : type ID
                  | param_list COMMA type ID
                  | VOID'''
    if len(p) == 3 and p[1] == 'void':
        return  # 空参数列表，void
    elif len(p) == 3:
        print(f"        {p[1]}")
        print(f"        {p[2]}")
    elif len(p) == 5:
        print(f"        {p[3]}")
        print(f"        {p[4]}")
        p[1]  # 递归输出参数列表


def p_type(p):
    '''type : INT
            | VOID
            | CHAR'''
    p[0] = p[1]  # 设置类型


def p_compound_stmt(p):
    '''compound_stmt : LBRACE stmt_list RBRACE'''
    print("        compound_stmt")
    p[2]  # 输出语句列表


def p_stmt_list(p):
    '''stmt_list : stmt
                 | stmt stmt_list'''
    p[0] = p[1]
    if len(p) == 3:
        p[2]


def p_stmt(p):
    '''stmt : expr_stmt
           | if_stmt
           | return_stmt
           | var_decl'''
    p[0] = p[1]


def p_expr_stmt(p):
    '''expr_stmt : expr SEMI'''
    print("            expr_stmt")
    p[1]  # 输出表达式


def p_if_stmt(p):
    '''if_stmt : IF LPAREN expr RPAREN compound_stmt
               | IF LPAREN expr RPAREN compound_stmt ELSE compound_stmt'''
    print("            if_stmt")
    p[3]  # 输出表达式
    p[5]  # 输出复合语句
    if len(p) == 8:
        p[7]  # 输出else的复合语句


def p_return_stmt(p):
    '''return_stmt : RETURN expr SEMI'''
    print("            return_stmt")
    p[2]  # 输出返回的表达式


def p_var_decl(p):
    '''var_decl : type ID SEMI'''
    print("            var_decl")
    print(f"                {p[1]}")
    print(f"                {p[2]}")


def p_expr(p):
    '''expr : var ASSIGN expr
            | var
            | NUMBER
            | expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr MODULO expr
            | expr LT expr
            | expr LE expr
            | expr GT expr
            | expr GE expr
            | expr EQ expr
            | expr NE expr
            | expr AND expr
            | expr OR expr
            | NOT expr
            | LPAREN expr RPAREN'''

    # 处理赋值语句
    if len(p) == 4 and p[2] == '=':
        print("            assign")
        print("                var")
        print(f"                    {p[1]}")
        print(f"                    {p[3]}")

    # 处理数字
    elif len(p) == 2 and isinstance(p[1], int):
        print(f"                {p[1]}")

    # 处理变量
    elif len(p) == 2:
        print(f"                var\n                    {p[1]}")

    # 处理二元运算符
    else:
        print("            binop")
        print(f"                {p[2]}")
        print(f"                {p[1]}")
        print(f"                {p[3]}")

def p_var(p):
    '''var : ID'''
    p[0] = p[1]  # 变量就是其标识符

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# 构建词法分析器和语法分析器
lexer = lex.lex()
parser = yacc.yacc()

# 输入示例
input_data = '''
int main(void) {
    int x;
    x = 5;
    if (x > 0) {
        return x;
    }
    return 0;
}
'''
# 执行语法分析
parser.parse(input_data)
