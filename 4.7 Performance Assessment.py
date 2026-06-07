import pandas as pd
import matplotlib.pyplot as plt

def main():
    # 1. Print Student ID
    print("jasdan3949")

    # 2. Create a classroom of 10 students
    students = ["Alex", "Brianna", "Carlos", "Diana", "Ethan",
                "Fatima", "George", "Hannah", "Isaac", "Jasmine"]

    # Grades for two subjects
    math_grades =   [92, 85, 78, 88, 95, 84, 73, 90, 82, 87]
    science_grades = [89, 91, 80, 85, 93, 88, 76, 84, 79, 90]

    # 3. Create a MultiIndex for student + subject
    
    index = pd.MultiIndex.from_product(
        [students, ["Math", "Science"]],
        names=["Student", "Subject"]
    )

    # 4. Create a DataFrame of grades for each student for two subjects
    
    grades = math_grades + science_grades
    df = pd.DataFrame({"Grade": grades}, index=index)

    # 5. Display the DataFrame
    print(df)

    # 6. Group by the mean of each subject
    
    subject_means = df.groupby("Subject").mean()
    print(subject_means)

    # 7. Display the vertical bar graph
    plt.bar(subject_means.index, subject_means["Grade"])
    plt.title("Average Grade by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Grade")
    plt.ylim(0, 100)
    plt.show()

main()
