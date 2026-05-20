def student_marks():
    print("\n--- Marks Module ---")

    subject1 = int(input("Enter Marks for Python: "))
    subject2 = int(input("Enter Marks for DBMS: "))
    subject3 = int(input("Enter Marks for OS: "))

    total = subject1 + subject2 + subject3
    average = total / 3

    print("\nResult")
    print("----------------------")
    print(f"Total Marks : {total}")
    print(f"Average     : {average:.2f}")

    if average >= 75:
        print("Grade       : A")
    elif average >= 60:
        print("Grade       : B")
    elif average >= 40:
        print("Grade       : C")
    else:
        print("Grade       : Fail")