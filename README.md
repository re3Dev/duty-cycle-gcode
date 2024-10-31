***USAGE***

DUTY_CYCLE - Turns on motor for 2 seconds every 30 seconds


DUTY_CYCLE_OFF - Stops duty cycle


*Make sure to give files proper permissions. 

1. SSH into pi
2. Clone repo <code> git clone https://github.com/re3Dev/duty-cycle-gcode </code>
3. Move files <code> sudo mv duty-cycle-gcode/duty-cycle.py /home/pi/duty-cycle.py && sudo mv duty-cycle-gcode/duty_cycle.sh /usr/local/bin/duty_cycle.sh && sudo mv duty-cycle-gcode/duty_cycle_off.sh /usr/local/bin/duty_cycle_off.sh && sudo mv duty-cycle-gcode/macros.cfg /home/pi/printer_data/config/macros.cfg</code>
4. File permissions <code> sudo chmod +x /usr/local/bin/duty_cycle.sh && sudo chmod +x /usr/local/bin/duty_cycle_off.sh && sudo chmod +x duty-cycle.py && sudo chown pi:pi /home/pi/printer_data/config/macros.cfg </code>
