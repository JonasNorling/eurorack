This is a dual voltage controller oscillator (VCO) based on the SSI2131 chip, for Eurorack modular synthesizer systems. In goes a one-volt-per-octave control voltage (CV) and out comes a triangle, saw and square wave. Times two. The second oscillator also has a handy low frequency mode.

## Specs

- Power consumption +12V 60mA, -12V 50mA
- Frequency range without CV input: approx. 12Hz to 1.5kHz
- Selectable low frequency range of second oscillator: approx. 2.8 Hz to 50 seconds
- Inputs:
  - CV (1 volt per octave) for each oscillator. Second oscillator CV normalled to first.
  - PWM (pulse width modulation) for each oscillator square wave, approx. ±5V
- Pots:
  - Range: 7 octave rough tuning
  - Tune: 5 semitone fine tuning
  - PW: Pulse width for square output, 0-100%
- Outputs:
  - Triangle wave ±5V, DC coupled 1kΩ
  - Saw wave ±5V, DC coupled 1kΩ
  - Square wave ±5V, AC coupled

## Assembly instructions

- Solder the shrouded pin header on the bottom side of the board. You could use a rubber band to hold it down.
- Power it up and check voltages.
- Solder the electrolytic caps on the top side of the board, minding polarity. White stripe and short lead means negative, goes into the hole with round pad. Be sure to keep height below 9mm.
- Solder the trimmer pots to the bottom side of the board. The screw should point away from the chip (not that it matters but it will make the calibration instructions correct). Rev 2 board: watch out for the trimmer lead shorting against the switch later on.
- With the aid of a multimeter in ohms mode, adjust the trimmer pots until you measure 24.3kohm between 2.5V (TP3) and pin 13 on each SSI2131. For me this meant 1.5 turns to the left (out). This is not strictly necessary but will make calibration easier later on.
- Put all the jacks, pots, switch and LEDs in their holes. Short, negative, lead on the LEDs go in the holes with square pads. Remove nut and washer from the pots before installing. The two plastic shaft pots are for PW. Put on the front panel and put a couple of rubber bands around the whole thing to hold everything in position. Then solder down all the pots and jacks and the switch. Do the LEDs last, making sure they are aligned properly. LEDs are heat sensitive, so be swift. Trim the LED leads last.
- Put on the front panel and screw on the nuts. Install knobs. The nuts for the 3.5mm jacks are fiddly and designed to drive you mad.
- Power it up and check that outputs are reasonable: around 10.5Vpp from around 11 to 1.5 kHz. It should be fairly playable already if you managed to adjust the tracking trimmer pots with a multimeter.

### Trimming the tracking

- Connect CV to a trusted keyboard or something. Tune the tracking by playing octaves and adjusting trimmers until it sounds right. Use a tuner (could be a phone app) to preserve mental health.
  - Play a low A and tune it with the range and tuning knobs
  - Play a high A and adjust the trimmer pot. If the high note is too high turn left (out), if it's too low turn right (in).
  - Repeat many times. The lower note will have moved when you turned the trimmer.
