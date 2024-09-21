def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        #Number_of_words(file_contents)
        char_counts = character_count(file_contents)
        #print(char_counts)
        Sorting_function(char_counts)
           
def Number_of_words(file_contents):
    # Split into words
    words = file_contents.split()
    # Count the number of words
    word_count = len(words)
    print(f"Number of words: {word_count}")

def character_count(file_contents):
    lowered = file_contents.lower()
    char_counts = {}

    for c in lowered:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
            
    return char_counts

def Sorting_function(char_counts):
    # Filter for alphabetical characters and create a list of tuples
    filtered_chars = [(c, count) for c, count in char_counts.items() if c.isalpha()]

    # Sort the list of tuples based on count
    sorted_char_counts = sorted(filtered_chars, key=lambda item: item[1], reverse=True)

    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    
    print("---End Report---")
main()
