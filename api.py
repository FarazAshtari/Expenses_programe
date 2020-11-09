import sqlite3
from datetime import datetime

conn = sqlite3.connect('sepent.db')
c = conn.cursor()
def init():

    c.execute(''' CREATE TABLE IF NOT EXISTS expenses(
                    amount REAL,
                    category TEXT COLLATE NOCASE,
                    message TEXT,
                    date TEXT
                        )''')

    conn.commit()
    conn.close()

def add(amount , category , message = ''):

    date = str(datetime.now().strftime('%Y , %M , %D | %H:%M'))
    c.execute('INSERT INTO expenses VALUES (:amount , :category , :message , :date)', {'amount' : amount , 'category' : category , 'message' : message , 'date' : date})
    conn.commit()
    conn.close

def show(category = None):

    if category:
        c.execute('SELECT * FROM expenses WHERE categoty = (:category)', {'category' : category})
        result = c.fetchall()
        c.execute('SELECT sum(amount) FROM expenses WHERE categoty = (:category)', {'category' : category})
        Total_amount = c.fetchone()[0]
    
    else:
        c.execute('SELECT * FROM expenses')
        result = c.fetchall()
        c.execute('SELECT sum(amount) FROM expenses')
        Total_amount = c.fetchone()[0]
        
    return Total_amount , result
    conn.close


#init()
#add(20 , 'cinama')
