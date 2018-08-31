import sqlite3
database='C:/Web development/HTML_DJANGO/python_lvl_2/import_test/fol/mqttdb.db'
def create_table():
    conn=sqlite3.connect(database)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS message (topic TEXT,letter TEXT)")
    conn.commit()
    conn.close

def insert(topic,letter):
    conn=sqlite3.connect(database)
    cur=conn.cursor()
    cur.execute("INSERT INTO message VALUES(?,?)",(topic,letter))
    conn.commit()
    conn.close

# insert("test2","Hii !")

def view_all():
    conn=sqlite3.connect(database)
    cur=conn.cursor()
    cur.execute("SELECT * FROM message")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(topic):
    conn=sqlite3.connect(database)
    cur=conn.cursor()
    cur.execute("DELETE TABLE message")
    # cur.execute("DELETE FROM store WHERE topic=?",(topic,))
    conn.commit()
    conn.close()

def update(letter,topic):
    conn=sqlite3.connect(database)
    cur=conn.cursor()
    cur.execute("UPDATE message SET letter=? WHERE topic=?",(letter,topic))
    conn.commit()
    conn.close()

def view_topic(topic):
    conn=sqlite3.connect(database)
    cur=conn.cursor()
    cur.execute("SELECT topic FROM message where topic=?",(topic,))
    rows=cur.fetchall()
    conn.close()
    return rows

def view_letter(topic):
    conn=sqlite3.connect(database)
    cur=conn.cursor()
    cur.execute("SELECT letter FROM message where topic=?",(topic,))
    rows=cur.fetchall()
    conn.close()
    return rows

def check_insert(topic,letter):
    a=view_topic(topic)
    if (str(a)=='[]'):
        insert(topic,letter)
    else:
        update(letter,topic)

def steps(topic,letter):
    create_table()
    check_insert(topic,letter)



# create_table()
# check_insert("help","china")
print(view_all())
# insert("africa","china")


# delete("Wine Glass")

# ms=view2("test")
# print(ms[1:6])




# update("Welcome","test")

# print(view())
