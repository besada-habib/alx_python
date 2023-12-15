def fibonacci_sequence(n):
    sequence = [0, 1]

    while len(sequence) < n:
        next_term = sequence[-1] + fib_sequence[-2]
        sequence.append(next_term)

    return sequence