#def arithmetic_arranger(problems):
def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    pieced_problems = [i.split(" ") for i in problems]

    try:
        first_operands = [i[0] for i in pieced_problems]
        last_operands = [(i[2]) for i in pieced_problems]

    except ValueError:
        return "Error: Numbers must only contain digits."

    operators = [i[1] for i in pieced_problems]

    for operator in operators:
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."

    longest_operand = ""
    for problem in pieced_problems:
        for piece in problem:
            if len(piece) > len(longest_operand) and piece not in "+-":
                longest_operand = piece

    return longest_operand

    return arranged_problems


print(arithmetic_arranger(["32 + 698"]))

    #return arranged_problems


