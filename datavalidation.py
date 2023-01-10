from flask import Flask, request
from datetime import date, time, datetime
import mysql.connector
from mysql import connector
from credentials import DBcredential
app = Flask(__name__)

DBcredential['username'] 

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                    user=DBcredential['username'] ,         # your username
                    passwd=DBcredential['password'] ,  # your password
                    db="learningschema")        # name of the data base
cursor = db.cursor()
if (db.is_connected()):
    print("Connected")
else:
    print("connection failed")
sql_insert = "INSERT INTO learningschema.event_table(EventTitle, EventDescription, StatusFlag, EventDate, Event_link, USER_ID) VALUES ( %s, %s, %s, %s, %s, %s)"

@app.route('/datevalidation')
def datavalidation():
    inputuserid = request.args.get('user')
    inputdate = request.args.get('date')
    print(inputdate)
    inputtime = request.args.get('time')
    inputevent = request.args.get('eventname')
    inputdescription = request.args.get('event_description')
    inputuser = request.args.get('username')
    currentdate = str(date.today())

    valid_date = True
    try:
        date_valid = bool(datetime.strptime(inputdate, "%Y-%m-%d"))
        time_valid = bool(datetime.strptime(inputtime, "%H:%M:%S"))
    except ValueError as e:
        valid_date = False
    if valid_date == False:
        return("Either date or time is not in valid format, Please use %Y-%m-%d and %H:%M:%S" )
              
    if inputdate >= currentdate:
        if '00:00:00' <= inputtime <= '23:59:59':
            return dbinsert(inputdate, inputevent, inputdescription, inputuser, inputuserid)
        else:        
            return('validtaion of time failed')
    else:
        return 'Invalid date'
    
    
#connecting to database  
def dbinsert(inputdate, inputevent, inputdescription, inputuser, inputuserid):
   
    try:
        print (sql_insert)
        cursor.execute(sql_insert, (inputevent, inputdescription, 0, inputdate, "", inputuserid))                
        db.commit()
        status = "Data inserted"
    except Exception as e:
        print(str(e))
        db.rollback()
        status = "Data insertion failed"
    return(status)

@app.route("/findevent")
def findevent():
    row = ''
    finduser = request.args.get('user')
    findtodate = request.args.get('todate')
    findfromdate = request.args.get('fromdate')
         
#Validation of request
    try:
        valid_date_01 = bool(datetime.strptime(findtodate, "%Y-%m-%d"))
        valid_date_02 = bool(datetime.strptime(findfromdate, "%Y-%m-%d"))
    except ValueError as e:
        valid_date_01 = False
        valid_date_02 = False
    if valid_date_01 and valid_date_02 == True:
        sql_query = "select EventID, EventTitle, EventDescription, EventDate from event_table where USER_ID = '" + finduser + "' and date(EventDate) >= '" + findfromdate + "' and date(Eventdate) <= '" + findtodate +"'"
        print(sql_query)
        cursor.execute(sql_query)
        row = cursor.fetchall()
        return(row)
    else:
        return ("Please enter valid date in format yyyy-mm-dd")  

# find date To-From with no event name
    

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5000, debug = True)


