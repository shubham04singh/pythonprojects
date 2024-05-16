def main():
    try:
        # Open a file in write mode
        with open('student_ages.txt', 'w') as file:
            # Ask user for the number of students
            num_students = int(input("Enter the number of students: "))
            
            # Write student ages to the file
            for i in range(num_students):
                age = input(f"Enter age of student {i+1}: ")
                file.write(age + '\n')
                
        print("Student ages have been written to student_ages.txt.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
4
