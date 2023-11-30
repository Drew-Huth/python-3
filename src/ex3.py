import re


def create_files(file_name):
    count = 0
    biglist = []
    lillist = [] 
    with open(file_name , "r") as file:
        for line in file:
            new_string = re.sub(r'[^\w\s]', '', line)
            
            for word in new_string.split():
                if len(word) >=3 and word not in biglist :
                    biglist.append(word)
                elif len(word) <3 and word not in lillist :
                    lillist.append(word)
                else: 
                    continue
    
    with open("files\large-words.txt", "w") as large_output:
        for word in biglist:
            large_output.writelines(word + "\n")
            count += 1
                
    with open("files\small-words.txt", "w") as small_output:
        for word in lillist:
            small_output.writelines(word + "\n")
            count += 1
    return count
                
def ex3():
    total_words = create_files("files/words.txt")
    print(f"Total unique words: {total_words}.")

ex3()