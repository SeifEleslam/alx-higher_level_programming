#!/usr/bin/python3
"""Print Text with custom line speration"""


def text_indentation(text):
    """Print Text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[start:i+1].strip(), end="\n\n")
            start = i+1
        elif i == len(text)-1:
            print(text[start:].strip(), end="")
