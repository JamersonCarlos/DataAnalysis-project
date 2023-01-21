import random
import sqlite3
db = sqlite3.connect("DB_Banco")
cursordb = db.cursor()
# cursordb.execute("""CREATE TABLE CONTAS_BANCO (id integer not null primary key autoincrement, numConta int, saldoConta float)""")
# queryResult = cursordb.execute("""SELECT * FROM CONTAS_BANCO WHERE id = 1""")



class Banco():
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        cursordb.execute("""INSERT INTO CONTAS_BANCO (numConta, saldoConta) VALUES (?, ?)""", (num, 0.0))
        db.commit()
        return num

    def consultaSaldo(self, numConta):
        cursordb.execute("""SELECT * FROM CONTAS_BANCO WHERE numConta = ?""", [numConta])
        queryResult = cursordb.fetchall()
        if(queryResult != []): 
            return queryResult[0][2]
        return -1

    def depositar(self, numConta, valor):
        cursordb.execute("""SELECT * FROM CONTAS_BANCO WHERE numConta = ?""", [numConta])
        queryResult = cursordb.fetchall()
        if(queryResult != []):
            newSaldo = queryResult[0][2] + valor
            cursordb.execute("""UPDATE CONTAS_BANCO SET saldoConta = ? WHERE numConta = ? """, [newSaldo, numConta])
            db.commit()
                
    def sacar(self, numConta, valor):
        cursordb.execute("""SELECT * FROM CONTAS_BANCO WHERE numConta = ?""", [numConta])
        queryResult = cursordb.fetchall()
        if(queryResult!= []): 
            saldo = queryResult[0][2]
            if (saldo >= valor): 
                saldo = saldo - valor
                cursordb.execute("""UPDATE CONTAS_BANCO SET saldoConta = ? WHERE numConta = ? """, [saldo, numConta])
                db.commit()
                return True 
            return False
