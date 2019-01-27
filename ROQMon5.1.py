#  Customer Support Reachout Queue Monitor  #
#  Ver 1.0 - 2018-09-11                     #
#  Author(s):  Joel Steen, Dan Stamper      #
#  MEDHOST, Inc                             #
#  Purpose:  To monitor Reach Out Queue     #
#       tool for events that have not been  #
#       marked as being worked.             #

#Setup
import os
import sys
import MySQLdb as db
import RPi.GPIO as GPIO
import time
import logging
import logging.handlers
import myClass

##Testing Setup Only
import random
##End Testing Setup


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# create logger
rolog = logging.getLogger()

#setup logging to file
rorotate = logging.handlers.TimedRotatingFileHandler('/home/pi/ROQLog.log',when='midnight', backupCount=3, encoding=None, delay=False, utc=False, atTime=None)
rorotate.setLevel(logging.DEBUG)
fileformatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rorotate.setFormatter(fileformatter)
rolog.addHandler(rorotate)


class indChannel:
    #Active Low relay switches activate at low power and deactivate at high power.
    #    ActPwrState = 0 if ActiveLowPower (like Andruino compatible relay switches) or 1 if ActiveHighPower (like a normal LED)
    
    def __init__(self, channel, actPwrState):
        self.channel = channel
        self.actPwrState = actPwrState
        GPIO.setup(channel, GPIO.OUT)

    def pwrOn(self):
        if self.actPwrState == 0:
            GPIO.output(self.channel, GPIO.LOW)
        else:
            GPIO.output(self.channel, GPIO.HIGH)

    def pwrOff(self):
        if self.actPwrState == 0:
            GPIO.output(self.channel, GPIO.HIGH)
        else:
            GPIO.output(self.channel, GPIO.LOW)

    def lightFlash(self, interval, repeats):
        print("flash settings: interval - "+str(interval)+", repeats - "+str(repeats))
        if repeats < 1:
            return
        else:
            for i in range(0, repeats):
                self.pwrOn()
                ##logging.debug("flash: ON")
                time.sleep(interval)
                self.pwrOff()
                ##logging.debug("flash: OFF")
                time.sleep(interval)
            return
	

#DB connection function
def dbConnection():
    for i in range(0, 10):                           #try to reconnect 10 times, then exit if unsuccessful
        try:                       
            conn = db.connect(host="",       #Reachout Queue db host
                              user="",          #Connection information provided by Bryan Conn
                              port="",
                              passwd="",    #user password
                              db="",            #db name
                              connect_timeout=5,		#connection timeout interval
                              read_timeout=10)     		#Query Timeout   
            if (conn):
                return conn
            else:
                time.sleep(5)                      #retry after 30 seconds
                continue

        except db.DatabaseError as e:
            logging.error(str(e))
            qInd.pwrOff()    #turn off RO Event indicator
            ##print("OFF: qInd - Database Error")
            dbInd.pwrOn()    #turn on problem indicator steady
            ##print("ON: dbInd - Database Error")
            continue
    else:
        logging.critical("Failed to connect to Reach Out Queue database.  Exiting.")
        os._exit(0)      #This allows all threads running the script to end otherwise the script could loop.




##test connection close
def randomClose(conn):
    #from random import randint
    ranFlag = random.randint(0,5)
    if (ranFlag >= 0):
        print("test - randomly closed db connection")
        conn.close()
    return



#Initialize indicators and set to initial power state
qInd = indChannel(16,0)     #Queue Indicator attached to ActiveLowPower relay switch.  Initial state is OFF.
##qInd = indChannel(7,1)      ## Green LED Indicator alternative for queue monitoring
dbInd = indChannel(11,1)    #Simple LED.  Initial State is OFF.
qInd.pwrOff()
##print("OFF: qInd, ch: "+str(qInd.channel)+", actPwrState: "+str(qInd.actPwrState))
dbInd.pwrOff()
##print("OFF: dbInd, ch: "+str(dbInd.channel)+", actPwrState: "+str(dbInd.actPwrState))
conn=dbConnection()
try:
	while conn.open:
		try:
			dbhandler=conn.cursor()
			dbhandler.execute("SELECT * FROM Event where Department = 2 and Status = 1")
			result=dbhandler.fetchone()
			if result is not None:
				qInd.pwrOn()
				logging.info("ON:  qInd - event(s) available")
			else:
				qInd.pwrOff()
				logging.info("OFF:  qInd - no event(s) available")
			dbhandler.close()
			time.sleep(5)
		except Exception as err:
			logging.error("Checking Connection to DB: Query took longer than 10 seconds")
			qInd.pwrOff()
			##logging.error("OFF:  qInd - lost connection to db")
			dbInd.lightFlash(0.5,2)
			##logging.error("FLASH:  dbInd - lost connection to db")
			conn=dbConnection()

except KeyboardInterrupt:
	print("\nQuitting ROQMonitor.py")
	qInd.pwrOff()
	dbInd.pwrOff()
	GPIO.cleanup()
	os._exit(0)