def is_palindrome(input_str):
    # remove spaces and convert string to lowercase
    cleaned_str = input_str.replace(" ", "").lower()

    # compare the cleaned string with its reversed version
    # uses slicing to step backwards and check if the string is the same backwards as it is forwards
    return cleaned_str == cleaned_str[::-1]

def main():
    word = input("Enter a word or phrase: ")
    if is_palindrome(word):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
    
if __name__ == "__main__":
    main()