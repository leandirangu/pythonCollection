def welcome_student(name):
  welcome_str = "Hi {} welcome to Akirachix"
  return welcome_str.format(name)
  
name = input("Enter student name:")
print(welcome_student("Assue"))
print(welcome_student("Eve"))
print(welcome_student("Taspyn"))
print(welcome_student("Maureen"))