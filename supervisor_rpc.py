#!/usr/bin/python
#-*- coding: UTF-8 -*-
import xmlrpclib


def get_all_process_info(rpc):
    server = xmlrpclib.Server(rpc)
    return server.supervisor.getAllProcessInfo()

def restart_all_process(**kwargs):
    server = xmlrpclib.Server(kwargs.get('rpc'))
    server.supervisor.stopAllProcesses()
    server.supervisor.startAllProcesses()

def stop_all_process(**kwargs):
    server = xmlrpclib.Server(kwargs.get('rpc'))
    server.supervisor.stopAllProcesses()

def stop_process(**kwargs):
    rpc = kwargs.get('rpc')
    server = xmlrpclib.Server(rpc)
    server.supervisor.stopProcess(kwargs.get('process_name'))

def restart_process(**kwargs):
    process_name = kwargs.get('process_name')
    server = xmlrpclib.Server(kwargs.get('rpc'))
    res = server.supervisor.getProcessInfo(process_name)
    # code 20 means the process is running
    if res['state'] == 20:
        server.supervisor.stopProcess(process_name)
    server.supervisor.startProcess(process_name)

def start_process(**kwargs):
    server = xmlrpclib.Server(kwargs.get('rpc'))
    server.supervisor.startProcess(kwargs.get('process_name'))

def clear_process_log(**kwargs):
    server = xmlrpclib.Server(kwargs.get('rpc'))
    server.supervisor.clearProcessLogs(kwargs.get('process_name'))

def tail_process_log(**kwargs):
    server = xmlrpclib.Server(kwargs.get('rpc'))
    temp = server.supervisor.tailProcessStdoutLog(kwargs.get('process_name'), 0, 999)
    return temp[0].encode("utf-8").replace('\n', '\r\n')
