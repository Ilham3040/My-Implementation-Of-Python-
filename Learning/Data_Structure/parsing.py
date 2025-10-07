import operator

def tokenize_simple(expr: str):
    allowed_ops = set("+-*/")
    tokens = []
    num_buf = []
    def flush_number_buf():
        if not num_buf:
            return
        s = ''.join(num_buf)
        if not any(ch.isdigit() for ch in s):
            raise ValueError(f"Invalid number token: {s!r}")
        val = float(s) if '.' in s else int(s)
        tokens.append(val)
        num_buf.clear()
    i = 0
    n = len(expr)
    while i < n:
        ch = expr[i]
        if ch.isspace():
            flush_number_buf(); i += 1; continue
        if ch.isdigit() or ch == '.':
            num_buf.append(ch); i += 1; continue
        if ch in allowed_ops:
            flush_number_buf()
            tokens.append(ch)
            i += 1
            continue
        raise ValueError(f"Invalid character at position {i}: {ch!r}")
    flush_number_buf()
    return tokens

def opps(line: str):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    tokens = tokenize_simple(line)
    if not tokens:
        raise ValueError("Empty expression")
    if len(tokens) % 2 == 0:
        raise ValueError("Malformed expression: expected number operator number ...")
    total = tokens[0]
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        if op not in ops:
            raise ValueError(f"Unsupported operator: {op!r}")
        operand = tokens[i + 1]
        if op == '/' and operand == 0:
            raise ZeroDivisionError("Division by zero")
        total = ops[op](total, operand)
    print(total)

# Example
opps(" 12.5 * 2.0 / .5 ")
