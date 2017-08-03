# balsamiq_directorytree
## Generate a Balsamiq Mockups compatible tree list off a directory on disk

Balsamiq Mockups allows you to display trees but it has its own language for the tree source, which is text based.
I found boring to manually type in the needed, thus I wrote a python tool to produce a directory listing according to what's expected from Balsamiq Mockup.

This is the output of a run:

[dariod@prometeo dir01]$ python ../../balsamiq_tree.py
F dir01
 F dir02
  F dir03
   - XX_0000.dat
   - XX_0001.dat
  F dir11
   - XX6S1dFM_Y0001.dat
   - XX6S1dffM_0000.dat
 F dir04
  F dir05
   F dir06
    - VALVE_0001.dat
    - VALVE_0000.dat
   F dir07
    - design.dat
