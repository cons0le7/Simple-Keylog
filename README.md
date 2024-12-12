# Simple Keylog
A streamlined keylogger for Linux systems written in shell.

# How to use: 

- Keep "decoder.py" and "sentencer.py" on your servers machine where the logs will be saved. Only "keylog.sh" will need to be planted on target host. 
- Edit "keylog.sh" in text editor of choice. 
- replace the upload interval with your desired amount in seconds. 
- Replace "http://yourserver.com/upload" with your own upload server url.
- Copy "keylog.sh" to target's machine, open terminal, cd to directory of "keylog.sh" and grant executable permissions using:
```
chmod +x keylog.sh
```
- then execute:
```
./keylog.sh
```
- "logs.txt" will upload to your server and update every X number of seconds according to your specification.
- Move "decoder.py" and "sentencer.py" to the same directory of server as "logs.txt" or create a new folder and add all files to it.
- cd to directory where the files are contained and you can either run:
```
python3 decoder.py 
```
- This will convert the captured logs into a user-readable format and output the converted version as "logs_decoded.txt" in the same directory. This version will include all the key presses and releases but may not be as readable.
- Or you can run
```
python3 sentencer.py
```
- This will convert the captured logs into an even more user-readable format and output the converted version as "logs_sentenced.txt" in the same directory. This version will be in a sentence-like format but will exclude key releases.
  
