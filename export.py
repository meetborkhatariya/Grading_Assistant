import csv

def export_results(results):
    filename = 'batch_results.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Score', 'Answers'])
        for name, score, answers in results:
            writer.writerow([name, score, ','.join(answers)])
    print(f"Results exported to {filename}") 