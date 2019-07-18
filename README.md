# MorseDecoder


This project uses Python and OpenCv to decode Morse Code messages transmitted through flashes(bursts) of light.

Learn more about morse code from here : https://en.wikipedia.org/wiki/Morse_code
Learn more about morse code tree representation from here : http://www.cranburyscouts.org/MorseTree.htm

The idea behind this project is to help navy or ships in general to detect flashes of light originating from any location at night time, and decode the morse code underneath it.

CURRENT LIMITATION - Since this project was originally intended to operate at night time, the code works on a relatively darker background with one bright source of illumination.

OpenCV is used detect the location of light source present in a scene. After the location has been determined, intermediate time units for both <b>light_time</b> (i.e. the time or the number of frames for which the light source was ON) and <b>dark_time</b> (i.e. the time or the number of frames for which the light source was OFF) are used to detect dots,dashes, inter-word pause and inter-sentence pause.

The morse code sequence is then decoded using the classic morse code tree represenattion.

Package requirements
---------------------
1. NumPy
2. OpenCV


HOW TO USE:
----------------

Inside main.py file mention the path of the video file to path variable.

---Provide threshold values as input----
Provide value to light_min_thresh variable (this is 1 unit of light ON time. And this value will vary depending upon your video.)

Provide values to dark_min_thresh, dark_med_thresh, dark_max_thresh (these are units of light OFF time. These stand for inter-charcater gap. inter-word gap and inter-sentence gap respectively.And these values will vary depending upon your video. )

If you are not sure what the threshold values should be, keep the default values and execute the code. And the observe the output of "light times" list and "dark times" list. It will give you an idea for the threshold values. Provide the updated threshold values and re execute teh code to get the correct morse code message and the decoded message.

FUTURE WORK
----------------
This project has been developed under the assumption that light houses and other naval vechicles use a light source with fixed light ON and light OFF time durations. 

But this may not work if the time durations vary. (Ex: A lone surviover stranded on an island and using a falshlight)

Future work may include a decode algorithm which will ahndle to above mentioned case.

