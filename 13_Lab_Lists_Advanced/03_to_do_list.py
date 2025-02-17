notes = [0] * 10
note = input()

while note != "End":
    note = note.split("-")

    priority = int(note[0])
    current_note = note[1]

    index = priority - 1

    notes.pop(index)  # first remove the position
    notes.insert(index, current_note)  # then inserting the new element

    note = input()

notes = [str(s) for s in notes if str(s) != "0"]
print(notes)

