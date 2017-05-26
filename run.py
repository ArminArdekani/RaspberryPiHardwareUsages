from flask import Flask, jsonify, make_response, render_template
app = Flask(__name__)
import subprocess, json
from CONFIG import *

@app.route("/")
def getHomePage():
    return render_template('index.html')

@app.route("/getCpuUsage")
def getCpuUsage():
    cpu_command = subprocess.check_output(['top -bn1 | grep "Cpu(s)"'], shell=True)
    cpu_usage = int(100 - float(cpu_command[cpu_command.index("ni, ")+4:cpu_command.index(" id,")]))
    return json.dumps({"percentage": cpu_usage});
    
@app.route("/getMemoryUsage")
def getMemoryUsage():
    memory_usage = int(float(subprocess.check_output(["free | awk 'FNR == 3 {print $3/($3+$4)*100}'"], shell=True)))
    return json.dumps({"percentage": memory_usage});
    
@app.route("/getDiskUsage")
def getDiskUsage():
    disk_usage = int(float(subprocess.check_output(["df -P / | awk '/%/ {print $5-0}'"], shell=True)))
    return json.dumps({"percentage": disk_usage});
    
@app.route("/getTemperatureUsage")
def getTemperatureUsage():
    cpu_temperature = int(float(subprocess.check_output(["cat /sys/class/thermal/thermal_zone0/temp"], shell=True))/1000)
    return json.dumps({"percentage": cpu_temperature});
    
if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG);
