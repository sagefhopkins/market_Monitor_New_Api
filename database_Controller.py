import mysql.connector

#Initializes database connection and returns connection to function caller
def database_Connect():
    connection = mysql.connector.connect(host='107.181.191.59', user='root', passwd='P@$$06281a', database='cur_Monitor')

    return connection

def checkTableExists(tablename):
    sql = database_Connect()
    cur = sql.cursor()
    query = "SELECT * FROM information_schema.tables WHERE table_schema = 'cur_Monitor' AND table_name = '{0}' LIMIT 1".format(tablename)
    cur.execute(query)
    if not cur.fetchone():
        return False
    else:
        return True


#Creates new tables into the database, this will always use the same format
#to ensure uniformity between tables
def database_Table_Commodity(name):
    sql = database_Connect()
    cur = sql.cursor()
    query = "CREATE TABLE `{0}` (`commodity` text, `state` text, `min` float, `med` float, `max` float, `date` date)".format(name)
    cur.execute(query)
    print (name + '_Commodity table created!')
def database_Table_Currency(name):
    sql = database_Connect()
    cur = sql.cursor()
    query = "CREATE TABLE `{0}` (`ticker` text, `price` float, `time` timestamp)".format(name)
    cur.execute(query)
    print (name + '_Currency table created!')

def database_Table_Stock(name):
    sql = database_Connect()
    cur = sql.cursor()
    query = "CREATE TABLE `{0}` (`ticker` text, `price` float, `time` timestamp)".format(name)
    cur.execute(query)
    print (name + '_Stock table created!')

def insert_Currency(ticker, price, time):
    try:
        if checkTableExists(ticker + '_Currency') != False:
            sql = database_Connect()
            cur = sql.cursor()
            query = "INSERT INTO `{0}` VALUES(%s, %s, %s)".format(ticker + '_Currency')
            cur.execute(query, (ticker, price, time))
        else:
            sql = database_Connect()
            cur = sql.cursor()
            database_Table_Currency(ticker + '_Currency')
            query = "INSERT INTO `{0}` VALUES(%s, %s, %s)".format(ticker + '_Currency')
            cur.execute(query, (ticker, price, time))
    except():
        pass
        print 'Error occurred databasing!'
def insert_Commodity(commodity, state, min, med, max, date):
    try:
        if checkTableExists(commodity + '_Commodity') != False:
            sql = database_Connect()
            cur = sql.cursor()
            query = "INSERT INTO `{0}` VALUES (%s, %s, %s, %s, %s, %s)".format(commodity + '_Commodity')
            cur.execute(query, (commodity, state, min, med, max, date))
        else:
            sql = database_Connect()
            cur = sql.cursor()
            database_Table_Commodity(commodity + '_Commodity')
            query = "INSERT INTO `{0}` VALUES(%s, %s, %s, %s ,%s ,%s)".format(commodity + '_Commodity')
            cur.execute(query, (commodity, state, min, med, max, date))
    except():
        pass
        print 'Error Occurred databasing!'

def insert_Stock(ticker, price, time):
    try:
        if checkTableExists(ticker + '_Stock') != False:
            sql = database_Connect()
            cur = sql.cursor()
            query = "INSERT INTO `{0}` VALUES(%s, %s,%s);".format(ticker + '_Stock')
            print query
            cur.execute(query,(ticker, price, time))
        else:
            sql = database_Connect()
            cur = sql.cursor()
            database_Table_Stock(ticker + '_Stock')
            query = "INSERT INTO `{0}` VALUES(%s, %s,%s);".format(ticker + '_Stock')
            cur.execute(query, (ticker, price, time))
    except():
        pass
        print 'Error occurred databasing!'

#Queries the table, and returns all values which either match or include the
#name string in their overall value
def database_Read(table, currency):
    sql = database_Connect()
    cur = sql.cursor()
    query = "SELECT * FROM " + table + " WHERE currency LIKE '" + currency + "%'"
    for row in cur.execute(query):
        return row

#Allows the ordering of table read outs to help allow users to view data better
def database_Order(table, order):
    sql = database_Connect()
    cur = sql.cursor()
    query = "SELECT * FROM " + table + " ORDER BY " + order
    for row in cur.execute(query):
        print row
