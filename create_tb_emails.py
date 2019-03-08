import psycopg2
from dbclass import DbClass


if __name__ == '__main__':

    try:
        db = DbClass(dbn="courses", log=True)
#
        db.connect()
#
        command = (
            """                                                                                                            
           CREATE TABLE emails (                               
               email_id VARCHAR(70) PRIMARY KEY,                  
               email_active CHAR(01) NOT NULL                   
               )                                                                                                                 
            """)
        db.execute(command)
#
        db.commit()
#
        db.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DataBase '{dbn}' - Error = ".format(dbn=db.dbn), error)






