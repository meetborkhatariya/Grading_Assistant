import sys
from grader import grade_assignment
from batch import batch_grade
from export import export_results

def main():
    last_batch_results = []
    print("Welcome to the Modular Grading Assistant!")
    while True:
        print("\nMenu:")
        print("1. Grade a single assignment")
        print("2. Batch grade assignments")
        print("3. Export results")
        print("4. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            grade_assignment()
        elif choice == '2':
            last_batch_results = batch_grade()
        elif choice == '3':
            if last_batch_results:
                export_results(last_batch_results)
            else:
                print("No batch results to export. Please run batch grading first.")
        elif choice == '4':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 