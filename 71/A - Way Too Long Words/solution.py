import sys
 
def solve():
    # Read all lines from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # The first element is the number of words
    n = int(input_data[0])
    
    # Process each word
    for i in range(1, n + 1):
        word = input_data[i]
        length = len(word)
        
        if length > 10:
            # Abbreviate: First char + count of middle chars + last char
            abbreviation = word[0] + str(length - 2) + word[-1]
            print(abbreviation)
        else:
            # Keep it as it is
            print(word)
 
if __name__ == '__main__':
    solve()