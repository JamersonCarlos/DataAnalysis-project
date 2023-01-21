import random
import mysql.connector
dbMySql = mysql.connector.connect(host="localhost", database="banco", user="user", password="pass")
cursordb = dbMySql.cursor()
cursordb.execute('''use banco''')
# cursordb.execute("""CREATE TABLE CONTAS_BANCO (id integer not null primary key autoincrement, numConta int, saldoConta float)""")
# queryResult = cursordb.execute("""SELECT * FROM CONTAS_BANCO WHERE id = 1""")



class Banco():
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        cursordb.execute("""INSERT INTO CONTAS_BANCO (numConta, saldoConta) VALUES (%s, %s)""", [num, 0.0])
        dbMySql.commit()
        return num

    def consultaSaldo(self, numConta):
        cursordb.execute("""SELECT * FROM CONTAS_BANCO WHERE numConta = %s""", [numConta])
        queryResult = cursordb.fetchall()
        if(queryResult != []): 
            return queryResult[0][2]
        return -1

    def depositar(self, numConta, valor):
        cursordb.execute("""SELECT * FROM CONTAS_BANCO WHERE numConta = %s""", [numConta])
        queryResult = cursordb.fetchall()
        if(queryResult != []):
            newSaldo = queryResult[0][2] + valor
            cursordb.execute("""UPDATE CONTAS_BANCO SET saldoConta = %s WHERE numConta = %s """, [newSaldo, numConta])
            dbMySql.commit()
                
    def sacar(self, numConta, valor):
        cursordb.execute("""SELECT * FROM CONTAS_BANCO WHERE numConta = %s""", [numConta])
        queryResult = cursordb.fetchall()
        if(queryResult!= []): 
            saldo = queryResult[0][2]
            if (saldo >= valor): 
                saldo = saldo - valor
                cursordb.execute("""UPDATE CONTAS_BANCO SET saldoConta = %s WHERE numConta = %s""", [saldo, numConta])
                dbMySql.commit()
                return True 
            return False
