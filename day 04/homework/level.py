# input - არის ბრძანების გაცემა ანუ მოწყობილობიდან ან პროგრამიდან გამავალი ბრძანება, რომელიც უნდა შესრულდეს. output - არის ბრძანების შესრულების შედეგი, რომელიც შეიძლება იყოს ტექსტი, სურათი ან სხვა ტიპის მონაცემი.
# output - არის როდესაც მიღებული ბრძანების შედეგი რომელიც შეიძლება იყოს ტექსტი სურათი ან სხვა ტიპის მონაცემი მაგალითად კლავიატურა როცა ღილაკს აჭერ ის გამოაქვს ეკრანზე.

GuestName =input("Enter your name: ")
GuestSurname =input("Enter your surname: ")
GuestAge =int(input("Enter your age: "))
GuestHeight =float(input("Enter your height: "))

favorite_car = input("Enter your favorite car: ")
favorite_color = input("Enter your favorite color: ")

print(f"Favorite car: {favorite_car}")
print(f"Favorite color: {favorite_color}")

# type- ფუნქციით ჩვენ ვიგებთ რა ტიპის არის მონაცემი მაგალითად int, float, str.

print(type(GuestName))
print(type(GuestAge))
