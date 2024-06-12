import sqlite3
import datetime

def byteConvert(filename: str):
    f = open(filename, mode="rb")
    data = f.read()
    """ 
    Conversao de bytes em milimetro
        Divide a string de bytes em um vetor com um byte com um valor e um byte vazio
        Converte o byte com valor para um numero inteiro via type casting
        Ex: 250mm   
    """
    number = int(data.split(b'mm')[0])
    f.close()
    return number

def createBank(bankname: str):
    conn = None
    try:
        conn = sqlite3.connect(bankname)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def createTable(bankname: str):
    sql_statement = ["""CREATE TABLE IF NOT EXISTS readings(
                        data CHAR(30) PRIMARY KEY NOT NULL,
                        value INT NOT NULL);
                    """]

    try:
        with sqlite3.connect(bankname) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_statement[0])
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def insertBank(bankname: str, values: tuple):
    sql_statement = '''INSERT INTO readings(data, value) VALUES(?,?)'''
    try:
        with sqlite3.connect(bankname) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_statement, values)
            conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    

if __name__ == "__main__":
    filename = str(input("Insira o nome do arquivo: "))
    distance = byteConvert(filename)
    time = datetime.datetime.now()
    timestring = str(time)
    createBank("banco.db")
    createTable("banco.db")
    insertBank("banco.db", (timestring, distance))