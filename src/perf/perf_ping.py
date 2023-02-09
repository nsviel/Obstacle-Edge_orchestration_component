#---------------------------------------------
from src.param import param_hu
from src.misc import specific

import datetime
import time
import os


#TODO: refaire cette function

def compute_ping(list_latency, list_reliability):
    data = make_ping()
    compute_timestamp()
    compute_latency(data, list_latency)
    compute_reliability(data, list_reliability)

def make_ping():
    ip = param_hu.state_hu["pywardium"]["ip"]
    os.system("ping -c 50 -i 0.002 -t 1 " + ip + " > src/perf/ping 2>/dev/null")
    with open('src/perf/ping', 'r') as file:
        data = file.read().rstrip()
    return data

def compute_timestamp():
    timestamp = time.time()
    param_hu.state_perf["cloud_local"]["timestamp"] = timestamp

def compute_latency(data, list_latency):
    if(param_hu.state_hu["pywardium"]["http_connected"] == True):
        id_b = data.find("time=") + 5
        id_e = data.find(" ms")
        latency = float(data[id_b:id_e])
        specific.list_stack(list_latency, latency, 10)

        param_hu.state_perf["cloud_local"]["latency"]["value"] = latency
        param_hu.state_perf["cloud_local"]["latency"]["min"] = min(list_latency)
        param_hu.state_perf["cloud_local"]["latency"]["max"] = max(list_latency)
        param_hu.state_perf["cloud_local"]["latency"]["mean"] = specific.mean(list_latency)

def compute_reliability(data, list_reliability):
    if(param_hu.state_hu["pywardium"]["http_connected"] == True):
        packetloss = float([x for x in data.split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])
        reliability = 100 - packetloss
        specific.list_stack(list_reliability, reliability, 10)

        param_hu.state_perf["cloud_local"]["reliability"]["value"] = reliability;
        param_hu.state_perf["cloud_local"]["reliability"]["min"] = min(list_reliability)
        param_hu.state_perf["cloud_local"]["reliability"]["max"] = max(list_reliability)
        param_hu.state_perf["cloud_local"]["reliability"]["mean"] = specific.mean(list_reliability)
