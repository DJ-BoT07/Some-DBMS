import pymongo
from bson.code import Code
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['bookstore']
books_collection = db['books']

def insert_book(name, pages):
    books_collection.insert_one({
        'name': name,
        'pages': int(pages)
    })
    print("Book inserted successfully")

def categorize_books():
    try:
        # Map function
        mapper = """
            function() {
                var category = (this.pages >= 200) ? "Big Book" : "Small Book";
                emit(category, {
                    books: [{
                        name: this.name,
                        pages: this.pages
                    }]
                });
            }
        """

        # Reduce function
        reducer = """
            function(key, values) {
                var result = { books: [] };
                values.forEach(function(value) {
                    result.books = result.books.concat(value.books);
                });
                return result;
            }
        """

        # Execute map-reduce using command
        result = db.command({
            'mapReduce': 'books',
            'map': mapper,
            'reduce': reducer,
            'out': {'inline': 1}
        })

        # Print results
        for doc in result['results']:
            print(doc['_id'] + ':')
            for book in doc['value']['books']:
                print(book['name'], book['pages'])

    except Exception as e:
        print(f"Error in map-reduce operation: {e}")

def main():
    print("Welcome to Book Categorization System")
    while True:
        try:
            print("\n1. Insert Book")
            print("2. Categorize Books")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                name = input("Enter book name: ")
                pages = input("Enter number of pages: ")
                insert_book(name, pages)
            
            elif choice == 2:
                categorize_books()
            
            elif choice == 3:
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Please enter a valid number!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()