def main():
    path = "./books/frankenstein.txt"
    file_contents = get_book_text(path)
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    sorted_char_count = sort_dict(char_count)
    print_report(word_count, sorted_char_count, path)

def get_book_text(path):
    with open("./books/frankenstein.txt") as f:
        return f.read()

def count_words(doc):
    split_doc = doc.split()
    return len(split_doc)

def count_chars(doc):
    lower_doc = doc.lower()
    alphabet_count = {}
    for c in lower_doc:
        if c in alphabet_count and c.isalpha():
            alphabet_count[c] += 1
        elif c.isalpha():
            alphabet_count[c] = 1
    return alphabet_count

def print_report(word_count, sorted_char_count, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words in the document")
    print("")
    for dict in sorted_char_count:
        print(f"'{dict["char"]}' found {dict["count"]} times")
    print("--- End report ---")

def sort_dict(dict):
    list_of_dicts = []
    for key in dict:
        dict_to_add = {}
        dict_to_add["char"] = key
        dict_to_add["count"] = dict[key]
        list_of_dicts.append(dict_to_add)
    list_of_dicts.sort(reverse=True, key=sort_dict_on)
    print(f"list of dicts: {list_of_dicts}")
    return list_of_dicts

def sort_dict_on(dict):
    return dict["count"]


main()