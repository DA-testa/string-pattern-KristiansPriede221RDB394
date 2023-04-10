# python3

path="C:/Users/Kristians/Desktop/pitons_vs/string-pattern-KristiansPriede221RDB394/tests/06"
check=input()
if check.startswith('I'):
    pattern=input()
    text=input()
elif check.startswith('F'):
    ptf=path
    with open(ptf,'r')as file:
        lines=file.read()
        line=lines.split("\n",2)
        pattern=line[0] 
        text=line[1]

def get_occurrences(pattern, text):
    pat_len=len(pattern)
    txt_len=len(text)
    prime_num=5407
    a=26
    output=[]
    pat_hash=0
    txt_hash=0
    h=1
    i=0
    j=0
    for i in range(pat_len-1):
        h=(h*a)%prime_num
    for i in range(pat_len):
        pat_hash=(a*pat_hash+ord(pattern[i]))%prime_num
        txt_hash=(a*txt_hash+ord(text[i]))%prime_num
    for i in range(txt_len-pat_len+1):
        if(pat_hash==txt_hash):
            for j in range(pat_len):
                if(text[i+j]!=pattern[j]):
                    break
                else:
                    j+=1
            if(j==pat_len):
                output.append(i)
        if(txt_len-pat_len>i):
            txt_hash=(a*(txt_hash-ord(text[i])*h)+ord(text[i+pat_len]))%prime_num
            if (txt_hash<0):
                txt_hash=txt_hash+prime_num
    return output                      


# this part launches the functions
if __name__ == '__main__':
    print(get_occurrences(pattern, text))
