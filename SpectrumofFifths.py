# All (sensible) musical pitches handled using a spectrum of fifths
# Gbb to Ax, 1-31, with D natural at the centre

names = ["Gbb","Dbb","Abb","Ebb","Bbb",
            "Fb","Cb","Gb","Db","Ab","Eb","Bb",
            "F","C","G","D","A","E","B",
            "F#","C#","G#","D#","A#","E#","B#",
            "Fx","Cx","Gx","Dx","Ax"]

shapes = {
    "triad_major":[4,3],
    "triad_minor":[3,4],
    "scale_major":[0,2,4,-1,1,3,5],
    "scale_dorian":[2,1,2,2,2,1]
}

def get_notes(key,shape):
    notes = []

    key = names.index(key)

    for note in shapes[shape]:
        notes.append(note + key)

    return notes

def ints_to_notes(notes):
    return_names = []
    for note in notes:
        return_names.append(names[note])
    return return_names


                            # shift is an integer in SEMITONES
def transpose(notes,shift):
                            # converted here into fifths:
    shift = (shift + 6*(shift % 2)) % 12

    trans = []

    for note in notes:
        trans.append(note + shift)

    trans = enharmonic(trans)

    return trans

def enharmonic(notes):
    temp = []
    if sum(notes) / len(notes) > 22:
        for note in notes:
            temp.append(note - 12)
    elif sum(notes) / len(notes) < 9:
        for note in notes:
            temp.append(note + 12)
    else:
        temp = notes
    return temp

if __name__ == "__main__":
    print("\n")
                            # a few tests:
    print("C major scale: " + str(ints_to_notes(get_notes("C","scale_major"))))

    print("B major scale transposed down a third: " + str(ints_to_notes(transpose(get_notes("B","scale_major"),-4))))