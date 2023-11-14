units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def numtolist(num):
    numlist = [0,0,0,0,0,0,0,0,0]
    numlist[0] = (num//100000000)%10
    numlist[1] = (num//10000000)%10
    numlist[2] = (num//1000000)%10
    numlist[3] = (num//100000)%10
    numlist[4] = (num//10000)%10
    numlist[5] = (num//1000)%10
    numlist[6] = (num//100)%10
    numlist[7] = (num//10)%10
    numlist[8] = (num//1)%10
    return numlist

def numtowords(num):
    word =''
    if num==0:
        word = 'zero'
    if num<0:
        word = 'negative '
        num *= -1
    numlist = numtolist(num)
    if num>=1 and num<=9:
        word += units[num]
    if num>=10 and num<=19:
        word += teens[num%10]
    if num>=20 and num<=99:
        word += tens[num//10]
        if numlist[8]!=0:
            word+=' '+units[num%10]
    if num>=100 and num<=999:
        word += units[num//100%10] + ' hundred'
        if numlist[7]!=0:
            word += ' '+tens[num//10%10]
        if numlist[8]!=0:
            word+=' '+units[num%10]
    if num>=1000 and num<=9999:
        word += units[num//1000%10] + ' thousand'
        if numlist[6]!=0:
            word += ' '+units[num//100%10] + ' hundred'
        if numlist[7]!=0:
            word += ' '+tens[num//10%10]
        if numlist[8]!=0:
            word+=' '+units[num%10]
    if num>=10000 and num<=999999:
        word += numtowords(numlist[3]*100 + numlist[4]*10 + numlist[5])+' thousand'
        if numlist[6]!=0:
            word += ' '+units[num//100%10] + ' hundred'
        if numlist[7]!=0:
            word += ' '+tens[num//10%10]
        if numlist[8]!=0:
            word+=' '+units[num%10]
    if num>=1000000 and num<=999999999:
        word += numtowords(numlist[0]*100 + numlist[1]*10 + numlist[2])+' million'
        if numlist[3]!=0 or numlist[4]!=0 or numlist[5]!=0:
            word += ' '+numtowords(numlist[3]*100 + numlist[4]*10 + numlist[5])+' thousand'
        if numlist[6]!=0:
            word += ' '+units[num//100%10] + ' hundred'
        if numlist[7]!=0:
            word += ' '+tens[num//10%10]
        if numlist[8]!=0:
            word+=' '+units[num%10]
    return word

print(numtowords(int(input("Enter any Number: "))))