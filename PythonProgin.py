#Setting up Life
import sys
import psycopg2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

counter=0

while 1:
        conn = None

        try:
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(7, GPIO.OUT)
                conn = psycopg2.connect("dbname = 'DBNAME' user = 'USERNAME' password='PASSWORD'")
                curs = conn.cursor()
                curs.execute("SELECT * from TABLENAME")
                row = curs.fetchone()
                if row is not None:
                        print('ON')
                        GPIO.output(7,True)
                        time.sleep(10)
                else:
                        print('OFF')
                        GPIO.output(7,False)
                        time.sleep(10)
                GPIO.cleanup()
                conn.close()

        except psycopg2.DatabaseError, e:
                print e