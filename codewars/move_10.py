import string

"""
Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.

tbl = str.maketrans(al, al[10:] + al[:10])
def move_ten(st):
    return st.translate(tbl)

"""

def move_ten(st):
    switched = []
    ascii = string.ascii_lowercase

    for char in st:
        indx = ascii.index(char) + 10
        try:
            switched.append(ascii[indx])
        except IndexError:
            switched.append(ascii[indx - len(ascii)])
            
    return ''.join(switched)

