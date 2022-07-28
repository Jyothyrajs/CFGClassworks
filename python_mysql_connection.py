import mysql.connector
from config import HOST,USER,PASSWORD

# We will practice how to connect python to  mysql
mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD)
# mydb = mysql.connector.connect(
# host = "localhost",
# user = "root",
# password = "databasepassword"
# )
print(mydb)
# User-defined exception for database connection error

class DbConnectionError(Exception):
    pass

# Connect to db
def connect_db(db_name):
        context = mysql.connector.connect(host=HOST,
                                          user=USER,
                                          password=PASSWORD,
                                          database=db_name)
        return context

# def connect_db(db_name):
#         context = mysql.connector.connect(host="localhost",
#                                      user="root",
#                                      password="databasepassword", database=db_name)
#         return context

# Query all records
def get_all():
    try:
        testsdb = connect_db(("tests"))
        mycursor = testsdb.cursor()
        mycursor.execute("SELECT * FROM abcreport")
        result = mycursor.fetchall()
        for order in result:
            print(order[1])
    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if testsdb:
            testsdb.close()
            print('Connection closed')

# Query with condition
def get_by_region(mregion):
    try:
        testsdb = connect_db(("tests"))
        mycursor = testsdb.cursor()
        stmt = "SELECT * FROM abcreport WHERE Region='{}'".format(mregion)
        mycursor.execute(stmt)
        # mycursor.execute(f"SELECT * FROM abcreport WHERE Region='{mregion}'")
        result = mycursor.fetchall()
        for order in result:
            print(order[1])
    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if testsdb:
            testsdb.close()
            print('Connection closed')


def calc_commission(result):
    sales = []
    for s in result:
        sales.append(s[1])
    return sum(sales) * 0.1

def get_commission(rep_name):
    try:
        testsdb = connect_db(("tests"))
        mycursor = testsdb.cursor()
        # stmt = f"SELECT SUM(Total) as Total_rep from abcreport GROUP BY Rep HAVINg Rep='{rep_name}'"
        stmt = "SELECt Rep,Total  from abcreport WHERE Rep = '{}'".format(rep_name)
        print(stmt)
        mycursor.execute(stmt)
        # mycursor.execute(f"SELECT * FROM abcreport WHERE Region='{mregion}'")
        result = mycursor.fetchall()
        for r in result:
            print(r)
        print(f"Commission for {rep_name} is {calc_commission(result)}")
    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if testsdb:
            testsdb.close()
            print('Connection closed')

# Insert data
record = {
    'OrderDate': '2020-12-15',
    'Region': 'Central',
    'Rep': 'John Doe',
    'Item': 'post-it-notes',
    'Units': 220,
    'UnitCost': 2.5,
    'Total': 220 * 2.5,
}
def insert_new_record(record):
    try:
        testsdb = connect_db(("tests"))
        mycursor = testsdb.cursor()
        insert_cmd = "INSERT INTO abcreport ({}) VALUES('{}','{}','{}','{}',{},{},{})".\
            format(','.join(record.keys()),
                   record['OrderDate'],
                   record['Region'],
                   record['Rep'],
                   record['Item'],
                   record['Units'],
                   record['UnitCost'],
                   record['Total']
                   )
        mycursor.execute(insert_cmd)
        testsdb.commit()
        print(f"Record inserted successfully {record['Rep']}")
    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if testsdb:
            testsdb.close()



def main():
    # get_all()
    # get_by_region('Central')
    get_commission('Andrews')
    insert_new_record(record)
if __name__ == "__main__":
    main()

