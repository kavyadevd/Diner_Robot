#!/usr/bin/python

import sys
import sim as sim # Import Coppeliasim
import time

sim.simxFinish(-1) # cose open connections if any

clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5) # connect to CoppeliaSim
if clientID!=-1:
    print ("Connection successful")
	
    emptyBuff = bytearray()

    #Start the simulation:
    sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot_wait)
    time.sleep(3)
    res,robotHandle=sim.simxGetObjectHandle(clientID,'UR5#',sim.simx_opmode_oneshot_wait)  
    print(robotHandle)
    sim.simxStopSimulation(clientID, sim.simx_opmode_oneshot_wait)

else:
    print("Connection failed")
sys.exit("Exiting")
