# function to capitalize every first letter of word in string 
def to_jaden_case(string):
    s1 = string.split()
    giga_words=[]
    for words in s1:
        flag = words.capitalize()
        giga_words.append(flag)

    final_string = " ".join(giga_words)
    return final_string