# Raspberry Pi Hardware Usages
Provides real time percentages of cpu, memory, disk, and temperature of raspberry pi device (Unix based) through a web interface.

![raspberrypi hardware usages](http://i.imgur.com/nd0FLUR.png)

## Motivation
- Wanted an easy way of accessing my raspberry pi hardware usages without opening an ssh shell and easily accessible through my phone. 
- Consdered a web administration tool like webmin however after installing and running, it would use up half of my raspberry pi memory.
- Decided to implement a lightweight web interface that leverages REST through a micro framework called Flask.

## Used Libraries
- Flask (A Python Microframework) - http://flask.pocoo.org/
- jQuery Knob (jQuery dial) - http://anthonyterrien.com/demo/knob/

## Tech Stack
- Flask, jQuery, Ajax, JS, Unix Shell, HTML5, CSS

## Setup

1. Install Python 2.7
- sudo apt-get install python

2. Install Flask
- pip install Flask

4. Modify CONFIG file
- Change host and port if necessary

3. Run the micro web service
- py run.py

Access via http://HOST:PORT (as configured in CONFIG file)




