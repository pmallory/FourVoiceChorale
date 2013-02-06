from midiutil.MidiFile import MIDIFile
import random
from collections import namedtuple

Chord = namedtuple('Chord', 'alto, soprano, tenor, bass')

def main():
    # Create the MIDIFile Object with one track
    MyMIDI = MIDIFile(4)

    # tracks are numbered from 0
    soprano_track = 0
    alto_track = 1
    tenor_track = 2
    bass_track = 3

    MyMIDI.addTrackName(soprano_track, 0, "Soprano")
    MyMIDI.addTrackName(alto_track, 0, "Alto")
    MyMIDI.addTrackName(tenor_track, 0, "Tenor")
    MyMIDI.addTrackName(bass_track, 0, "Bass")

    MyMIDI.addTempo(soprano_track, 0, 120)
    MyMIDI.addTempo(alto_track, 0, 120)
    MyMIDI.addTempo(tenor_track, 0, 120)
    MyMIDI.addTempo(bass_track, 0, 120)

    initial_chord = Chord(alto=77, soprano=67, tenor=59 ,bass=57)

    # Soprano is from C4 to A5, MIDI notes [60, 81]
    # Alto is from G3 to F5, MIDI notes [55, 76]
    # Tenor is from C3 to A4, MIDI notes [48, 69]
    # Bass is from E2 to E4, MIDI notes [40, 64]

    previous_chord = initial_chord
    for note_number in xrange(64):
        current_chord = move(previous_chord)



        MyMIDI.addNote(soprano_track, 0, current_chord.soprano, note_number, 1, 100)
        MyMIDI.addNote(alto_track, 1, current_chord.alto, note_number, 1, 100)
        MyMIDI.addNote(tenor_track, 2, current_chord.tenor, note_number, 1, 100)
        MyMIDI.addNote(bass_track, 2, current_chord.bass, note_number, 1, 100)

    # Save song.
    binfile = open("output.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()

def move(chord):
    #keep the common voice, or move up to one tone. Stay in range.
    if 60 <= chord.soprano <= 81:
        pitch_soprano = chord.soprano + random.choice(xrange(-2, 3))
    elif chord.soprano < 60:
        pitch_soprano = chord.soprano + random.choice(xrange(0, 3))
    else:
        pitch_soprano = chord.soprano + random.choice(xrange(-2, 1))

    if 55 <= chord.alto<= 76:
        pitch_alto = chord.alto + random.choice(xrange(-2, 3))
    elif chord.alto < 55:
        pitch_alto = chord.alto + random.choice(xrange(0, 3))
    else:
        pitch_alto = chord.alto + random.choice(xrange(-2,1))

    if 48 <= chord.tenor <= 69:
        pitch_tenor = chord.tenor + random.choice(xrange(-2, 3))
    elif chord.tenor < 48:
        pitch_tenor = chord.tenor + random.choice(xrange(0, 3))
    else:
        pitch_tenor = chord.tenor + random.choice(xrange(-2,1))

    pitch_bass = chord.bass + random.choice(range(-2,3))

    return Chord(soprano=pitch_soprano,
                 alto=pitch_alto,
                 tenor=pitch_tenor,
                 bass=pitch_bass)


if __name__ == '__main__':
   main()
