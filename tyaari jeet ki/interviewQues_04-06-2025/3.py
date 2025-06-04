def StringChallenge(strParam):
    arr = [0] * 26

    # count alphabets
    for char in strParam:
        arr[ord(char) - ord('a')] += 1
    
    strParam = ""
    for i in range(26):
        if arr[i] > 0:
            strParam += chr(i + ord('a')) * arr[i]

    return strParam

print(StringChallenge("coderbyte"))