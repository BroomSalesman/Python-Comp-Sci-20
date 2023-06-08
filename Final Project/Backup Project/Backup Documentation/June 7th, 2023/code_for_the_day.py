def arithmetic_arranger(problems):
  if len(problems)
  pieced_problems = [i.split(" ") for i in problems]

  first_numbers = [i[0] for i in pieced_problems]
  try:
    operators = [int(i[1]) for i in pieced_problems]
  except ValueError:
    return "Error: Numbers must only contain digits."

  last_numbers = [i[2] for i in pieced_problems]



  return arranged_problems
