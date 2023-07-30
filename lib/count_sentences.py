#!/usr/bin/env python3
import io
import sys
import re

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Split the string using regular expressions to handle punctuation marks
        sentences = re.split(r"[.!?]", self._value)

        # Remove any empty strings from the list of sentences
        sentences = list(filter(lambda x: x.strip(), sentences))

        return len(sentences)