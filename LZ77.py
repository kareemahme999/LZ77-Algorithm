def lz77_compression(text, window_size=8):

    tokens = []
    i = 0

    while i < len(text):
        window_start = max(0, i - window_size)
        best_offset = 0
        best_length = 0
    
        for j in range(window_start, i):
            length = 0

            while (i + length < len(text) and length < window_size and text[j + length] == text[i + length]):
                length += 1
            
            if length > best_length:
                best_length = length
                best_offset = i - j

        next_char = text[i + best_length] if i + best_length < len(text) else ""

        tokens.append({"offset": best_offset, "length": best_length, "next": next_char})

        i += best_length + (1 if next_char else 0)

    return tokens

lz77_compression("aacaacabcaba")