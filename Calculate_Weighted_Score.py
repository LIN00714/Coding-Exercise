# Weighted Exam Score Average

# Calculate average exam score for each year, then identify which year contribute to
# the score for degree classification, and calculate the fincal weighted exam score

# Entering how many years you have studied for your degree
number_of_years = int(input("Enter number of years: "))
print(number_of_years)

# Store average score for each year
score_list = []

# For each year calculate the average exam score
for year in range(number_of_years):
    # Entering how many exams you have done
    print("Enter number of exams for year", year+1, "below.")
    number_of_exams = int(input("Enter number of exams for: "))
    print("Number of exams for year ", year+1, "is", number_of_exams)
    # Entering how many credits these exams cover
    total_credits = int(input("Enter how many credits these exams cover: "))
    # Begin with average of 0 and then add up percentages from each exam
    average = 0
    for exam in range(number_of_exams):
        score = int(input("Enter exam score: "))
        exam_credits = int(input("Enter how many credits this exam covered: "))
        average = average + score * exam_credits / total_credits
    print("Your average for year", year+1, "is", average)
    score_list.append(average)

print(score_list)

# Enter which year will contribute to the weighted_score for final degree
# classification
print("If over one year's score is used, enter '12' for year 1 and 2")
w_list = list(input("Enter number of years contributed to degree classification: "))

# Calculate final weighted score for year contributed to degree classification
w_score = 0
for j in w_list:
    print("For year", j)
    y_score = score_list[int(j)-1]
    y_cont = int(input("Enter how many percentage this year contributed: "))
    w_score = w_score + y_score*y_cont*0.01

print("Your final average score that contributed to degree classification is ", w_score)
