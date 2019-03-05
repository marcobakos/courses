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
            CREATE TABLE courses_students (                        
                course_id INTEGER NOT NULL,                       
                student_id INTEGER NOT NULL,                     
                course_date_init DATE,                            
                course_date_finish DATE,                          
                PRIMARY KEY (course_id , student_id),             
                FOREIGN KEY (course_id)                           
                    REFERENCES courses (course_id)                
                    ON UPDATE CASCADE ON DELETE CASCADE,          
                FOREIGN KEY (student_id)                          
                    REFERENCES students (student_id)              
                    ON UPDATE CASCADE ON DELETE CASCADE           
                )                                                                                                                                                    
            """)
        db.execute(command)
#
        db.commit()
#
        db.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DataBase '{dbn}' - Error = ".format(dbn=db.dbn), error)
