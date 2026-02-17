students = {};

if __name__=="__main__":
    print("This is the main module");
    while(1):
        print("Enter the option to perform the operation \n" \
        "1. Add student \n" \
        "2. View students \n" \
        "3. Update student \n" \
        "4. Delete student \n" \
        "5. Exit");
        option = int(input("Enter the option: "));
        if option == 1:
            name = input("Enter the student name: ");
            grade = input("Enter the student grade: ");
            students[name] = grade;
            print("Student added successfully");
        elif option == 2:
            print("Students: ");
            for name, grade in students.items():
                print(f"Name: {name}, Grade: {grade}");
        elif option == 3:
            name = input("Enter the student name to update: ");
            if name in students:
                grade = input("Enter the new grade: ");
                students[name] = grade;
                print("Student updated successfully");
            else:
                print("Student not found");
        elif option == 4:
            name = input("Enter the student name to delete: ");
            if name in students:
                del students[name];
                print("Student deleted successfully");
            else:
                print("Student not found");
        elif option == 5:
            print("Exiting...");
            break;
        else:
            print("Invalid option. Please try again.");
