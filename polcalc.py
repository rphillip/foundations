
def add(a,b):
 return a + b
def sub(a,b):
 return a - b
def mult(a,b):
 return a * b
def div(a,b):
 return a / b

symbols = { '+': add(a,b),"-": sub(a,b),"*": mult(a,b),"/": div(a,b)
}



def calc(equation):
  parts = equation.split()
  value = []

  for x in parts:
    if x in symbols:
      b = stack.pop()
      a = stack.pop()
      result = symbols[x](a, b)
      stack.append(result)
    else:
      stack.append(x)

  return stack.pop()

equation = input("Enter equation with spaces")
print(calc(equation))
