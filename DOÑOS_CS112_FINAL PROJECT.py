import time
import turtle

# Class to store user information
class UserInfo:
    def __init__(self, age, gender, weight_kg, height_cm, activity_level, goal):
        self.age = age
        self.gender = gender.lower()
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.activity_level = activity_level.lower()
        self.goal = goal.lower()

# Class to calculate daily calories
class DailyCalorieCalculator:
    def __init__(self, user_info):
        self.user_info = user_info
        self.ACTIVITY_LEVELS = {
            "sedentary": 1.2,
            "lightly active": 1.375,
            "moderately active": 1.55,
            "very active": 1.725,
            "athletic": 1.9
        }
        self.GENDER_FACTORS = {
            "male": 5,
            "female": -161
        }

    def calculate_bmr(self):
        # Calculate Basal Metabolic Rate (BMR)
        return (10 * self.user_info.weight_kg) + (6.25 * self.user_info.height_cm) - (5 * self.user_info.age) + self.GENDER_FACTORS[self.user_info.gender]

    def calculate_daily_calories(self):
        # Calculate daily calories based on BMR and activity level
        bmr = self.calculate_bmr()
        calorie_multiplier = self.ACTIVITY_LEVELS.get(self.user_info.activity_level, None)
        if calorie_multiplier is None:
            raise ValueError("Invalid activity level. Choose one of: sedentary, lightly active, moderately active, very active, athletic.")

        daily_calories = bmr * calorie_multiplier

        # Adjust calories based on goals
        if self.user_info.goal == 'lose':
            daily_calories -= 500
        elif self.user_info.goal == 'gain':
            daily_calories += 500

        return round(daily_calories, 2)

# Class to calculate macronutrients
class MacronutrientCalculator:
    def calculate_macros(self, daily_calories, goal):
        # Calculate macronutrient distribution based on user's goal
        if goal == 'loss':
            protein_percentage = 0.30
            fat_percentage = 0.25
            carb_percentage = 0.45
        elif goal == 'maintain':
            protein_percentage = 0.25
            fat_percentage = 0.30
            carb_percentage = 0.45
        elif goal == 'gain':
            protein_percentage = 0.35
            fat_percentage = 0.25
            carb_percentage = 0.40
        else:
            raise ValueError("Invalid goal. Choose from: loss, maintain, gain.")

        protein_calories = daily_calories * protein_percentage
        fat_calories = daily_calories * fat_percentage
        carb_calories = daily_calories * carb_percentage

        protein_grams = protein_calories / 4
        fat_grams = fat_calories / 9
        carb_grams = carb_calories / 4

        return round(protein_grams, 2), round(fat_grams, 2), round(carb_grams, 2)

# Function to collect user input
def get_user_input():
    print("Welcome to the Daily Calorie and Macronutrient Calculator!")

    age = 0
    gender = ""
    weight_kg = 0.0
    height_cm = 0.0
    activity_level = ""
    goal = ""

    # Get age from the user with input validation
    while True:
        try:
            age = int(input("Enter your age: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid age (numeric).")

    # Get gender from the user with input validation
    while True:
        gender = input("Enter your gender (male/female): ").lower()
        if gender in ["male", "female"]:
            break
        else:
            print("Invalid input. Please enter 'male' or 'female'.")

    # Get weight from the user with input validation
    while True:
        try:
            weight_kg = float(input("Enter your weight in kilograms: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid weight (numeric).")

    # Get height from the user with input validation
    while True:
        try:
            height_cm = float(input("Enter your height in centimeters: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid height (numeric).")

    # Get activity level from the user with input validation
    while True:
        activity_level = input("Enter your activity level (sedentary/lightly active/moderately active/very active/athletic): ").lower()
        if activity_level in ["sedentary", "lightly active", "moderately active", "very active", "athletic"]:
            break
        else:
            print("Invalid input. Please choose from the provided options.")

    # Get goal from the user with input validation
    while True:
        goal = input("Enter your goal (lose/maintain/gain): ").lower()
        if goal in ["lose", "maintain", "gain"]:
            break
        else:
            print("Invalid input. Please choose from the provided options.")

    # Return UserInfo
    return UserInfo(age, gender, weight_kg, height_cm, activity_level, goal)

# Function to draw background using Turtle
def draw_background(gender, age, weight_kg, height_cm, activity_level, daily_calories, protein, fat, carb):
    screen = turtle.Screen()
    screen.title("Daily Calorie Calculator Results")
    screen.bgcolor("lightgray")

    turtle.penup()
    turtle.goto(-200, 160)
    turtle.pendown()
    turtle.color("black")
    turtle.write("User Information:", font=("Arial", 14, "bold"))
    turtle.penup()
    turtle.goto(-200, 130)
    turtle.pendown()
    turtle.write(f"Gender: {gender.capitalize()}", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.write(f"Age: {age} years", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, 70)
    turtle.pendown()
    turtle.write(f"Weight: {weight_kg} kg", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, 40)
    turtle.pendown()
    turtle.write(f"Height: {height_cm} cm", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, 10)
    turtle.pendown()
    turtle.write(f"Activity Level: {activity_level.capitalize()}", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, -20)
    turtle.pendown()
    turtle.write("Your estimated daily calorie requirement is:", font=("Arial", 14, "bold"))
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.write(f"{round(daily_calories, 2)} calories", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, -80)
    turtle.pendown()
    turtle.write("Macronutrient Distribution:", font=("Arial", 14, "bold"))
    turtle.penup()
    turtle.goto(-200, -110)
    turtle.pendown()
    turtle.write(f"Protein: {round(protein, 2)} grams", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, -140)
    turtle.pendown()
    turtle.write(f"Fat: {round(fat, 2)} grams", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, -170)
    turtle.pendown()
    turtle.write(f"Carbohydrates: {round(carb, 2)} grams", font=("Arial", 14, "normal"))
    turtle.penup()

    turtle.done()

def main():
    user_info = get_user_input()

    calorie_calculator = DailyCalorieCalculator(user_info)
    daily_calories = calorie_calculator.calculate_daily_calories()

    macronutrient_calculator = MacronutrientCalculator()
    protein, fat, carb = macronutrient_calculator.calculate_macros(daily_calories, user_info.goal)

    # Print user information and results
    print("\nUser Information:")
    time.sleep(0.2)
    print("Gender:", user_info.gender.capitalize())
    time.sleep(0.2)
    print("Age:", user_info.age, "years")
    time.sleep(0.2)
    print("Weight:", user_info.weight_kg, "kg")
    time.sleep(0.2)
    print("Height:", user_info.height_cm, "cm")
    time.sleep(0.2)
    print("Activity Level:", user_info.activity_level.capitalize())
    time.sleep(0.2)

    print("\nYour estimated daily calorie requirement is:", daily_calories, "calories.")
    time.sleep(0.2)
    print("\nMacronutrient Distribution:")
    time.sleep(0.2)
    print("Protein: {} grams".format(protein))
    time.sleep(0.2)
    print("Fat: {} grams".format(fat))
    time.sleep(0.2)
    print("Carbohydrates: {} grams".format(carb))

    # Draw the background using Turtle graphics
    draw_background(user_info.gender, user_info.age, user_info.weight_kg, user_info.height_cm, user_info.activity_level, daily_calories, protein, fat, carb)

main()