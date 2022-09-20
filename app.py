from flask import Flask, request, jsonify

import mysql.connector

from cloudevents.http import from_http

app = Flask(__name__)


# create an endpoint at http://localhost:/3000/
@app.route("/", methods=["POST"])
def home():
    # create a CloudEvent
    event = from_http(request.headers, data=request.get_data())

    bdata=event.data
    conn = mysql.connector.connect(
   user='root', password='root', host='127.0.0.1', database='sample'
)

    cur = conn.cursor()

   # cmd="INSERT INTO batteryalerts (id,datetime,batteryVoltage) values (223,'2020-01-01 10:10:10',2898)"



    id = bdata[1]

    dt = bdata[3]

    volt=bdata[5]['batterydata']['voltage']



    cmd=f"INSERT INTO batteryalerts (id,datetime,batteryVoltage) values ('{id}','{dt}','{volt}')"
    cur.execute(cmd)
    conn.commit()
    conn.close()
    print(bdata)




    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=7000)

