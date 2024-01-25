#1. GRADING PROGRAM
# program that converts student scores to grades.
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)


#2. Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Dortmund"], "total_visits": 6}
}

print(travel_log["France"])


#3. Nesting dictionary in a list
travel_log = [
    {
     "country_visited": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visits": 12
    },
    {
     "country_visited":"Germany",
     "cities_visited": ["Berlin", "Hamburg", "Dortmund"], 
     "total_visits": 6
    },
]

print(travel_log[0])
print(travel_log[1])


#4. Dictionary in a list
# PROGRAM 1

country = input("Add country name ") 
visits = int(input("Number of visits? ")) 
list_of_cities = eval(input("List of cities? ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# function that allows new countries to be added to the travel_log. 

def add_new_country(country, visits, list_of_cities):
    new_country_entry = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    travel_log.append(new_country_entry)

# adding_new_country   
add_new_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
#print(travel_log)


# PROGRAM 2

country = input("Add country name ") 
visits = int(input("Number of visits? ")) 
list_of_cities = eval(input("List of cities? ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# function that allows new countries to be added to the travel_log. 

def add_new_country(country, visits, list_of_cities):
    new_country_entry = {}
    new_country_entry["country"]: country
    new_country_entry["visits"]: visits
    new_country_entry["cities"]: list_of_cities
    
    travel_log.append(new_country_entry)

# adding_new_country   
add_new_country(country, visits, list_of_cities)

# Determine the index of the last added country
new_country_index = len(travel_log) - 1

# Display information about the new country
#print(f"I've been to {travel_log[new_country_index]['country']} {travel_log[new_country_index]['visits']} times.")
#print(f"My favourite city was {travel_log[new_country_index]['cities'][0]}.")
print(travel_log)
