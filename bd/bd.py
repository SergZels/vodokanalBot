import sqlite3

class botBD:
	
	def __init__(self) -> None:
		self.con = sqlite3.connect("db_ai_bot.db",check_same_thread=False)
		self.cursor = self.con.cursor()

	def close(self):
		self.con.close()

	def rec(self,os_rax:str,pib:str,street:str,pokaznik:str,date:str):
		#with open("c:\d\code\TelegramBot\otus.txt", "a") as file:
		#	 file.write(mes)
		self.cursor.execute("INSERT INTO main (os_raxunok, pib, street, pokaznik, date) VALUES (?,?,?,?,?)",(os_rax,pib,street,pokaznik,date,))
		#self.cursor.execute("INSERT INTO main (os_raxunok, pib, street, pokaznik, date) VALUES ('555','Кошляк','Січових Стр','111','27.07.2022')")

		self.con.commit()

	def stat(self):
		rows= self.cursor.execute("SELECT os_raxunok, pib, street, pokaznik, date FROM main").fetchall()
		st=""
		for i in rows:
			st+=f"Особовий рахунок: {i[0]}\nПІБ: {i[1]}\nВулиця: {i[2]}\nПоказник: {i[3]}\nДата: {i[4]}\n"
		
		return st
		#with open("c:\d\code\TelegramBot\otus.txt", "r") as file:
		#	return file.read()