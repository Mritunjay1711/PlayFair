from queue import Queue
from collections import deque
plainText = input('Enter the plainText\n')
key = input('Enter the key\n')
plainText = plainText.upper()
key = key.upper()


def remove(plainText):
    return plainText.replace(" ", "")


plainText = remove(plainText)

arr = []


def keyMatrix(arr, key):
    N = 26
    alpha = [0] * N
    queue = []

    for i in key:
        temp = ord(i) - ord('A')
        if i != 'J' and alpha[temp] != 1:
            alpha[temp] = 1
            queue.append(i)
    for i in range(len(alpha)):
        if alpha[i] != 1:
            temp = chr(i + ord('A'))
            if temp != 'J':
                queue.append(temp)

    for i in range(5):
        row = []
        for j in range(5):
            temp = queue.pop(0)
            print(temp)
            row.append(temp)
        arr.append(row)


keyMatrix(arr, key)
print(arr)
