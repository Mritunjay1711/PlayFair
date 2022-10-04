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
cypherText = ''
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


def encryption(arr, plainText, cypherText):
    i = 0
    n = len(plainText)
    while i < n:
        ind1i, ind1j = findIndex(arr, plainText[i])
        i = i + 1
        if i == n:
            ind2i, ind2j = findIndex(arr, 'X')
            i = i + 1
        else:
            ind2i, ind2j = findIndex(arr, plainText[i])
            i = i + 1
        if ind1i == ind2i:
            cypherText = cypherText + arr[ind1i][(ind1j + 1) % 5]
            cypherText = cypherText + arr[ind2i][(ind2j + 1) % 5]
        elif ind1j == ind2j:
            cypherText = cypherText + arr[(ind1i + 1) % 5][ind1j]
            cypherText = cypherText + arr[(ind2i + 1) % 5][ind2j]
        else:
            cypherText = cypherText + arr[ind1i][ind2j]
            cypherText = cypherText + arr[ind2i][ind1j]


keyMatrix(arr, key)
# ch = 'A'
# indi, indj = findIndex(arr, ch)
# print(indi, indj)
encryption(arr, plainText, cypherText)
print("Cipher text", cypherText)
