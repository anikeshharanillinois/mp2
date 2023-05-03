from flask import Flask, request
import subprocess
import socket
import stress_cpu
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/',methods = ['POST'])
def run_stress_cpu():
   p = subprocess.Popen(["python3", "/home/ubuntu/strees_cpu.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
   output, errors = p.communicate()
   print(output)

@app.route('/',methods = ['GET'])
def get_seed():
   myHostName = socket.gethostname()
   myIP = socket.gethostbyname(myHostName)
   return str(myIP)

if __name__ == '__main__':
   #run_stress_cpu()
   app.run(host='0.0.0.0',debug = True)