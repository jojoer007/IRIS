from flask import Flask, render_template

app = Flask(__name__)

stu_name = "ณัฐนนท์ แสงจันทร์"
stu_id = "66130537"
stu_email = "66130537@dpu.ac.th"
stu_faculty = "คณะวิศวกรรมศาสตร์"
stu_major = "วิศวกรรมคอมพิวเตอร์"


# หน้าแรก
@app.route('/')

def studentinfo():
    return render_template ('studentinfo.html', stu_name=stu_name, stu_id=stu_id);


# หน้าที่ 2 about
@app.route('/about')

def about():
    return render_template ('about.html', stu_name=stu_name, stu_id=stu_id, stu_email=stu_email, stu_faculty=stu_faculty, stu_major=stu_major);


if __name__ == '__main__':
    app.run(debug=True)