from queue import Queue
from collections import deque
from tkinter import N
plainText = input('Enter the plainText\n')
key = input('Enter the key\n')
plainText = plainText.upper()
key = key.upper()


def remove(plainText):
    return plainText.replace(" ", "")


plainText = remove(plainText)
cipherText = ''
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
            print(temp, end=" ")
            row.append(temp)
        print()
        arr.append(row)


def findIndex(arr, ch):
    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            if arr[i][j] == ch:
                return i, j


def encryption(arr, plainText, cipherText):
    i = 0
    n = len(plainText)
    while i < n:
        ind1i, ind1j = findIndex(arr, plainText[i])
        # print(ind1i, ind1j)
        i = i + 1
        if i == n:
            ind2i, ind2j = findIndex(arr, 'X')
            # print(ind2i, ind2j)
            i = i + 1
        else:
            ind2i, ind2j = findIndex(arr, plainText[i])
            # print(ind2i, ind2j)
            i = i + 1
        if ind1i == ind2i:
            # print(ind1i, ind2i)
            cipherText = cipherText + arr[ind1i][(ind1j + 1) % 5]
            print(cipherText)
            # print(arr[ind1i][(ind1j + 1) % 5])
            cipherText = cipherText + arr[ind2i][(ind2j + 1) % 5]
        elif ind1j == ind2j:
            cipherText = cipherText + arr[(ind1i + 1) % 5][ind1j]
            cipherText = cipherText + arr[(ind2i + 1) % 5][ind2j]
        else:
            cipherText = cipherText + arr[ind1i][ind2j]
            cipherText = cipherText + arr[ind2i][ind1j]

    return cipherText


def decryption(arr, plainText, cipherText):
    i = 0
    n = len(cipherText)
    while i < n:
        ind1i, ind1j = findIndex(arr, cipherText[i])
        i = i + 1
        ind2i, ind2j = findIndex(arr, cipherText[i])
        i = i + 1
        if ind1i == ind2i:
            plainText = plainText + arr[ind1i][(ind1j + 1) % 5]
            plainText = plainText + arr[ind2i][(ind2j + 1) % 5]
        elif ind1j == ind2j:
            plainText = plainText + arr[(ind1i + 1) % 5][ind1j]
            plainText = plainText + arr[(ind2i + 1) % 5][ind2j]
        else:
            plainText = plainText + arr[ind1i][ind2j]
            plainText = plainText + arr[ind2i][ind1j]

    return plainText


keyMatrix(arr, key)
# ch = 'A'
# indi, indj = findIndex(arr, ch)
# print(indi, indj)
cipherText = encryption(arr, plainText, cipherText)
print("Cipher Text", cipherText)

plaintext = decryption(arr, plainText, cipherText)
print("Plain Text", plaintext)
