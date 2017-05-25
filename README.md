# Raspberry Pi Hardware Usages
Provides real time percentages of cpu, memory, disk, and temperature of raspberry pi device (Unix based) through a micro web service.

![raspberrypi hardware usages](http://i.imgur.com/nd0FLUR.png)

## Motivation
- Wanted an easy way of accessing my raspberry pi hardware usages without opening an ssh shell and easily accessible through my phone. 
- Consdered a web administration tool like webmin however after installing and running, it would use up half of my memory.
- Decided to implement a lightweight micro web service using Flask to drive this.

## Used Libraries
- Flask (A Python Microframework) - http://flask.pocoo.org/
- jQuery Knob (jQuery dial) - http://anthonyterrien.com/demo/knob/

## Tech Stack
- Flask, jQuery, Ajax, JS, Unix Shell, HTML5, CSS.

## Setup

1. Install Python 2.7
- sudo apt-get install python

2. Install Flask
- pip install Flask

4. Modify host and port of micro web service in last line of run.py
- app.run(host='{IP_ADDRESS}', port={AVAILABLE_PORT}, debug=False)

3. Run the micro web service
- py run.py

Access via http://{IP_ADDRESS}:{AVAILABLE_PORT}




