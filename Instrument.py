class Instrument:
    def play(self):
        return "Playing the instrument."

class Guitar(Instrument):
    def play(self):
        return "Strumming the guitar."

class Piano(Instrument):
    def play(self):
        return "Playing the piano."

def play_instrument(instrument):
    """Call the play method of the given instrument instance and print the result."""
    print(instrument.play())

# Example usage:
guitar = Guitar()
piano = Piano()

play_instrument(guitar)  # Output: Strumming the guitar.
play_instrument(piano)   # Output: Playing the piano.
