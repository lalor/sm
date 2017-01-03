#!/usr/bin/python
#-*- coding: UTF-8 -*-

RPC_FORMAT = "http://{user}:{password}@{ip}:{port}/RPC2"

def format_rpc(host):
    return RPC_FORMAT.format(user=host.username,
            password=host.password,
            ip=host.ip_address,
            port=host.port)
