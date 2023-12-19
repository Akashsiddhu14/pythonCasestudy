import mysql.connector as sql

class DBConnection:
    @staticmethod
    def getConnection():
        try:
            conn=sql.connect(host='localhost',database='casestudy',user='root',password='akash1436')
            s=conn.cursor()
            print("Database is connected")
        except Exception as e:
            print(str(e) + "---Database is not Connected:--")