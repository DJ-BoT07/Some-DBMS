import pymongo

# At the top of the file, add global connection variables
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['demo']
stud_collection = db['student']

def insert_data(name, roll, email, phone, age):
    stud_collection.insert_one({
        'name':name,
        'roll':roll,
        'email':email,
        'phone':phone,
        'age':age
    })
    print("Data inserted successfully")
    
def read_data():
    data = stud_collection.find()
    for i in data:
        print(i)

def read_one(roll):
    data = stud_collection.find_one({'roll':roll})
    if data:
        for key, value in data.items():
            print(f"{key}: {value}")
        return data
    else:
        print("No record found with this roll number")
        return None

def update_data(roll,name,email,phone,age):
    stud_collection.update_one(
        {'roll': roll},
        {
            '$set':{
                'name':name,
                'email':email,
                'phone':phone,
                'age':age
            }
        }
    )
    print("Data updated successfully")

def delete_data(roll):
    stud_collection.delete_one({
        'roll':roll
    })
    print("Data deleted successfully")



if __name__ == '__main__':
    print("Welcome to MongoDB")
    while True:
        print("1. Insert Data")
        print("2. Read Data")
        print("3. Read One Data")
        print("4. Update Data")
        print("5. Delete Data")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            roll = int(input("Enter roll: "))
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            age = int(input("Enter age: "))
            insert_data(name, roll, email, phone, age)
        elif choice == 2:
            read_data()
        elif choice == 3:
            roll = int(input("Enter roll: "))
            read_one(roll)
        elif choice == 4:
            roll = int(input("Enter roll: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            age = int(input("Enter age: "))
            update_data(roll, name, email, phone, age)
        elif choice == 5:
            roll = int(input("Enter roll: "))
            delete_data(roll)
        elif choice == 6:
            break
        else:
            print("Invalid choice")
        
        

    
    
    