def generate_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    fib_sequence = []

    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    print(f"Fibonacci sequence with {n} terms:")
    print(fib_sequence)

try:
    terms = int(input("Enter the number of terms: "))
    generate_fibonacci(terms)
except ValueError:
    print("Invalid input. Please enter an integer.")