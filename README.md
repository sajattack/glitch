#glitch.py
Randomly changes binary file data in order to create glitch art.
##Usage
```./glitch <infile> [percent] [outfile]```
        
		infile: the file to take as input
		
        percent: the percentage of the file to corrupt, by default, 0.1%
		
        outfile: the file to output, by default <filename>-glitched.<fileext>

Play around with different values for percent, 0.1 seems to work okay for most image formats, 0.01 worked okay for avi video.