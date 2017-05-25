from flask import Flask
from flask import jsonify, make_response
app = Flask(__name__)
import commands

@app.route("/")
def main():
    cpu_usage = commands.getstatusoutput("top -bn1 | grep \"Cpu(s)\" | \ sed \"s/.*, *\([0-9.]*\)%* id.*/\1/\" | \ awk '{print 100 - $1"%\"}'")
    memory_usage = commands.getstatusoutput("free | awk 'FNR == 3 {print $3/($3+$4)*100}'")
    print cpu_usage + "," + memory_usage

if __name__ == "__main__":
    app.run(host='192.168.0.99', port=1337, debug=True)
