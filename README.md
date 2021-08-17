# 1984-Bot
Silence political dissidents with your very own 1984 Bot. Many restrictions apply because I don't know JavaScript.



Requirements:

JS ES6

 -Node
 
 -python-shell
 
 
Python 3.7

 -NLTK
 
 -Pickle
 
 -pyttsx3
 
 -speech_recognition




How to use:

1. Edit bot.js with the appropriate user IDs, guild IDs, and text channel IDs.

2. Edit PythonShell options in bot.js with the appropriate path to python.exe and path to judgment.py script.

3. Add the bot to your server.

4. Use command *join to have the bot join your voice channel.

5. Use command *record to have the bot record speech for designated user. 

6. After desired speech has been recorded, use command *stop to end and save the recording.
    - Please note that the recording seems to take some additional time after speech has concluded to finish recording.
    
7. Use command *judge to have the bot analyze speech file and deliver judgment.


I haven't tested this too much, and it may be possible to record and analyze multiple users at once, but with the delay recording only one I decided not to add this, you can if you want. 
