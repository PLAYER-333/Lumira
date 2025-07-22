
import re

def interpret_lumira(code):
    variables = {}

    def evaluate(expr):
        expr = expr.strip()
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        elif '.' in expr:
            try:
                return float(expr)
            except:
                return expr
        elif expr.startswith("'") and expr.endswith("'"):
            try:
                return int(expr[1:-1])
            except:
                return expr
        elif expr in variables:
            return variables[expr]
        return expr

    def parse_line(line):
        if line.strip().startswith("~!"):
            return

        if line.startswith("let "):
            parts = line[4:].split("=", 1)
            var = parts[0].strip()
            val = parts[1].strip()
            variables[var] = evaluate(val)

        elif line.startswith("printos("):
            inner = line[len("printos("):-1]
            if '+' in inner:
                parts = [evaluate(p.strip()) for p in inner.split('+')]
            else:
                parts = [evaluate(p.strip()) for p in inner.split(',')]
            print(" ".join(str(p) for p in parts))

        elif line.startswith("inscan()"):
            return input("> ")

        elif line.startswith("defn "):
            print("~! Function definition support coming in v0.3")

        elif line.startswith("if "):
            print("~! Conditional support coming in v0.3")

        elif line.startswith("foros "):
            print("~! Loop support coming in v0.3")

        else:
            print(f"Unknown syntax: {line}")

    lines = code.strip().split("\n")
    for line in lines:
        parse_line(line)

# Example usage
sample_code = """
~! Lumira v0.2 demo
let name = "Lumira"
let version = '2'
printos("Welcome to", name)
printos("Version: " + version)
"""

interpret_lumira(sample_code)
