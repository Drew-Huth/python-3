import re


def create_files(file_name):
    count = 0
    biglist = []
    lillist = [] 
    bigwords = open("files\large-words.txt", "w")
    smallwords = open("files\small-words.txt", "w")
    wordstxt = open("files/words.txt", "r")
    
    with wordstxt as file_input:
        for line in file_input:
            new_string = re.sub(r'[^\w\s]', '', line)
            for word in new_string.split():
                if len(word) >=3 and word not in biglist :
                    biglist.append(word)
                elif len(word) <3 and word not in lillist :
                    lillist.append(word)
                else: 
                    continue
    
    with bigwords as large_output:
        for word in biglist:
            large_output.writelines(word + "\n")
            count += 1
                
    with smallwords as small_output:
        for word in lillist:
            small_output.writelines(word + "\n")
            count += 1
    return count
                
def ex3():
    total_words = create_files("words.txt")
    print(f"Total unique words: {total_words}.")

ex3()