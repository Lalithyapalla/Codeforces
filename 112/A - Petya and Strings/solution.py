import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    string1 = input_data[0]
    string2 = input_data[1]
    str1_lowercase = string1.lower()
    str2_lowercase = string2.lower()
    if str1_lowercase < str2_lowercase:
        print("-1")
    elif str1_lowercase > str2_lowercase:
        print("1")
    else:
        print("0")
 
if __name__ == '__main__':
    solve()