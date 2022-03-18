import re
import hashlib
from collections import namedtuple

UserInfo = namedtuple('UserInfo', 'name email tgname')
Message = namedtuple('Message', 'id text date from_tgn to_tgn is_edit')

class Database(object):
    def __init__(self):
        """Constructor"""
        self.__list_UserInfo = []
        self.__list_Message = []

    def check_UserInfo(self, name, email, tgname):
        if name == "":
            return -1
        if email == "" or not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            return -2
        if tgname == "":
            return -3
        return 0

    def set_UserInfo(self, name, email, tgname):
        rcode = self.check_UserInfo(name, email, tgname)
        if rcode:
            return rcode

        self.__list_UserInfo.append(UserInfo(name, email, tgname))
        return 0

    def get_UserList(self):
        return self.__list_UserInfo

    def get_UserInfo(self, index):
        try:
            return self.__list_UserInfo[index]
        except IndexError:
            return UserInfo("", "", "")

    def check_Message(self, text, tgname):
        if text == "":
            return -1
        if tgname == "":
            return -2
        return 0

    def get_MessageId(self, date, tgname):
        if date == "" or tgname == "":
            return ""
        else:
            return hashlib.md5(str(str(date)+tgname).encode('utf-8')).hexdigest()

    def set_Message(self, text, from_date, from_tgn, to_date="", to_tgn=""):
        rcode = self.check_Message(text, from_tgn)
        if rcode:
            return rcode

        from_id = self.get_MessageId(from_date, from_tgn)
        to_id = self.get_MessageId(to_date, to_tgn)
        self.__list_Message.append(Message(from_id, text, from_date, from_tgn, to_id, False))
        return 0

    def edit_Message(self, new_text, from_date, from_tgn):
        try:
            rcode = self.check_Message(new_text, from_tgn)
            if rcode:
                return rcode

            id = self.get_MessageId(from_date, from_tgn)
            for ind in range(len(self.__list_Message)):
                if self.__list_Message[ind].id == id:
                    if self.__list_Message[ind].text != new_text:
                        self.__list_Message[ind] = self.__list_Message[ind]._replace(is_edit=True)

            return 0
        except IndexError:
            return -99

    def get_MessageList(self):
        return self.__list_Message

    def get_Message(self, index):
        try:
            return self.__list_Message[index]
        except IndexError:
            return Message("", 0, "", 0, False)