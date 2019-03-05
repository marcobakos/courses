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
           CREATE TABLE evaluations (                                                
               course_id INTEGER NOT NULL,                                          
               student_id INTEGER NOT NULL,                                        
               eval_date DATE,                                                      
               eval_course_mod CHAR(10),                                            
               eval_course_date DATE,                                               
               eval_domain CHAR(10),                                                
               eval_present_duration CHAR(10),                                      
               eval_facility CHAR(10),                                              
               eval_clarity CHAR(10),                                               
               eval_relationship CHAR(10),                                          
               eval_usable CHAR(10),                                                
               eval_handout CHAR(10),                                               
               eval_applicable CHAR(10),                                            
               eval_organiz CHAR(10),                                               
               eval_local CHAR(10),                                                 
               eval_expectancy CHAR(10),                                            
               eval_comments CHAR(10),                                              
               eval_strong_points CHAR(150),                                        
               eval_improved_points CHAR(150),                                      
               eval_themes CHAR(150),                                               
               eval_considerations CHAR(150),                                       
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
