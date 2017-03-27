import sqlite3

def create_table():
    conn=sqlite3.connect('Store.db')
    cursor=conn.cursor();
    cursor.execute('CREATE TABLE IF NOT EXISTS Store (Item TEXT,Quantity INTEGER,Price REAL)');
    conn.commit();
    conn.close();

def insert(Item,Quantity,Price):
    conn=sqlite3.connect('Store.db')
    cursor=conn.cursor();
    cursor.execute("INSERT INTO Store VALUES(?,?,?)",(Item,Quantity,Price))
    conn.commit();
    conn.close();

def view():
    conn=sqlite3.connect('Store.db')
    cursor=conn.cursor();
    cursor.execute("SELECT * FROM Store");
    rows=cursor.fetchall();
    conn.close();
    return rows;

def delete(item):
    conn=sqlite3.connect('Store.db')
    cursor=conn.cursor();
    cursor.execute("DELETE FROM Store WHERE Item=?",(item,));
    conn.commit();
    conn.close();

def update(item,Quantity):
    conn=sqlite3.connect('Store.db')
    cursor=conn.cursor();
    cursor.execute("UPDATE Store SET Quantity=? WHERE Item=?",(Quantity,item));
    conn.commit();
    conn.close();
    
    
create_table();
insert('Capacitor',10,21);
insert('Coupler',12,10);
print view()
delete('Coupler')
update('Capacitor',9)
print view()
