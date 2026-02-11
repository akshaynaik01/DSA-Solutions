# Stack implementation using array (list)

MAX_SIZE = 5
stack = []

# Push operation
def push(element):
    if len(stack) == MAX_SIZE:
        print("Stack Overflow")
    else:
        stack.append(element)
        print(f"{element} pushed into stack")

# Pop operation
def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print(f"{stack.pop()} popped from stack")

# Peek operation
def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

# Display stack elements
def display():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack elements (top to bottom):")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

# Driver code
push(10)
push(20)
push(30)
display()
peek()
pop()
display()
