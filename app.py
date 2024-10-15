def greet_person():
    print("Welcome to the Scoreboard!")

def get_score_input():
    while True:
        try:
            score = int(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def evaluate_score(score):
    if score >= 90:
        return "Excellent - Passed"
    elif 80 < score < 90:
        return "Great - Passed"
    elif 70 <= score <= 80:
        return "Good - Passed"
    elif 60 <= score < 70:
        return "Satisfactory - Passed"
    else:
        return "Failed"

def main():
    greet_person()  # Call the greeting function first
    while True:
        score = get_score_input()
        result = evaluate_score(score)
        print(result)

        again = input("Would you like to enter another score? (yes/no): ").strip().lower()
        if again != 'yes':
            break


if __name__ == "__main__":
    main()
