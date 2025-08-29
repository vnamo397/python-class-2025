def score_to_grade(score):
    """Converts a numerical score to a letter grade."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """
    Reads scores from score.txt, converts them to grades,
    and saves the results to grade.txt.
    """
    try:
        with open('score.txt', 'r') as f_scores, open('grade.txt', 'w') as f_grades:
            for line in f_scores:
                parts = line.strip().split(',')
                student_id = parts[0]
                scores = [int(score) for score in parts[1:]]
                grades = [score_to_grade(score) for score in scores]
                f_grades.write(f"{student_id},{','.join(grades)}\n")
        print("Successfully converted scores to grades and saved to grade.txt.")
    except FileNotFoundError:
        print("Error: score.txt not found. Please run score.py first to generate it.")

if __name__ == "__main__":
    main()
