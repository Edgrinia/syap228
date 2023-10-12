string="fjdfj(fuu((xxx)aaa)xxasf((mcmzx))"

i = []
left = 0
right = 0
k=0

while k<len(string):
    for el in string:
        if el == '(':
            left = k
            i.append('(')
        if el == ')' and len(i) > 0:
            i.clear()
            right = k
            s = string[left:right + 1]
            print(s)
            string = string.replace(s, '')
            right = 0
            left = 0
            k=0
        k += 1

    # print(str(left) + " ---- " + str(right) + "\n")

print(string)
