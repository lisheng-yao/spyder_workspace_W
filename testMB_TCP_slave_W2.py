# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 08:32:34 2023

@author: w
"""

from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusSocketFramer

num_slaves = 6
register_size = 10000

def create_slave_context(register_size):
    
    return ModbusSlaveContext( 
        
        di = ModbusSequentialDataBlock(0 , [0] * register_size),
        co = ModbusSequentialDataBlock(0 , [0] * register_size),
        hr = ModbusSequentialDataBlock(0 , [0] * register_size),
        ir = ModbusSequentialDataBlock(0 , [0] * register_size)
        
        
        )

def create_server_context(num_slaves , register_size):
    
    slaves = {slave_id: create_slave_context(register_size) for slave_id in range(1, num_slaves+1)}
    return ModbusServerContext(slaves=slaves, single=False)


context = create_server_context( num_slaves , register_size )


tcp_params = {
    
    'address' : ("192.168.3.200" , 502)
    
    }

StartTcpServer(context , framer= ModbusSocketFramer , **tcp_params)