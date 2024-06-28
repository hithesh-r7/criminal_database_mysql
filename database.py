import mysql.connector
mydb = mysql.connector.connect(
user="root",
password="kryptonneon7",
host="localhost",
port=3306,
database="criminal_management",

)
c = mydb.cursor()
def create_table():
    c.execute('create table criminal(criminal_id int NOT NULL,weight int NOT NULL,eye_color varchar(10) NOT NULL,age int NOT NULL,height varchar(5) NOT NULL,gender varchar(10) NOT NULL,national_origin varchar(15) NOT NULL,mother_toungue varchar(10) NOT NULL,body_marks varchar(30) NOT NULL,body_build varchar(10) NOT NULL,criminal_name varchar(50) NOT NULL,address varchar(75) NOT NULL,phonenumber varchar(10) NOT NULL)')
        # PRIMARY KEY (criminal_id),case_id int(10) NOT NULL,past_history_id int(10) NOT NULL,FOREIGN KEY (case_id) REFERENCES crime_information(case_id) on delete cascade,FOREIGN KEY (past_history_id) REFERENCES past_history(past_history_id) on delete cascade)') 

def add_data(criminal_id, weight, eye_color, age, height, gender , national_origin , mother_toungue , body_marks,body_build,criminal_name,address,phonenumber,case_id,past_history_id):
    c.execute("insert into criminal (criminal_id, weight, eye_color, age, height, gender , national_origin , mother_toungue , body_marks,body_build,criminal_name,address,phonenumber,case_id,past_history_id) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s,%s,%s)", (criminal_id, weight, eye_color, age, height, gender , national_origin , mother_toungue , body_marks,body_build,criminal_name,address,phonenumber,case_id,past_history_id))
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM criminal')
    data = c.fetchall()
    return data
    
def view_only_criminal_names():
    c.execute('SELECT criminal_id FROM criminal')
    data = c.fetchall()
    return data

def get_criminal(criminal_id):
    c.execute('SELECT * FROM criminal WHERE criminal_id="{}"'.format(criminal_id))
    data = c.fetchall()
    return data

def delete_data(criminal_id):
    c.execute('DELETE FROM criminal WHERE criminal_id="{}"'.format(criminal_id))
    mydb.commit()


# make changes caseid pasthistory


    
def edit_criminal_data(new_criminal_id, new_weight, new_eye_color, new_age, new_height, new_gender , new_national_origin , new_mother_toungue , new_body_marks,new_body_build,new_criminal_name,new_address,new_phonenumber,new_case_id,new_past_history_id):
    c.execute('UPDATE criminal set  weight=%s, eye_color=%s, age=%s, height=%s, gender =%s, national_origin =%s, mother_toungue =%s, body_marks=%s,body_build=%s,criminal_name=%s,address=%s,phonenumber=%s,case_id=%s,past_history_id=%s WHERE criminal_id=%s' ,( new_weight, new_eye_color, new_age, new_height, new_gender , new_national_origin , new_mother_toungue , new_body_marks,new_body_build,new_criminal_name,new_address,new_phonenumber,new_case_id,new_past_history_id,new_criminal_id) )
    mydb.commit()
    data = c.fetchall()
    return data

