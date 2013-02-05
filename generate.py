from midiutil.MidiFile import MIDIFile
import random

# Create the MIDIFile Object with one track
# TODO: one track per voice
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

# Soprano is from C4 to A5, MIDI notes [60, 81]
pitch_soprano = 72 #start in the middle of the soprano range
# Alto is from G3 to F5, MIDI notes [55, 76]
pitch_alto = pitch_soprano - random.choice(range(1, 12)) #within an octave of soprano
# Tenor is from C3 to A4, MIDI notes [48, 69]
pitch_tenor = pitch_alto - random.choice(range(1, 12)) #within an octave of alto
# Bass is from E2 to E4, MIDI notes [40, 64]
pitch_bass = 52 #start in middle

# Generate the soprano's part, keep the common tone or move by one
for note_number in xrange(64):

    #keep the common voice, or move up to one tone. Stay in range.
    if 60 <= pitch_soprano <= 81:
        pitch_soprano += random.choice(xrange(-2, 3))
    elif pitch_soprano < 60:
        pitch_soprano += random.choice(xrange(0, 3))
    else:
        pitch_soprano += random.choice(xrange(-2, 1))

    if 55 <= pitch_alto<= 76:
        pitch_alto += random.choice(xrange(-2, 3))
    elif pitch_alto < 55:
        pitch_alto += random.choice(xrange(0, 3))
    else:
        pitch_alto += random.choice(xrange(-2,1))

    if 48 <= pitch_tenor <= 69:
        pitch_tenor += random.choice(xrange(-2, 3))
    elif pitch_tenor < 48:
        pitch_tenor += random.choice(xrange(0, 3))
    else:
        pitch_tenor += random.choice(xrange(-2,1))

    pitch_bass += random.choice(range(-2,3))



    MyMIDI.addNote(soprano_track, 0, pitch_soprano, note_number, 1, 100)
    MyMIDI.addNote(alto_track, 1, pitch_alto, note_number, 1, 100)
    MyMIDI.addNote(tenor_track, 2, pitch_tenor, note_number, 1, 100)
    MyMIDI.addNote(bass_track, 2, pitch_bass, note_number, 1, 100)


# Save song.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

