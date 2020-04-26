# piDust
Raspberry Pi controlled servo blast gates for my dust collection system

This RPi script accespts MQTT messages from other devices (esp32/8266 etc) in the form of a tool selection string, and then sends PWM commands to the servos controlling a series of blast gates. These blast gates open or close tubing from one tool back to the dust collector fan/cyclone. The definitions for which blastgates need to be opened/closed to service a tool are populated herein. 
