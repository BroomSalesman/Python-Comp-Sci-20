def arithmetic_arranger(problems, show_solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    pieced_problems = [i.split(" ") for i in problems]

    try:
        top_operands = [str(int(piece[0])) for piece in pieced_problems]
        bottom_operands = [str(int(piece[2])) for piece in pieced_problems]

    except ValueError:
        return "Error: Numbers must only contain digits."

    operators = [i[1] for i in pieced_problems]

    # This for loop makes a list of the answers by determining whether the problem is
    # addition or subtraction by looping throughthe math operators list.
    # After it determines the math operator to be used, it converts operands into integers, adds them
    # then converts the answer back into a string and appends it into the answers list.
    solutions = []

    for i in range(len(problems)):

        if operators[i] == "+":
            solutions.append(
                str(int(top_operands[i]) + int(bottom_operands[i])))

        elif operators[i] == "-":
            solutions.append(
                str(int(top_operands[i]) - int(bottom_operands[i])))

        else:
            return "Error: Operator must be '+' or '-'."

    first_operand_padding = []
    operator_with_operand_padding = []

    for problem in pieced_problems:
        longest_operand = ""

        for piece in problem:

            if len(piece) > 4:
                return "Error: Numbers cannot be more than four digits."

            if len(piece) > len(longest_operand) and piece not in "+-":
                longest_operand = piece

        first_operand_padding.append(2 + len(longest_operand))
        operator_with_operand_padding.append(1 + len(longest_operand))

    top_operand_formatted = []
    operator_with_operand_formatted = []
    seperators = []
    solutions_formatted = []
    for i in range(len(problems)):
        top_operand_formatted.append(top_operands[i].rjust(
            first_operand_padding[i]))
        operator_with_operand_formatted.append(
            operators[i] +
            bottom_operands[i].rjust(operator_with_operand_padding[i]))
        seperators.append("-" * len(operator_with_operand_formatted[i]))
        solutions_formatted.append(solutions[i].rjust(
            first_operand_padding[i]))

    # All the problems must be shown horizontally
    # so every top operand (top number) will be outputted
    # in the same line, every operator with the second operand will
    # appear in the same line, and so on. This can be outputted like that by
    # joining every row in each math problem in the same line.

    top_operands_line = (" " * 4).join(top_operand_formatted)
    operators_with_operands_line = (" " *
                                    4).join(operator_with_operand_formatted)
    seperators_line = (" " * 4).join(seperators) + "\n"
    solutions_line = (" " * 4).join(solutions_formatted)

    if show_solution:
        all_formatted = top_operands_line + "\n" + operators_with_operands_line + "\n" + seperators_line + solutions_line
    else:
        all_formatted = top_operands_line + "\n" + operators_with_operands_line + "\n" + seperators_line

    return all_formatted
