from queue import Queue
from collections import deque
from tkinter import N
from easyocr import Reader
import argparse
import cv2


def remove(plainText):
    return plainText.replace(" ", "")


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
            # print(cipherText)
            # print(arr[ind1i][(ind1j + 1) % 5])
            cipherText = cipherText + arr[ind2i][(ind2j + 1) % 5]
        elif ind1j == ind2j:
            cipherText = cipherText + arr[(ind1i + 1) % 5][ind1j]
            cipherText = cipherText + arr[(ind2i + 1) % 5][ind2j]
        else:
            cipherText = cipherText + arr[ind1i][ind2j]
            cipherText = cipherText + arr[ind2i][ind1j]

    return cipherText



a = input("Enter the way to input the Plain text:\n1 for text\n2 for Image\n")
if a == "1":
    plainText = input('Enter the plainText\n')
elif a == "2":
    pathImage = input("Enter the path of image: ")
    language = input("Enter the languages in image: ")

    langs = language.split(", ")
    print("[INFO] using the following languages: {}".format(langs))
    image = cv2.imread(pathImage)

    print("[INFO] Performing OCR on input image...")
    reader = Reader(langs, gpu=1)
    results = reader.readtext(image)

    plainText = ""

    for(bbox, text, prob) in results:
        print("[INFO] {:.4f}: {}".format(prob, text))
        plainText = plainText+text
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))

        cv2.rectangle(image, tl, br, (0, 255, 0), 2)
        cv2.putText(image, text, (tl[0], tl[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
else:
    print("Invalid input!")
    exit(0)

plainText = remove(plainText)
print(f"Plain text = {plainText}")
cipherText = ''
arr = []
key = input('Enter the key\n')
plainText = plainText.upper()
key = key.upper()

keyMatrix(arr, key)
# ch = 'A'
# indi, indj = findIndex(arr, ch)
# print(indi, indj)
cipherText = encryption(arr, plainText, cipherText)
print("Cipher Text", cipherText)

# plaintext = decryption(arr, plainText, cipherText)
# print("Plain Text", plaintext)
