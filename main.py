from database import *

test = UserInfo("Дима", "dimamalenkov@gmail.com", "@dmalenkov");

dbase = Database()

rcode = dbase.set_UserInfo("Дима", "dimamalenkov@gmail.com", "@dmalenkov")
print("set_UserInfo return ", rcode)
rcode = dbase.set_UserInfo("Test", "test@test.test", "@test")
print("set_UserInfo return ", rcode)
print(dbase.get_UserList())
print(dbase.get_UserInfo(0).name)
print(dbase.get_UserInfo(0).email)
print(dbase.get_UserInfo(0).tgname)
print(dbase.get_UserInfo(1).name)
print(dbase.get_UserInfo(1).email)
print(dbase.get_UserInfo(1).tgname)

rcode = dbase.set_Message("Это сообщение #1", 99, "@test")
print("set_Message return ", rcode)
rcode = dbase.set_Message("Это сообщение #2", 100, "@dmalenkov", 99, "@test")
print("set_Message return ", rcode)
rcode = dbase.set_Message("Это сообщение #3", 115, "@dmalenkov")
print("set_Message return ", rcode)
rcode = dbase.edit_Message("Отредактированное сообщение #3", 100, "@dmalenkov")
print("edit_Message return ", rcode)
rcode = dbase.edit_Message("Это сообщение #3", 115, "@dmalenkov")
print("edit_Message return ", rcode)
print(dbase.get_MessageList())
