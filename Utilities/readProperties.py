import configparser
config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicatinURL():
        url= config.get('common info','BaseUrl')
        return url
    @staticmethod
    def getuserMail():
        username= config.get('common info','username')
        return username
    @staticmethod
    def getuserPassword():
        password= config.get('common info','password')
        return password
