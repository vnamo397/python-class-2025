import random

def generate_scores():
    """
    Generates scores (50-100) for 100 students (1000-1099) for 5 subjects
    and saves them to score.txt.
    """
    with open('score.txt', 'w') as f:
        for student_id in range(1000, 1100):
            english_score = random.randint(50, 100)
            math_score = random.randint(50, 100)
            programming_score = random.randint(50, 100)
            ai_score = random.randint(50, 100)
            db_score = random.randint(50, 100)
            f.write(f"{student_id},{english_score},{math_score},{programming_score},{ai_score},{db_score}\n")

if __name__ == "__main__":
    generate_scores()
    print("Successfully generated scores and saved to score.txt")
