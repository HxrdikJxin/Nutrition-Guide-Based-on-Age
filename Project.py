# --------------------------------------------
# Nutrition Guide Based on Age
# Python Project for B.Tech First Year
# --------------------------------------------

def get_age_group(age):
    """Classify age into a specific group."""
    if 1 <= age <= 3:
        return "Toddlers (1-3 years)"
    elif 4 <= age <= 12:
        return "Children (4-12 years)"
    elif 13 <= age <= 19:
        return "Teenagers (13-19 years)"
    elif 20 <= age <= 39:
        return "Adults (20-39 years)"
    elif 40 <= age <= 59:
        return "Middle-aged Adults (40-59 years)"
    elif age >= 60:
        return "Senior Citizens (60+ years)"
    else:
        return None


def get_food_recommendations(age_group):
    """Return food recommendations based on age group."""
    recommendations = {
        "Toddlers (1-3 years)": [
            "Mashed fruits (banana, apple)",
            "Boiled vegetables",
            "Milk and dairy",
            "Soft cooked rice and lentils"
        ],
        "Children (4-12 years)": [
            "Whole grains (chapati, oats)",
            "Vegetables and fruits",
            "Protein foods (eggs, dal, paneer)",
            "Milk or dairy products"
        ],
        "Teenagers (13-19 years)": [
            "High-protein foods (eggs, chicken, soy)",
            "Calcium-rich foods (milk, paneer)",
            "Iron-rich foods (spinach, beans)",
            "Healthy snacks (nuts, fruits)"
        ],
        "Adults (20-39 years)": [
            "Balanced diet with carbs, protein, healthy fats",
            "Fresh vegetables and fruits",
            "Lean protein (fish, chicken, tofu)",
            "Plenty of water and whole grains"
        ],
        "Middle-aged Adults (40-59 years)": [
            "Fiber-rich foods (whole grains, leafy veggies)",
            "Low-fat dairy",
            "Heart-healthy fats (olive oil, nuts)",
            "Foods low in salt and sugar"
        ],
        "Senior Citizens (60+ years)": [
            "Easily digestible foods",
            "Calcium and Vitamin D rich items",
            "Light protein (dal, eggs, fish)",
            "Fruits and soft-cooked vegetables"
        ]
    }

    return recommendations.get(age_group, [])


def main():
    print("===================================")
    print("     NUTRITION GUIDE PROGRAM")
    print("===================================\n")

    try:
        age = int(input("Enter your age: "))

        age_group = get_age_group(age)
        if age_group is None:
            print("\nInvalid age entered. Age must be above 0.")
            return

        print(f"\nAge Group: {age_group}")
        print("Recommended Foods:")

        foods = get_food_recommendations(age_group)
        for food in foods:
            print(f" - {food}")

    except ValueError:
        print("\nPlease enter a valid number for age.")

    print("\nThank you for using the Nutrition Guide!")
  
main()
