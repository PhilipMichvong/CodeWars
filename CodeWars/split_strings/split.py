# function to split string after every 2 letters
def split(s : str):
    
    if len(s)%2 != 0: 
        s+="_"
# my own assumption, 
# if there is a number in the string, i replace it with _
    for num in s:
        if num.isdigit():
            s = s.replace(num, "_")
    
    splited = [s[i:i+2] for i in range(0,len(s),2)]

    return splited