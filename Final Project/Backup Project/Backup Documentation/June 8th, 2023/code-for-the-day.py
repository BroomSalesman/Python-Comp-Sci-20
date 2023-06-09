def arithmetic_arranger(problems, show_solution = False):
  if len(problems) > 5:
    return "Error: Too many problems."

  pieced_problems = [i.split(" ") for i in problems]

  try:
    first_operands = [i[0] for i in pieced_problems]
    last_operands = [(i[2]) for i in pieced_problems]

  except ValueError:
    return "Error: Numbers must only contain digits."

  operators = [i[1] for i in pieced_problems]

  answers = []

  for operator in range  (len(operators)):
    if operator not in "+-":
      return "Error: Operator must be '+' or '-'."
    if operator == "+":
      answers.append(str(first_opernads))
    

  longest_operand = ""
  for problem in pieced_problems:
    for piece in problem:
      if piece 
      if len(piece) > len(longest_operand) and piece != {"+", "-"}:
        longest_operand = piece
  return longest_operand

  return arranged_problems