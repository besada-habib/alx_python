def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)
    
    # Return a tuple with the length and the first character of the sentence
    return (len(sentence), sentence[0])

# Example usage:
sentence1 = "Hello, World!"
result1 = multiple_returns(sentence1)
print(result1)  # Output: (13, 'H')

sentence2 = ""
result2 = multiple_returns(sentence2)
print(result2)  # Output: (0, None)
