import os

WINDOW_SIZE = 6

def read_message(filename):

    message = []

    try:
        folder = os.path.dirname(__file__)
        if not filename.endswith(".txt"):
            filename += ".txt"
        filepath = os.path.join(folder, filename)
        with open(filepath, "r") as file:
            while True:
                char = file.read(1)
                if char == "":
                    break
                message.append(char)
        return message

    except FileNotFoundError:
        return None


def LZ77_compression(message):

    compressed = []
    i = 0
    while i < len(message):

        window_start = max(0, i - WINDOW_SIZE)
        best_offset = 0
        best_length = 0

        for j in range(window_start, i):
            length = 0
            while (
                i + length < len(message)
                and message[j + length] == message[i + length]
            ):
                length += 1
            if length > 0 and length >= best_length:
                best_length = length
                best_offset = i - j
        if i + best_length < len(message):
            next_char = message[i + best_length]
        else:

            next_char = ""

        compressed.append(
            (best_offset, best_length, next_char)
        )
        i += best_length
        if next_char != "":
            i += 1
    return compressed


def write_compressed(compressed, newname):
    folder = os.path.dirname(__file__)
    if not newname.endswith(".txt"):
        newname += ".txt"
    filepath = os.path.join(folder, newname)
    with open(filepath, "w") as file:
        for tag in compressed:
            file.write(str(tag) + "\n")



# decompression  read file


def read_compressed(filename):

    compressed = []

    try:

        folder = os.path.dirname(__file__)

        if not filename.endswith(".txt"):
            filename += ".txt"

        filepath = os.path.join(folder, filename)

        with open(filepath, "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                tag = eval(line)

                compressed.append(tag)

        return compressed

    except FileNotFoundError:

        return None



# LZ77 decompression

def LZ77_decompression(compressed):

    message = []

    for offset, length, next_char in compressed:

        if offset == 0 and length == 0:

            if next_char != "":
                message.append(next_char)

        else:

            start = len(message) - offset

         
            for i in range(length):

                message.append(message[start + i])

            if next_char != "":
                message.append(next_char)

    return message


# Write decompressed file


def write_message(message, newname):

    folder = os.path.dirname(__file__)

    if not newname.endswith(".txt"):
        newname += ".txt"

    filepath = os.path.join(folder, newname)

    with open(filepath, "w") as file:

        file.write("".join(message))



print("================================")
print("       LZ77 Compression")
print("================================")

print("1. Compression")
print("2. Decompression")

choice = input("Choose an option: ")


match choice:

    # Compression
    

    case "1":

        input_name = input("Enter input file name: ")

        output_name = input("Enter output file name: ")

        message = read_message(input_name)

        if message is not None:

            compressed = LZ77_compression(message)

            write_compressed(compressed, output_name)

            print("\nCompression completed successfully!")

            print("Output file:", output_name)

            print("\nCompressed tokens:")

            for token in compressed:

                print(token)

        else:

            print("\nFile not found!")


    # Decompression

    case "2":

        input_name = input("Enter compressed file name: ")

        output_name = input("Enter output file name: ")

        compressed = read_compressed(input_name)

        if compressed is not None:

            message = LZ77_decompression(compressed)

            write_message(message, output_name)

            print("\nDecompression completed successfully!")

            print("Output file:", output_name)

            print("\nDecompressed message:")

            print("".join(message))

        else:

            print("\nFile not found!")


    # Wrong Choice

    case _:

        print("\nInvalid choice!")
