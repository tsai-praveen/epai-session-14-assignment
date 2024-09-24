# Text Toolkit

text_toolkit is a Python module designed for text analysis tasks, such as word frequency counting, unique word extraction, word co-occurrence matrix generation, and efficient processing of large text files using generators. It supports both text string inputs and file path inputs, making it flexible for various use cases.

## Features:

* Word Frequency Counter: Count how often each word appears in a text.
* Unique Word Extractor: Extract all unique words from a text.
* Word Co-occurrence Matrix: Create a matrix showing how often words appear next to each other within a specified window * size.
* Text Generator: Efficiently process large files by yielding one line at a time.

## Usage 

```
import text_toolkit as tt

# Example usage:
freq = tt.word_frequency('example.txt')
print(freq)

unique = tt.unique_words('example.txt')
print(unique)

cooccurrence_matrix = tt.word_cooccurrence_matrix('example.txt')
print(cooccurrence_matrix)

# Example of using the text generator
for line in tt.text_generator('example.txt'):
    print(line)
```
