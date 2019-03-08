import psycopg2
from dbclass import DbClass

if __name__ == '__main__':

    try:
#
        db = DbClass(dbn="courses", log=True)
#
        db.connect()
#
        i = 0
        for i in range(500):
            command = ("DELETE FROM students " +
                       " WHERE "
                       "student_id IS NOT NULL")
            db.execute(command)
#
        print("Total of records deleted = ", i)
#
        db.commit()
#
        db.close()
#
    except (Exception, psycopg2.DatabaseError) as error:
        print("Db error = ", error)






