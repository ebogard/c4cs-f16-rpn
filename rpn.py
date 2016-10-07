#!/usr/bin/env python3

def add(a, b):
	return a + b
def subtract(a, b):
	return a - b
def multiply(a, b):
	return a * b
def divide(a, b):
	return a / b

operators = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide
}

def calculate(myarg1):
	stack = list()
	for token in myarg1.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			art1 = stack.pop()
			function = operators[token]
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError
	return stack.pop()


def main():
	while True:
		calculate(input("rpn calc> "))


if __name__ == '__main__':
	main()
