import mysql.connector

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Bvp@2723",  # your password
                     db="learningschema")        # name of the data base
if (db.is_connected()):
    print("Connected")
else:
    print("Not connected")

cursor = db.cursor()

insertdata = """INSERT INTO learningschema.calendar_table(CalendarDate,CalendarDay, CalendarMonth, CalendarQuarter, CalendarYear, 
CalendarTimehrmmss, DayOfWeekNum, HolidayName, HolidayFlag)
VALUES ('2022-11-22', 'Tuesday', 'November', 4, '2022', '234644', 47, ' ', ' ')"""

try:
   # Executing the SQL command
   cursor.execute(insertdata)

   # Commit your changes in the database
   db.commit()

except:
   # Rolling back in case of error
   db.rollback()

db.close()

