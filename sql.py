import mysql.connector as con;

def create_database():
    try:
        with con.connect(host='localhost', user='admin',password='admin') as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE DATABASE IF NOT EXISTS doctor_appointment')
            cursor.execute('USE doctor_appointment')
    except Exception as e:
        print(e)

def connect_to_database():
    return con.connect(host='localhost', user='admin',password='admin' , database = 'doctor_appointment')

def create_table():
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS patient(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL)
            ''')
        
def add_patient(name, phone , email):
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO patient(name, phone, email) VALUES('{name}', '{phone}', '{email}')" )
        conn.commit()
        print('Patient added successfully')

def view_patients():
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patient')
        patients = cursor.fetchall()
        for patient in patients:
            print(patient)

def search_patient(patient_id):
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM patient WHERE id = {patient_id}")
        patient = cursor.fetchone()
        if patient:
            print(patient)
        else:  
            print('Patient not found')

def update_patient(patient_id, name , phone , email):
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE patient set name= '{name}', phone = '{phone}', email = '{email}' WHERE id = {patient_id}")
        conn.commit()
        print('Patient updated successfully')

def delete_patient(patient_id):
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM patient WHERE id = {patient_id}")
        conn.commit()
        print('Patient deleted successfully')

def menu():
    while True:
        print('1. Add patient')
        print('2. View patients')
        print('3. Search patient')
        print('4. Update patient')
        print('5. Delete patient')
        print('6. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter name: ')
            phone = input('Enter phone: ')
            email = input('Enter email: ')
            add_patient(name, phone, email)
        elif choice == '2':
            view_patients()
        elif choice == '3':
            patient_id = int(input('Enter patient id: '))
            search_patient(patient_id)
        elif choice == '4':
            patient_id = int(input('Enter patient id: '))
            name = input('Enter name: ')
            phone = input('Enter phone: ')
            email = input('Enter email: ')
            update_patient(patient_id, name, phone, email)
        elif choice == '5':
            patient_id = int(input('Enter patient id: '))
            delete_patient(patient_id)
        elif choice == '6':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    create_database()
    create_table()
    menu()
    
    

        
            
    
            
    