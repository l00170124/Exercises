# Infrastructure as code - Assignment 1 - Project Status

>The project is currently completed to a certain level, the code code be cleaner and there are a few errors appearing but it does read the log file and bring back the required data to the csv file. 

The following are limitations/issues in the code have been identified:

1. There is a error generating from this dictionary entry "18:68", a key error. A charachter "A" was placed inf ront of the key values to aim to resolve as it may be reading the digits incorrectly. This did not resolve the issue. 
2. Line 4 of the poutput code is brining in an additional line I could not identify why. It is identified as ",192.168.5.172,(secs),unknown"
3. Originally the csvwriter command was to be used to write to the SCV file but the coder was unable to get this to work in the programme. It was replaced by the f.write command. 
