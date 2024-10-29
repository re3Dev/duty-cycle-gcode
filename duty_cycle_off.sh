#!/bin/bash


PID=$(pgrep -f duty_cycle.py)

if [ -z "$PID" ]; then
    echo "No running instance of duty_cycle.py found."
else
    kill "$PID"
    echo "Stopped duty_cycle.py with PID $PID."
fi