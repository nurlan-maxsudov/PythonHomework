
import re

file_path = "lesson-6\homework\sample.txt"

def count_words():
    with open("lesson-6\homework\sample.txt", "r") as file:
        content = file.read()
        print(content)

    content = re.sub(r'[.,]', '', content)
    words = content.split()
    # print(words)

    encountered_words = {}

    for word in words:
        if word.lower() not in encountered_words.keys():
            encountered_words[word.lower()] = 1
        else:
            encountered_words[word.lower()] += 1

    sorted_dict = dict(sorted(encountered_words.items(), key=lambda item: item[1], reverse=True))

    top_5_words = list(sorted_dict.items())[:5]

    top_words = f"Total words: {len(words)}\n"
    for key, value in dict(top_5_words).items():
        top_words += f"{key} - {value}\n"

    with open("lesson-6\homework\word_count_report.txt", "w") as file:
            file.write("Word Count Report\n" + top_words)

try:
    count_words()
except FileNotFoundError:
        text = input("Please, write something: ")
        with open(file_path, "w") as file:
            file.write(text)
        count_words()
