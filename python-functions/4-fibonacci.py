def fibonacci_sequence(n):
    sequence = [0, 1]
    if n <= 0:
        return [0]

    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence