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
            CREATE TABLE courses (                                                                                
                course_id SERIAL PRIMARY KEY,                                                                     
                course_name CHAR(25) NOT NULL,                                                                    
                course_descrip VARCHAR(250),                                                                         
                course_mod  CHAR(10),                                                                             
                course_type CHAR(03)                                                                              
                )                                                                                                                                                                                                 
            """)
        db.execute(command)
#
        db.commit()
#
        db.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DataBase '{dbn}' - Error = ".format(dbn=db.dbn), error)
