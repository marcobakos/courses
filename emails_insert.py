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
        with open('emails.txt', mode='r') as fl:
            for rec in fl.readlines():
                command = ("INSERT INTO emails (email_id, email_active)" +
                           " VALUES ('{rec}' , 'A')".format(rec=rec))
                print("record num. = ", str(i))
                i += 1
                db.execute(command)

        print("Total of records inserted = ", i)
#
        db.commit()
#
        db.close()
#
    except (Exception, psycopg2.DatabaseError) as error:
        print("Db error = ", error)







