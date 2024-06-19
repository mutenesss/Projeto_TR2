import sqlite3
import datetime

def byteConvert(filename: str) -> int:
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

def createBank(bankname: str) -> None:
    # Cria um banco de dados com o nome passado
    conn = None
    try:
        conn = sqlite3.connect(bankname)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def createTable(bankname: str) -> None:
    # Cria uma tabela readings com os campos data e value
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

def insertBank(bankname: str, values: tuple) -> None:
    # Insere uma tupla (data, valor) no banco 
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
    
def returnLastRecords(bankname: str) -> list:
    # Retorna ate os 3 ultimos registros do banco
    sql_statement = '''SELECT * FROM readings ORDER BY data DESC LIMIT 3'''
    try:
        with sqlite3.connect(bankname) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_statement)
            conn.commit()
            rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            return rows
                
def timeSinceLastRecord(time_buffer: list) -> list:
    # Calcula o tempo desde a ultima leitura
    difference = []
    time = datetime.datetime.now()
    for value in time_buffer:
        old = time.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
        difference.append(time - old)
    # Diferenca entre a ultima leitura e a leitura mais antiga
    return difference


if __name__ == "__main__":
    # buffers podem ser implementados com tupla
    reading_buffer = []
    time_buffer = []
    filename = str(input("Insira o nome do arquivo: "))
    distance = byteConvert(filename)
    time = datetime.datetime.now()
    timestring = str(time)
    createBank("banco.db")
    createTable("banco.db")
    #insertBank("banco.db", (timestring, distance))
    records = returnLastRecords("banco.db")
    if len(records) == 3:
        # Guarda as tres ultimas leituras em buffer para calcular media
        # A leitura mais recente fica na posicao 0, enquanto a mais antiga na posicao 2
        for record in records:
            time_buffer.append(record[0])
            reading_buffer.append(record[1])
            
    for i in range(3):
        a = timeSinceLastRecord(time_buffer)
        print(a[i])
    