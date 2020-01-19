import mysql.connector
from tkinter import messagebox

class DBHelper:

    def __init__(self):
        try:
            self._connection = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="tinder")
            self._myCursor = self._connection.cursor()
            self._flag=True
        except:
            messagebox.showerror("CONNECTIVITY","YOU ARE NOT CONNECTED TO THE SERVER")
            self._flag=False

    def checkConnection(self):
        return self._flag

    def searchItem(self, column1, table, column2, value,user_id="",userValue=""):
        if column1 != '*':
            self._myCursor.execute("SELECT `{}` FROM `{}` WHERE {} LIKE '{}'".format(column1, table, column2, value))
        else:
            self._myCursor.execute(
                "SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` NOT LIKE {} ORDER BY `name` ASC".format(table, column2, value,
                                                                                           user_id,userValue))

        response = self._myCursor.fetchall()
        return response


    def search(self, table, key1, value1, key2, value2):

        self._myCursor.execute(
            "SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'".format(table, key1, value1, key2, value2))
        response = self._myCursor.fetchall()
        return response

    def getAll(self, table, user_id):

        self._myCursor.execute("SELECT * FROM `{}` WHERE `user_id` != {} ORDER BY `name` ASC".format(table, user_id))
        response = self._myCursor.fetchall()
        return response

    def insert(self, table, inputDict):
        cols = ""
        vals = ""

        for i in inputDict:
            cols += "`" + i + "`" + ","
            vals += "'" + str(inputDict[i]) + "'" + ","

        cols = cols[:-1]
        vals = vals[:-1]

        try:
            self._myCursor.execute("INSERT INTO `{}` ({}) VALUES ({})".format(table, cols, vals))
            self._connection.commit()
            return True
        except:
            return False

    def update(self, table, user_id, updateDict):

        try:
            s = ''
            for i in updateDict:
                s += '`' + i + '`' + " = " + "'" + updateDict[i] + "'" + ","
            s = s[:-1]
            t = "UPDATE " + "`" + "{}".format(table) + "`" + " SET " + s + " WHERE " + "`" + "{}".format(
                table) + "`." + "`" + "user_id" + "`" + " = " + str(user_id)

            self._myCursor.execute(t)
            self._connection.commit()

            return True
        except:
            return False

    def delete(self, table, column, value):

        try:
            s = "DELETE FROM `{}` WHERE `{}`.`{}` = {}".format(table, table, column, value)
            self._myCursor.execute(s)
            self._connection.commit()

            return True
        except:
            return False

    def findProposalsOrRequests(self,column1,column2,user_id):

        s="SELECT * FROM `users` where `user_id` in ( SELECT `{}` from proposals where `{}` = {} ) ORDER BY `name` ASC".format(column1, column2, user_id)
        self._myCursor.execute(s)
        response=self._myCursor.fetchall()

        return response

    def findMatches(self,user_id):

        s="SELECT * FROM `users` WHERE `user_id` in ( SELECT `romeo_id` FROM `proposals` WHERE `romeo_id` in ( SELECT `juliet_id` FROM `proposals` where `romeo_id` = {0} ) and `juliet_id` = {0} ) ORDER BY `name` ASC".format(user_id)
        self._myCursor.execute(s)
        response=self._myCursor.fetchall()

        return response