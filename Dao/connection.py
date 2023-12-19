from Util.connection import DBConnection

class PropertyUtil:
    def init(self):
        PropertyUtil.connection=DBConnection.getConnection()
obj=PropertyUtil()