noum_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def latin(noum):

    latin = ''

    while noum > 0:
        for i, l in noum_list:
            while noum >= i and noum <1000000:
                latin = latin + l
                noum = noum - i

    return latin
noum = int(input("Enter an interger: "))
print latin(noum)
