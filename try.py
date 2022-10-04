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
            print(temp, end = " ")
            row.append(temp)
        print()
        arr.append(row)

def findIndex(arr, ch):
    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            if arr[i][j] == ch:
                return i, j;


keyMatrix(arr, key)
ch = 'A'
indi, indj=findIndex(arr, ch)
print(indi, indj)
print(arr)

