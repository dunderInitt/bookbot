def main():
    words = []
    book = "books/frankenstein.txt"
    with open(book) as f:
        content = f.read()
        
    words = content.split()
    chars_dict = count_char_in_string(content)
    print(f"--- Begin of report of {book}---")
    print("There are " + str(len(words)) + " words in this book")
    print("\n")
    create_character_report(chars_dict)
    print("--- End Report ---")

def count_char_in_string(text):
    characters_with_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in characters_with_count:
            characters_with_count[char] += 1
        else:
            characters_with_count[char] = 1
    return characters_with_count
    
    
def create_character_report(data):
    data_list = []
    for item in data:
        character_and_count = {}
        if item.isalpha():
            character_and_count["character"] = item
            character_and_count["count"] = data[item]
            data_list.append(character_and_count)

        
    data_list.sort(reverse=True, key=sort_on)
    for data in data_list:
        print(f"The {data["character"]} character was found {data["count"]} times")
        
    
def sort_on(dict):
    return dict["count"]


    
    
    
    
    
    
    
main()

