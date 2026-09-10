import ast
import operator
import re


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


def evaluate(node):

    if isinstance(node, ast.Constant):

        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Invalid number")


    if isinstance(node, ast.BinOp):

        left = evaluate(node.left)
        right = evaluate(node.right)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator")

        return operation(left, right)


    if isinstance(node, ast.UnaryOp):

        if isinstance(node.op, ast.USub):
            return -evaluate(node.operand)

        raise ValueError("Unsupported operator")


    raise ValueError("Invalid expression")


def calculate(expression):

    try:

        tree = ast.parse(
            expression,
            mode="eval"
        )

        return evaluate(tree.body)

    except:

        return None


def natural_calculation(query):

    query = query.lower().strip()


    # ---------------------------------------
    # PERCENTAGE
    # ---------------------------------------

    percentage_match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:percent|%)\s*(?:of|ka)\s*(\d+(?:\.\d+)?)",
        query
    )

    if percentage_match:

        percentage = float(
            percentage_match.group(1)
        )

        number = float(
            percentage_match.group(2)
        )

        result = (percentage / 100) * number

        return result


    # ---------------------------------------
    # "800 ka 25 percent"
    # ---------------------------------------

    percentage_match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:ka)\s*(\d+(?:\.\d+)?)\s*(?:percent|%)",
        query
    )

    if percentage_match:

        number = float(
            percentage_match.group(1)
        )

        percentage = float(
            percentage_match.group(2)
        )

        result = (percentage / 100) * number

        return result


    # ---------------------------------------
    # NORMAL MATH
    # ---------------------------------------

    expression = query

    expression = expression.replace(
        "what is",
        ""
    )

    expression = expression.replace(
        "calculate",
        ""
    )

    expression = expression.replace(
        "please",
        ""
    )

    expression = expression.strip()


    # Words → operators

    expression = expression.replace(
        "plus",
        "+"
    )

    expression = expression.replace(
        "minus",
        "-"
    )

    expression = expression.replace(
        "times",
        "*"
    )

    expression = expression.replace(
        "multiplied by",
        "*"
    )

    expression = expression.replace(
        "divided by",
        "/"
    )

    expression = expression.replace(
        "divide by",
        "/"
    )


    # Only allow safe mathematical characters

    if not re.fullmatch(
        r"[0-9+\-*/().%\s]+",
        expression
    ):

        return None


    return calculate(expression)