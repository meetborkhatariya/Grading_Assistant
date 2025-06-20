import os
import google.generativeai as genai
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
print(f"DEBUG: Loaded API Key ends with: {os.getenv('GEMINI_API_KEY')[-4:] if os.getenv('GEMINI_API_KEY') else 'None'}")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create Gemini model
gemini_model = Gemini(id="gemini-1.5-flash")

grading_assistant = Agent(
    name="Grading Assistant",
    role="Assignment grader who evaluates student submissions and provides feedback",
    instructions="""
You will be given a set of student answers and the corresponding answer key or rubric.
1. For each answer, compare the student's response to the answer key.
2. Assign a score for each answer (e.g., 0-5 points).
3. Provide specific feedback for each answer, mentioning strengths and areas for improvement.
4. At the end, calculate the total score and percentage.
5. Use clear, professional formatting.
6. If the answer is perfect, acknowledge it. If not, explain why points were deducted.
""",
    model=gemini_model
)

def run_grading_assistant():
    print("Welcome to the Grading Assistant!")
    while True:
        assignment = input("\nEnter the assignment name (or 'exit' to quit): ").strip()
        if assignment.lower() == 'exit':
            break

        print("\nPaste the answer key or rubric (press Enter twice to finish):")
        answer_key_lines = []
        while True:
            line = input()
            if line == '':
                break
            answer_key_lines.append(line)
        answer_key = '\n'.join(answer_key_lines)

        print("\nPaste the student's answers (press Enter twice to finish):")
        student_answer_lines = []
        while True:
            line = input()
            if line == '':
                break
            student_answer_lines.append(line)
        student_answers = '\n'.join(student_answer_lines)

        grading_prompt = (
            f"Assignment: {assignment}\n\n"
            f"Answer Key:\n{answer_key}\n\n"
            f"Student Answers:\n{student_answers}\n\n"
            "Grade the student's answers according to the answer key. Provide feedback and a total score."
        )
        grading_response = grading_assistant.run(grading_prompt)
        feedback = grading_response.content if grading_response else ""

        print("\nGrading Results:")
        print(feedback)

        cont = input("\nGrade another assignment? (y/n): ").lower()
        if cont != 'y':
            break

    print("\nSession Ended. Happy grading!")

if __name__ == "__main__":
    run_grading_assistant() 