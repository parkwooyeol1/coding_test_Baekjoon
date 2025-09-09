word = input().strip()
count = 0
alpha_table = {
    'c': ['c=','c-'],
    'd': ['dz=','d-'],
    'l': ['lj'],
    'n': ['nj'],
    's': ['s='],
    'z': ['z=']
}
con_ = 0
for i in range (len(word)):
    if con_ != 0:
        con_ -=1
        continue
    if word[i] in list(alpha_table.keys()):
        current = word[i]
        for j in word[i+1:]:
            con_+= 1
            current += j
            if current in alpha_table[word[i]]:
                count += 1
                break
            elif con_ == len(word[i+1:]):  
                con_ = 0 
                count += 1
        if word[i] in list(alpha_table.keys()) and i == len(word)-1:
            count +=1
    else:
        count +=1
print(count)