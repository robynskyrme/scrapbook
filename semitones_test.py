# Basic handling of musical pitches

names = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]

shapes = {
    "triad_major":[4,3],
    "triad_minor":[3,4],
    "scale_major":[2,2,1,2,2,2],
    "scale_dorian":[2,1,2,2,2,1]
}

def get_notes(key,shape,count):
    notes = [0]

    shape = shapes[shape]
    shape.append(12-sum(shape))

    key = names.index(key)


    iter = 0
    while len(notes) < count:
        notes.append(shape[iter % len(shape)])
        iter += 1

    for n in range(1,len(notes)):
        notes[n] += notes[n-1] % 12

    for n in range(len(notes)):
        notes[n] = names[(notes[n]+key) % 12]

    return notes


if __name__ == "__main__":
    print("\n")
                            # a few tests:
    print("D major triad, three octaves: " + str(get_notes("d","triad_major",10)))
    print("C major scale, two octaves: " + str(get_notes("c","scale_major",15)))
    print("G# minor triad, two octaves: " + str(get_notes("g#","triad_minor",7)))
    print("B major scale, one octave: " + str(get_notes("b","scale_major",8)))
    print("E dorian, two octaves: " + str(get_notes("e","scale_dorian",15)))