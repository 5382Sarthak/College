def rabin_karp(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    d = 256  # Number of characters in the input alphabet (ASCII)
    
    h = pow(d, m-1, prime)  # d^(m-1) % prime
    p_hash = 0  # Hash value for pattern
    t_hash = 0  # Hash value for text
    result = []

    # Calculate the hash value of the pattern and first window of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    # Slide the pattern over the text
    for i in range(n - m + 1):
        # If the hash values match, check the characters one by one
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        # Calculate hash for the next window
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime

    return result

def main():
    print("Rabin-Karp Pattern Matching")
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search: ")

    if len(pattern) > len(text):
        print("pattern is longer than the text.")
        return

    positions = rabin_karp(text, pattern)

    if positions:
        print(f"pattern found at index/indices: {positions}")
    else:
        print("pattern not found in the text.")

# Run the main function
if __name__ == "__main__":
    main()