directory = "books/frankenstein.txt"
def main():
    with open(directory) as f:
        file_contents = f.read()
        return file_contents
text = main()
def count(text):
    words = text.split()
    number = len(words)
    return number

lower_case_text = text.lower()
number_of_characters = {}
def character_numbers(lower_case_text):
    for char in lower_case_text:
        if char not in number_of_characters:
            number_of_characters[char] = 1
        else:
            number_of_characters[char] += 1
    
    return number_of_characters
def sort_on(dict):
    return dict["num"]
def sort(number_of_characters):
    char_list = []
    for char, num in number_of_characters.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True,key=sort_on)
    return char_list
count(text)
sort(number_of_characters)
print(f"--- Begin report of {directory} ---")
print(f"{count(text)} words found in the document\n")
sorted_chars = sort(character_numbers(lower_case_text)) 
for number_of_characters in sorted_chars:
    print(f"The character '{number_of_characters['char']}' was found {number_of_characters['num']} times")
print("--- End report ---")