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


# =========================
# Main
# =========================

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
