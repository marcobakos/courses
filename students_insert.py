import pandas as pd
import numpy as np
import psycopg2
from dbclass import DbClass

if __name__ == '__main__':

    try:
        dfr = pd.read_csv('Students_Unique_OK.csv', ";")
        arr1 = np.array(dfr)
#
        db = DbClass(dbn="courses", log=True)
#
        db.connect()
#
        i = 0
        for rec in arr1:
            obs = rec[4]
            obs_250 = obs[:250]
            command = ("INSERT INTO students " +
                       "(student_id, student_name, student_email, student_tel, student_obs)" +
                       " VALUES ('{r0}' , '{r1}' , '{r2}' , '{r3}' , '{r4}' )"
                       .format(r0=rec[0], r1=rec[1], r2=rec[2], r3=str(rec[3]), r4=obs_250))
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







