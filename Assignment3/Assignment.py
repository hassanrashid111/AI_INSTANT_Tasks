# Step 1: البيانات
customers = [
    "Ahmed", "Sara", "Omar", "Mona",
    "Ali", "Nour", "Youssef", "Hana",
    "Khaled", "Mariam", "Hassan", "Laila"
]
scores = [
    91, 45, 78, 66, 88, 30,
    72, 95, 51, 60, 84, 39
]

# Step 2: تصنيف العملاء
risk_levels = []

for i in range(len(customers)):
    score = scores[i]
    if score >= 85:
        risk_levels.append("High")
    elif score >= 60:
        risk_levels.append("Medium")
    else:
        risk_levels.append("Low")

# Step 3: حساب الإحصائيات
high_count = 0
medium_count = 0
low_count = 0
total_score = 0

for i in range(len(scores)):
    total_score = total_score + scores[i]
    if risk_levels[i] == "High":
        high_count = high_count + 1
    elif risk_levels[i] == "Medium":
        medium_count = medium_count + 1
    else:
        low_count = low_count + 1

average_score = total_score / len(scores)

# Step 4: إيجاد أفضل وأسوأ عميل 
best_name = customers[0]
best_score = scores[0]

worst_name = customers[0]
worst_score = scores[0]

for i in range(len(scores)):
    if scores[i] < best_score:
        best_score = scores[i]
        best_name = customers[i]
    if scores[i] > worst_score:
        worst_score = scores[i]
        worst_name = customers[i]

# Step 6: القائمة التفاعلية
choice = ""

while choice != "0":
    print("\n========== MENU ==========")
    print("1. Show All Customers")
    print("2. Search for a Customer")
    print("0. Exit")
    print("==========================")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Step 5: عرض التقرير
        print("\n========== CUSTOMER RISK REPORT ==========\n")
        print("Name       Score    Risk")
        print("------------------------------------------")
        for i in range(len(customers)):
            print(f"{customers[i]:<10} {scores[i]:<8} {risk_levels[i]}")

        print("\n=============== SUMMARY ================\n")
        print(f"High Risk:   {high_count}")
        print(f"Medium Risk: {medium_count}")
        print(f"Low Risk:    {low_count}")
        print(f"Average Score: {average_score:.2f}\n")
        print(f"Best Customer:  {best_name} ({best_score})")
        print(f"Worst Customer: {worst_name} ({worst_score})")

    elif choice == "2":
        search_name = input("Enter customer name: ")
        found = False

        for i in range(len(customers)):
            if customers[i].lower() == search_name.lower():
                print("Name:", customers[i])
                print("Score:", scores[i])
                print("Risk:", risk_levels[i])
                found = True
                break

        if found == False:
            print("Customer not found!")

    elif choice == "0":
        print("Goodbye!")

    else:
        print("Invalid choice!")