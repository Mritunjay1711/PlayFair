plainText = input('Enter the plainText\n')
print(plainText)
key = input('Enter the key\n')
print(key)
plainText = plainText.upper()
key = key.upper()


def remove(plainText):
    return plainText.replace(" ", "")


plainText = remove(plainText)

rows,cols = (5, 5)
arr = [[0] * cols] * rows


def keyMatrix(arr, key):
    N = 26
    alpha = [0] * N
    