def character_in_range(start_char: str, end_char: str) -> str:
    start_char, end_char = ord(start_char), ord(end_char)

    if end_char < start_char:
        start_char, end_char = end_char, start_char

    # chars = " ".join(chr(ch) for ch in range(start_char + 1, end_char))

    char = ""
    for ch in range(start_char + 1, end_char):
        char += f"{chr(ch)} "

    return char


start_ch = input()
end_ch = input()

print(character_in_range(start_ch, end_ch))
