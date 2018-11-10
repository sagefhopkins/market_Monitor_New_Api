import mysql.connector

#Initializes database connection and returns connection to function caller
def database_Connect():
    connection = mysql.connector.connect(host='nope', user='nope', passwd='nope', database='cur_Monitor')

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
def database_Table_News(stock):
    sql = database_Connect()
    cur = sql.cursor()
    query = "CREATE TABLE `News_Data` (`stock` text,`keyword_Matches` text, `percentage` float, `title` text, `description` text, `url` text, `date` timestamp)"
    cur.execute(query)
    print ('Stock Market News Table Generated!')
def database_Table_Commodity(name):
    sql = database_Connect()
    cur = sql.cursor()
    query = "CREATE TABLE `Commodity_Data` (`commodity` text, `state` text, `min` float, `med` float, `max` float, `date` timestamp)"
    cur.execute(query)
    print ('Commodity Market Data Table Generated!')
def database_Table_Currency(name):
    sql = database_Connect()
    cur = sql.cursor()
    query = "CREATE TABLE `Currency_Data` (`ticker` text, `price` float, `date` timestamp)"
    cur.execute(query)
    print ('Currency Market Data Table Generated!')

def database_Table_Stock(name):
    sql = database_Connect()
    cur = sql.cursor()
    query = "CREATE TABLE `Stock_Data` (`ticker` text, `price` float, `date` timestamp)"
    cur.execute(query)
    print ('Stock Market Data Table Generated!')

def insert_News(stock ,keyword_Matches, percentage, title, description, url, time):
    try:
        if checkTableExists('News_Data') != False:

            sql = database_Connect()
            cur = sql.cursor()
            query = "INSERT INTO `News_Data` (`stock`, `keyword_Matches`, `percentage`, `title`, `description`, `url`, `date`) VALUES(%s, %s, %s, %s, %s, %s, %s);"
            cur.execute(query, (stock, str(keyword_Matches), float(percentage), str(title), str(description), str(url), time))
            sql.commit()
        else:
            sql = database_Connect()
            cur = sql.cursor()
            database_Table_News('News_Data')
            query = "INSERT INTO `News_Data` VALUES(%s, %s, %s, %s, %s, %s, %s);"
            cur.execute(query, (stock, str(keyword_Matches), float(percentage), str(title), str(description), str(url), time))
            sql.commit()
    except UnicodeEncodeError:
        pass
def insert_Currency(ticker, price, time):
    try:
        if checkTableExists('Currency_Data') != False:
            sql = database_Connect()
            cur = sql.cursor()
            query = "INSERT INTO `Currency_Data` VALUES(%s, %s, %s);"
            cur.execute(query, (ticker, price, time))
            sql.commit()

        else:
            sql = database_Connect()
            cur = sql.cursor()
            database_Table_Currency('Currency_Data')
            query = "INSERT INTO `Currency_Data` VALUES(%s, %s, %s);"
            cur.execute(query, (ticker, price, time))
            sql.commit()
    except():
        pass
        print 'Error occurred databasing!'
def insert_Commodity(commodity, state, min, med, max, date):
    try:
        if checkTableExists('Commodity_Data') != False:
            sql = database_Connect()
            cur = sql.cursor()
            query = "INSERT INTO `Commodity_Data` VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(query, (commodity, state, min, med, max, date))
            sql.commit()
        else:
            sql = database_Connect()
            cur = sql.cursor()
            database_Table_Commodity('Commodity_Data')
            query = "INSERT INTO `Commodity_Data` VALUES(%s, %s, %s, %s ,%s ,%s);"
            cur.execute(query, (commodity, state, min, med, max, date))
            sql.commit()
    except():
        pass
        print 'Error Occurred databasing!'

def insert_Stock(ticker, price, time):
    try:
        if checkTableExists('Stock_Data') != False:
            sql = database_Connect()
            cur = sql.cursor()
            query = "INSERT INTO `Stock_Data` VALUES(%s, %s,%s);"
            print query
            cur.execute(query,(ticker, price, time))
            sql.commit()
        else:
            sql = database_Connect()
            cur = sql.cursor()
            database_Table_Stock('Stock_Data')
            query = "INSERT INTO `Stock_Data` VALUES(%s, %s,%s);"
            cur.execute(query, (ticker, price, time))
            sql.commit()
    except():
        pass
        print 'Error occurred databasing!'

#Queries the table, and returns all values which either match or include the
#name string in their overall value
def database_Read(table, currency):
    sql = database_Connect()
    cur = sql.cursor()
    query = "SELECT * FROM `Currency_Data` WHERE currency LIKE '" + currency + "%'"
    for row in cur.execute(query):
        return row

#Allows the ordering of table read outs to help allow users to view data better
def database_Order(table, order):
    sql = database_Connect()
    cur = sql.cursor()
    query = "SELECT * FROM " + table + " ORDER BY " + order
    for row in cur.execute(query):
        print row
