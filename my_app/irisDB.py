import psycopg2


def iris_db(features=None):

    conn = psycopg2.connect(
        host="localhost",
        database="iris",
        user="iris",
        password="iris"
    )

    if features is not None:    # เขียนข้อมูลลง database
        # สร้าง cursor object
        cur = conn.cursor()

        # สร้าง query SQL
        query = "INSERT INTO iris_predict (sepal_length,sepal_width,petal_length,petal_width,iris_type) VALUES (%s,%s,%s,%s,%s)"

        # ทำการ execute query
        cur.execute(query,[features[0],features[1],features[2],features[3],features[4]])

        # ยืนยันการเปลี่ยนแปลง
        conn.commit()

        # ปิดการเชื่อมต่อ
        cur.close()
        conn.close()

        return 0

    else:                      # อ่านข้อมูลจาก database

        # สร้าง cursor object
        cur = conn.cursor()

        # สร้าง query SQL
        cur.execute("SELECT * FROM iris_predict")

        # รับข้อมูลทั้งหมด
        data = cur.fetchall()

        # ปิดการเชื่อมต่อ
        cur.close()
        conn.close()
        
        return data