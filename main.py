import csv

# Load dataset
def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dataset.append(row)
    return dataset

# RB AI function with blank-field support
def car_evaluation_ai(dataset, user_input):
    classes = ['unacc', 'acc', 'good', 'vgood']
    class_counts = {c: 0 for c in classes}
    total_matches = 0

    for data_row in dataset:
        match = True
        for i in range(len(user_input)):
            # Skip blank inputs (treated as "don't care")
            if user_input[i] and user_input[i] != data_row[i]:
                match = False
                break
        if match:
            class_counts[data_row[-1]] += 1
            total_matches += 1

    if total_matches == 0:
        print("No matches found for your input.")
        return None

    # Percentages are based on total matches, not total dataset
    percentages = {c: (class_counts[c] / total_matches) * 100 for c in classes}
    return percentages

# Main program
if __name__ == "__main__":
    dataset = load_dataset('car.csv')  # Make sure car.csv is in the same folder
    print("Enter your car preferences (leave blank if you don't care):")
    buying = input("Buying price (vhigh, high, med, low): ").strip()
    maint = input("Maintenance price (vhigh, high, med, low): ").strip()
    doors = input("Number of doors (2, 3, 4, 5more): ").strip()
    persons = input("Number of passengers (2, 4, more): ").strip()
    lug_boot = input("Luggage size (small, med, big): ").strip()
    safety = input("Safety rating (low, med, high): ").strip()

    user_input = [buying, maint, doors, persons, lug_boot, safety]

    results = car_evaluation_ai(dataset, user_input)
    if results:
        print("\nEvaluation results (% breakdown of matching instances):")
        for car_class, percent in results.items():
            print(f"{car_class}: {percent:.2f}%")

#ChatGPT. 2025. Python code for a Rule-Based Car Evaluation AI. Personal communication, 3 November 2025.