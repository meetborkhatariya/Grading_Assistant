def batch_grade():
    print("\n--- Batch Grading ---")
    answer_key = input("Enter the answer key (comma-separated): ").strip().split(",")
    print("Enter each student's name or roll number, then their answers (comma-separated). Enter a blank name to finish:")
    students = []
    while True:
        name = input("Student name or roll no (blank to finish): ").strip()
        if not name:
            break
        answers = input(f"Answers for {name} (comma-separated): ").strip().split(",")
        students.append((name, answers))
    results = []
    print("\nResults:")
    for name, student_answers in students:
        score = sum(1 for a, b in zip(answer_key, student_answers) if a.strip().upper() == b.strip().upper())
        print(f"{name}: {score}/{len(answer_key)} correct | Answers: {student_answers}")
        results.append((name, score, student_answers))
    input("\nPress Enter to return to the main menu...")
    return results

