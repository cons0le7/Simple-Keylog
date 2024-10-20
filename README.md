# Simple Keylog
A very streamlined keylogger for Linux systems written in shell.

#How to use: 

- Edit "simple_keylog.sh" in notepad.
- replace the upload interval with your desired amount in seconds. 
- Replace "http://yourserver.com/upload" with your own upload server url.
- Run "simple_keylog.sh" on target host.
- "logs.txt" will upload to your server and update every X number of seconds according to your specification.
- Move "log_converter.py" to the same directory of server as "logs.txt" or create a new folder and add both files to it.

- Run:
```
python3 log_converter.py 
```
- This will convert the captured logd into a user-readable format and output the coonverted version as "logs_converted.txt" in the same directory. 
