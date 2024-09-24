from collections import Counter
import re
import numpy as np

def word_frequency(text_or_path):
    """
    Count how frequently each word appears in the text.
    Can accept a string or a file path to a text file.
    """
    def get_words(text):
        return re.findall(r'\b\w+\b', text.lower())

    if isinstance(text_or_path, str):
        if '\n' in text_or_path or len(text_or_path.split()) > 1:  # Detect if it's a string of text
            words = get_words(text_or_path)
        else:  # Assume it's a file path if not enough words or no newline
            with open(text_or_path, 'r') as file:
                words = get_words(file.read())
    return Counter(words)

def unique_words(text_or_path):
    """
    Extract unique words from the text.
    """
    def get_words(text):
        return set(re.findall(r'\b\w+\b', text.lower()))

    if isinstance(text_or_path, str):
        if '\n' in text_or_path or len(text_or_path.split()) > 1:
            words = get_words(text_or_path)
        else:
            with open(text_or_path, 'r') as file:
                words = get_words(file.read())
    return words

def word_cooccurrence_matrix(text_or_path, window=2):
    """
    Create a word co-occurrence matrix with a given window size.
    """
    def get_words(text):
        return re.findall(r'\b\w+\b', text.lower())

    if isinstance(text_or_path, str):
        if '\n' in text_or_path or len(text_or_path.split()) > 1:
            words = get_words(text_or_path)
        else:
            with open(text_or_path, 'r') as file:
                words = get_words(file.read())

    word_indices = {word: idx for idx, word in enumerate(set(words))}
    co_occurrence_matrix = np.zeros((len(word_indices), len(word_indices)))

    for idx, word in enumerate(words):
        for neighbor in words[max(idx - window, 0): min(idx + window + 1, len(words))]:
            if word != neighbor:
                i, j = word_indices[word], word_indices[neighbor]
                co_occurrence_matrix[i][j] += 1

    return co_occurrence_matrix, word_indices

def text_generator(text_or_path):
    """
    A generator that yields one line of text at a time.
    """
    if isinstance(text_or_path, str):
        if '\n' in text_or_path:  # If string contains newline characters
            for line in text_or_path.strip().splitlines():
                yield line.strip()
        else:  # Assume it's a file path
            with open(text_or_path, 'r') as file:
                for line in file:
                    yield line.strip()

