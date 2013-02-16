from midiutil.MidiFile import MIDIFile
import random

"""Generate a four measure melody is an arch chaped contour."""
def main():
    midi_file = MIDIFile(1)

    midi_file.addTrackName(0, 0, 'tune')
    midi_file.addTempo(0, 0, 120)

    base_tone = 64

    steps = fuzzy_steps()

    melody = map(lambda x: x+base_tone, steps)

    for beat, note in enumerate(melody):
        print ('tune', 0, note, beat, 1, 100)

        midi_file.addNote(0, 0, note, beat, 1, 100)


    # Save song.
    binfile = open("output.mid", 'wb')
    midi_file.writeFile(binfile)
    binfile.close()

def fuzzy_steps():
    '''return an increasing series that sums to 8'''
    s = [-2,-1,0,1,2,3]
    melody = []

    for i in xrange(1000):
        melody.append(random.choice(s))

    for i in range(len(melody)-8):
        candidate = melody[i:i+8]
        if sum(candidate)==8 and max(candidate)==candidate[-1] and candidate[0]<candidate[-1]:
            return candidate
    else:
        # this algo's worst case is not so good
        return fuzzy_steps()

if __name__ == '__main__':
    main()
