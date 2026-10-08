# LZ77 Algorithm

A simple Python implementation of the LZ77 lossless data compression algorithm.

This project reads a text file, compresses it using LZ77-style tokenization, writes the compressed output to another text file, and can also decompress the result back to its original form.

## Features

- Reads text input from `.txt` files
- Compresses data using a sliding window with a fixed window size
- Stores tokens as `(offset, length, next_char)`
- Writes compressed tokens to a output file
- Decompresses the token stream back into the original message
- Includes a simple interactive command-line menu

## Project Files

- `LZ77.py` — main implementation of the compression and decompression logic
- `kareem.txt` — sample input text file
- `README.md` — project documentation

## How LZ77 Works

The algorithm searches backward in a limited window to find the longest repeated sequence, then encodes it with:

- offset: how far back the match occurred
- length: how many characters matched
- next_char: the next character after the match

This approach reduces redundancy by replacing repeated patterns with shorter reference tokens.

## Usage

1. Open a terminal in the repository folder.
2. Run the script:

```bash
python LZ77.py
```

3. Choose an option:
   - `1` for compression
   - `2` for decompression

4. Enter the input filename and output filename.

Note: the script expects `.txt` files and writes the generated output in the same directory as the script.

## Example

If you have a file named `sample.txt` with the content:

```text
ABABABABA
```

The program will compress it by referencing repeated patterns in the previous window and then reconstruct the same content during decompression.

## Notes

- The window size is currently set to `6` in the script and can be adjusted by changing `WINDOW_SIZE` in `LZ77.py`.
- The implementation is educational and intended to demonstrate the LZ77 algorithm clearly and simply.

## License

This project is provided for learning and demonstration purposes.
