def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        Number_of_words(file_contents)

def Number_of_words(file_contents):
    # Split into words
    words = file_contents.split()

    # Count the number of words
    word_count = len(words)
    print(word_count)
def Charactor_count(file_contents):
    lowered= file_contents.lower()
    



main()
