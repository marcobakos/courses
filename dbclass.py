import psycopg2
"""
   Class to access Data Base PostGres
"""


class DbClass:
    """
        Class to be use to access the PostGres DataBase
            Methods :
                - connect()
                - execute(command)
                - commit()
                - close () - connection and cursor
    """

    def __init__(self,
                 hst='localhost',
                 dbn='courses',
                 usr='postgres',
                 psw='postgres',
                 prt='5432',
                 conn=None,
                 cur=None,
                 log=False):
        """
            Args:
                :param hst (str): PostGres host
                :param dbn (str): PostGres data base name - default = courses
                :param usr (str): PostGres user name
                :param psw (str): PostGres password
                :param prt (str): PostGres port - 5432
                :param conn (str): PostGres connection information
                :param cur (str): PostGres cursor for commands
                :param log (boolean): Print information - default = False
        """
        self.hst = hst
        self.dbn = dbn
        self.usr = usr
        self.psw = psw
        self.prt = prt
        self.conn = conn
        self.cur = cur
        self.log = log

    def connect(self):
        """ Connect to database - PostGresSQL """
        self.conn = psycopg2.connect(
            host=self.hst,
            database=self.dbn,
            user=self.usr,
            password=self.psw,
            port=self.prt
        )
        self.cur = self.conn.cursor()
        if self.log:
            print("Connecting to the PostgreSQL database...> '{db}' was succesfull.\n"
                  .format(db=self.dbn))

    def execute(self, sql):
        """ Execute Command database - SQL """
        if self.log:
            print("Command --> '{cmd}' \n".format(cmd=sql))
        self.cur.execute(sql)

    def commit(self):
        """ Execute Commit """
        # commit the changes
        self.conn.commit()
        if self.log:
            print("Commit was succesful.\n")

    def close(self):
        """ Close connection and cursor of the PostgreSQL database server """
        # close the communication with the PostgreSQL
        self.cur.close()
        self.conn.close()
        if self.log:
            print("\nClose conn and cur of the PostgreSQL database...> '{db}' was succesfull."
                  .format(db=self.dbn))

#