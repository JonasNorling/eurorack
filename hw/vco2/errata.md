# Errata


## Revision 2

Changes made to revision 2 boards after assembly at JLCPCB:

  - PWM range: R29,R30,R40,R41 0 ohm. R38,R42 39k. R19,R49 DNP.
    This change is made to improve the PWM range and let the pots control
    the full pulse width from 0 to 100%.

  - C17 1uF LFO cap.
    The low frequency range with C17=100n is 0.5 to 70 Hz which is too fast.
    With 1uF we get 18 to 8 Hz or so.
