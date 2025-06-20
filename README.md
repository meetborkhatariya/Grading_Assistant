# Modular Grading Assistant

A simple, modular tool for teachers and educators to grade assignments, batch process results, and export grades.

## Features

- Grade single assignments
- Batch grade multiple students
- Export results to CSV
- User-friendly command-line interface

## Setup

1. Clone or download this repository.
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. (Optional) If using AI features, add your API key to a `.env` file:
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

## Usage

Run the assistant from your terminal:

```sh
python grading_assistant/main.py
```

Follow the prompts to enter the answer key and student answers. Use the menu to grade, batch grade, or export results.

## License

MIT
