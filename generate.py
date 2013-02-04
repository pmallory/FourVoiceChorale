from midiutil.MidiFile import MIDIFile
import random

# Create the MIDIFile Object with one track
# TODO: one track per voice
MyMIDI = MIDIFile(1)

# tracks are numbered from 0
soprano_track = 0

# Add soprano track, starting on beat 0
MyMIDI.addTrackName(soprano_track, 0, "Soprano")
MyMIDI.addTempo(soprano_track, 0, 120)

# Soprano is from C4 to A5 (MIDI note 60 to 81)
pitch_soprano =  72 #start in the middle of the soprano range

# Generate the soprano's part, keep the common tone or move by one
for note_number in xrange(16):
    pitch_soprano += random.choice([-1, 0, 1])

    MyMIDI.addNote(0, 0, pitch_soprano, note_number, 1, 100)


# Save song.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

