import psycopg2
from dbclass import DbClass


if __name__ == '__main__':

    try:
#
        db = DbClass(dbn="Bakos", log=True)
#
        db.connect()
#
        command = "SELECT oid, * FROM pg_catalog.pg_am"
        db.execute(command)
#
        fetch = db.cur.fetchall()
        i = 1
        for row in fetch:
            print("Row number ", i, "- ", row)
            i += 1
#
        db.close()
#
    except (Exception, psycopg2.DatabaseError) as error:
        print("Db error = ", error)
