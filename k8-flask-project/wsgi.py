import psutil
from flask import Flask, render_template

app = Flask(__name__);

@app.route("/")
def index():

    cpu_metric = psutil.cpu_percent();
    mem_metric = psutil.virtual_memory().percent;
    message = "";

    if((cpu_metric>70) or (mem_metric < 70)):
        message = "Cpu consumption is high please take action !!!!";
    elif((cpu_metric<70) or (mem_metric > 70)):
        message = "Memory consumption is high please take action !!!!";
    else:
        message = "Memory consumption under control!!!!";
    data = {"cpu_metric": cpu_metric, "mem_metric": mem_metric, "message": message}
    return render_template("index.html", data=data);

if __name__ == "__main__":
    app.run(debug=True);
    
