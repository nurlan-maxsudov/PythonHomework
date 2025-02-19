def insert_underscores(txt):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []  
    count = 0    

    for i, char in enumerate(txt):
        result.append(char)  
        count += 1

    
        if count % 3 == 0 and i != len(txt) - 1: 
            if char.lower() in vowels or (i > 0 and txt[i - 1] == '_'):
                continue
            else:
                result.append('_')

    return ''.join(result) 

txt = "abcabcdabcdeabcdefabcdefg"
result = insert_underscores(txt)
print(result)