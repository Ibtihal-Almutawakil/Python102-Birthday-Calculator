import datetime

# Function to validate the date
def validate_date(date_str):
    """This function checks if the input date is valid"""
    try:
        # Split the date into day, month, year
        day, month, year = map(int, date_str.split('-'))
        
        # Check if month is between 1 and 12
        if month < 1 or month > 12:
            return False
        
        # Check if day is between 1 and 31
        if day < 1 or day > 31:
            return False
        
        # Check if the year is a positive number
        if year < 1:
            return False
        
        # Try to create a datetime object to see if the date is valid
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        # If there is an error, the date is not valid
        return False

# Function to calculate the age of a person
def calculate_age(birth_date):
    """This function calculates age based on the birth date"""
    today = datetime.datetime(2021, 1, 1)  # Date fixed for this program
    # Convert the birth_date string into a datetime object
    birth_date = datetime.datetime.strptime(birth_date, "%d-%m-%Y")
    
    # Calculate the age
    age = today.year - birth_date.year
    
    # If the current month and day is before the birth month and day, subtract 1 from age
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
        
    return age

# Function to find the day of the week for the birth date
def day_of_week(birth_date):
    """This function returns the day of the week for the birth date"""
    # Convert the birth_date string into a datetime object
    birth_date = datetime.datetime.strptime(birth_date, "%d-%m-%Y")
    
    # Use strftime to get the day of the week
    return birth_date.strftime('%A')

# Main function that controls the program flow
def main():
    people = []  # List to store the people's details
    
    # Loop to get input for multiple people
    while True:
        name = input("Enter name (or 'done' to finish): ")
        if name.lower() == 'done':  # If the user types 'done', stop asking for names
            break
        
        # Get the birth date from the user
        birth_date = input(f"Enter birth date for {name} (dd-mm-yyyy): ")
        
        # Check if the entered birth date is valid
        if not validate_date(birth_date):
            print(f"Invalid date for {name}. Please enter a valid date.")
            continue
        
        # Calculate the age and day of the week
        age = calculate_age(birth_date)
        day_of_birth = day_of_week(birth_date)
        
        # Add the person's details to the people list
        people.append({
            'name': name,
            'birth_date': birth_date,
            'age': age,
            'day_of_birth': day_of_birth
        })
    
    # If there's only one person, we don't need to calculate oldest or youngest
    if len(people) == 1:
        print("There is no oldest or youngest person.")
    else:
        # Find the oldest and youngest person
        oldest = max(people, key=lambda p: p['age'])
        youngest = min(people, key=lambda p: p['age'])
        print(f"The oldest one is {oldest['name']}")
        print(f"The youngest one is {youngest['name']}")
    
    # Print information about each person
    for person in people:
        print(f"{person['name']} is {person['age']} years old and she/he was born on {person['day_of_birth']}")
    
    print(f"Total People: {len(people)}")
    
    # Sort people by age from oldest to youngest
    people_sorted = sorted(people, key=lambda p: p['age'], reverse=True)
    print("\nPeople sorted by age (oldest to youngest):")
    for person in people_sorted:
        print(f"{person['name']} - {person['age']} years")
    
    # Print people born on Sunday
    print("\nPeople born on Sunday:")
    for person in people:
        if person['day_of_birth'] == "Sunday":
            print(person['name'])

# Run the program
if __name__ == "__main__":
    main()
