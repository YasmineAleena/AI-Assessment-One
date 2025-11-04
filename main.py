import csv

Load dataset

def load_dataset(file_path):
dataset = []
with open(file_path, 'r') as f:
reader = csv.reader(f)
next(reader) # skip header if it exists
for row in reader:
dataset.append(row)
return dataset

Main RB AI function

def car_evaluation_ai(dataset, user_input):
classes = ['unacc', 'acc', 'good', 'vgood']
class_counts = {c: 0 for c in classes}
total_matches = 0

# Compare user input with each row in dataset
for data_row in dataset:
    match = True
    for i in range(len(user_input)):
        if user_input[i] != data_row[i]:
            match = False
            break
    if match:
        class_counts[data_row[-1]] += 1
        total_matches += 1

# Calculate percentages
if total_matches == 0:
    print("No matches found for your input.")
    return None

percentages = {c: (class_counts[c] / total_matches) * 100 for c in classes}
return percentages
Example usage

if name == "main":
dataset = load_dataset('car.data') # Replace with your dataset path
print("Enter your car preferences:")
buying = input("Buying price (vhigh, high, med, low): ").strip()
maint = input("Maintenance price (vhigh, high, med, low): ").strip()
doors = input("Number of doors (2, 3, 4, 5more): ").strip()
persons = input("Number of passengers (2, 4, more): ").strip()
lug_boot = input("Luggage size (small, med, big): ").strip()
safety = input("Safety rating (low, med, high): ").strip()

user_input = [buying, maint, doors, persons, lug_boot, safety]

results = car_evaluation_ai(dataset, user_input)
if results:
    print("\nEvaluation results (% breakdown):")
    for car_class, percent in results.items():
        print(f"{car_class}: {percent:.2f}%")