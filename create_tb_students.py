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
            CREATE TABLE students (                           
                student_id SERIAL PRIMARY KEY,                
                student_name VARCHAR(255) NOT NULL,              
                student_company VARCHAR(50),                     
                student_addr VARCHAR(150),                       
                student_city VARCHAR(50),                        
                student_cpf CHAR(14),                         
                student_cnpj CHAR(19),                        
                student_tel CHAR(13),                         
                student_cel CHAR(13),                         
                student_email VARCHAR(50),                       
                student_obs VARCHAR(150)                         
                )                                                                                                                                                                                                                                         
            """)
        db.execute(command)
#
        db.commit()
#
        db.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DataBase '{dbn}' - Error = ".format(dbn=db.dbn), error)

