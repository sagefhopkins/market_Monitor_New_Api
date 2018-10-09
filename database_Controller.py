import sqlite3

#Initializes database connection and returns connection to function caller
def database_Connect():
    connection = sqlite3.connect('cur_Monitor.db')

    return connection

def checkTableExists(tablename):
    sql = database_Connect()
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name='{0}'".format(tablename)
    if not sql.execute(query).fetchone():
        return False
    else:
        return True


#Creates new tables into the database, this will always use the same format
#to ensure uniformity between tables
def database_Table_Commodity(name):
    sql = database_Connect()
    query = "CREATE TABLE `{0}` (`id` INTERGER PRIMARY KEY, `commodity` text, `state` text, `min` float, `med` float, `max` float, `date` date)".format(name)
    sql.execute(query)
    sql.commit()
    print (name + '_Commodity table created!')
def database_Table_Currency(name):
    sql = database_Connect()
    query = "CREATE TABLE `{0}` (`id` INTERGER PRIMARY KEY, `ticker` text, `price` float, `time` timestamp)".format(name)
    sql.execute(query)
    sql.commit()
    print (name + '_Currency table created!')

def database_Table_Stock(name):
    sql = database_Connect()
    query = "CREATE TABLE `{0}` (`id` INTERGER PRIMARY KEY, `ticker` text, `price` float, `time` timestamp)".format(name)
    sql.execute(query)
    sql.commit()
    print (name + '_Stock table created!')

def insert_Currency(ticker, price, time):
    try:
        if checkTableExists(ticker + '_Currency') != False:
            sql = database_Connect()
            query = "INSERT INTO `{0}` VALUES(NULL, ?, ?, ?)".format(ticker + '_Currency')
            sql.execute(query, (ticker, price, time))
            sql.commit()
        else:
            sql = database_Connect()
            database_Table_Currency(ticker + '_Currency')
            query = "INSERT INTO `{0}` VALUES(NULL, ?, ?, ?)".format(ticker + '_Currency')
            sql.execute(query, (ticker, price, time))
            sql.commit()
    except():
        pass
        print 'Error occurred databasing!'
def insert_Commodity(commodity, state, min, med, max, date):
    try:
        if checkTableExists(commodity + '_Commodity') != False:
            sql = database_Connect()
            query = "INSERT INTO `{0}` VALUES (NULL, ?, ?, ?, ?, ?, ?)".format(commodity + '_Commodity')
            sql.execute(query, (commodity, state, min, med, max, date))
            sql.commit()
        else:
            sql = database_Connect()
            database_Table_Commodity(commodity + '_Commodity')
            query = "INSERT INTO `{0}` VALUES(NULL, ?, ?, ?, ? ,? ,?)".format(commodity + '_Commodity')
            sql.execute(query, (commodity, state, min, med, max, date))
            sql.commit()
    except():
        pass
        print 'Error Occurred databasing!'

def insert_Stock(ticker, price, time):
    try:
        if checkTableExists(ticker + '_Stock') != False:
            sql = database_Connect()
            query = "INSERT INTO `{0}` VALUES(NULL, ?, ?, ?)".format(ticker + '_Stock')
            sql.execute(query, (ticker, price, time) )
            sql.commit()
        else:
            sql = database_Connect()
            database_Table_Stock(ticker + '_Stock')
            query = "INSERT INTO `{0}` VALUES(NULL, ?, ?, ?)".format(ticker + '_Stock')
            sql.execute(query, (ticker, price, time))
            sql.commit()
    except():
        pass
        print 'Error occurred databasing!'

#Queries the table, and returns all values which either match or include the
#name string in their overall value
def database_Read(table, currency):
    sql = database_Connect()
    query = "SELECT * FROM " + table + " WHERE currency LIKE '" + currency + "%'"
    for row in sql.execute(query):
        return row

#Allows the ordering of table read outs to help allow users to view data better
def database_Order(table, order):
    sql = database_Connect()
    query = "SELECT * FROM " + table + " ORDER BY " + order
    for row in sql.execute(query):
        print row
