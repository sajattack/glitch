#glitch.py
Randomly changes binary file data in order to create glitch art.
##Usage
```./glitch <infile> [percent] [outfile]```
        
		infile: the file to take as input
		
        percent: the percentage of the file to corrupt, by default, 0.1%
		
        outfile: the file to output, by default <filename>-glitched.<fileext>

Play around with different values for percent, 0.1 seems to work okay for most image formats, 0.01 worked okay for video.
Also, try different filetypes and share your results!

##Examples
![glados-original](/examples/glados.gif)

![glados-glitched](/examples/glados-glitched.gif)

![peacemaker-original](/examples/peacemaker.jpg)

![peacemaker-glitched](/examples/peacemaker-glitched.jpg)

![reaper_core-original](/examples/reaper_core.png)

![reaper_core-glitched](/examples/reaper_core-glitched.png)