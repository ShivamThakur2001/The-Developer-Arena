
marks = float(input("Enter your marks (out of 100): "))


if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
elif marks >= 90:
    print("Grade: A+ (Excellent!)")
elif marks >= 80:
    print("Grade: A (Very Good)")
elif marks >= 70:
    print("Grade: B (Good)")
elif marks >= 60:
    print("Grade: C (Average)")
elif marks >= 50:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")

print("Thank you for using the Grade Calculator!")
