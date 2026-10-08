# LZ77 Compression and Decompression

This project implements the **LZ77 compression algorithm** using Python.

## Features

* Compress a text file using LZ77.
* Decompress the compressed file.
* Uses a sliding window with `WINDOW_SIZE = 6`.
* Supports overlapping matches.
* Saves compressed data as tuples:

  ```text
  (offset, length, next_character)
  ```

## How LZ77 Works

LZ77 searches for repeated sequences in the previous part of the message.

Each compressed token contains:

* **Offset**: How far back the matching sequence starts.
* **Length**: Number of matching characters.
* **Next Character**: The character after the matched sequence.

Example:

```text
(3, 4, 'B')
```

This means:

* Go back 3 characters.
* Copy 4 characters.
* Then add `B`.

## Time Complexity

### Compression

| Case         | Complexity                                        |
| ------------ | ------------------------------------------------- |
| Best Case    | O(n)                                              |
| Average Case | Depends on input, commonly between O(n) and O(n²) |
| Worst Case   | O(n²)                                             |

The worst case can happen with highly repetitive input such as:

```text
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

because the algorithm performs long character comparisons.

### Decompression

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n)       |
| Average Case | O(n)       |
| Worst Case   | O(n)       |

Each character in the decompressed message is generated once.

## Project Structure

```text
LZ77/
│
├── main.py
├── input.txt
├── compressed.txt
├── output.txt
└── README.md
```

## How to Run

Run the Python program:

```bash
python main.py
```

Then choose:

```text
1. Compression
2. Decompression
```

## Example

Input:

```text
ABAABABAAB
```

The program compresses the message into LZ77 tuples and can then reconstruct the original message during decompression.

## Requirements

* Python 3.x

No external libraries are required.

## Notes

The implementation uses a sliding window of size `6`:

```python
WINDOW_SIZE = 6
```

**Names:**

Kareem Ahmed Abdelmoneim  
Badr Rafik Mohamed  
Mohamed Said Abd El-wahhab 

The decompression algorithm supports **overlapping matches**, which allows efficient compression of highly repetitive data.
