
#---------------------------------------------------
# Application: Filtering patients with High Diabetes Risk
#---------------------------------------------------
patient_names = ["Alice", "Bob", "Charlie", "David", "Ted", "Sam", "Jennifer", "Tom"]
glucose_levels = [140, 155, 130, 180, 200, 160, 120, 190]

#---------------------Method 1---------------------
#Create list of high risk patient names with their levels
high_risk_patients = []
#Loop through glucose_levels and identify if a person's level is greater than 150
for i in range(len(patient_names)):
    # If greater than 150, add the person's name and glucose level to "high risk patients" list
    if glucose_levels[i] > 150:
        high_risk_patients.append([glucose_levels[i],patient_names[i]])

#Sort the patients from highest to lowest risk and print
high_risk_patients.sort(reverse=True)
print(high_risk_patients)

#---------------------Method 2: List comprehensions---------------------
#high_risk_patients = [[glucose_levels[i], patient_names[i]] for i in range(len(patient_names)) if glucose_levels[i] > 150].sort(reverse=True) #will give error
#high_risk_patients.sort(reverse=True)
high_risk_patients = sorted([[glucose_levels[i], patient_names[i]] for i in range(len(patient_names)) if glucose_levels[i] > 150])
print(high_risk_patients)

#---------------------Method 3: enumerate() for loop ---------------------
high_risk_patients = []
for i, glucose in enumerate(glucose_levels):
    if glucose > 150:
        high_risk_patients.append([glucose, patient_names[i]])

# Sorting the list in descending order (permanent)
high_risk_patients.sort(reverse=True)
print(high_risk_patients)

#List comprehension exercise - convert the enumerate for loop into a list comprehension



#---------------------Method 4: zip() function ---------------------
high_risk_patients = []
for glucose, name in zip(glucose_levels, patient_names):
    if glucose > 150:
        high_risk_patients.append([glucose, name])

# Sorting in descending order permanently
high_risk_patients.sort(reverse=True)

#List comprehension exercise - convert the zip() for loop into a list comprehension
high_risk_patients = [[glucose, name] for glucose, name in zip(glucose_levels, patient_names) if glucose > 150]

#-------------------- Method 5: enumerate()---------------------
for i, glucose in enumerate(glucose_levels):
    if glucose > 150:
        patient_names[i] += " (High Risk)"  # Append label to name
        glucose_levels[i] = min(glucose, 200)  # Cap glucose at 200

print(patient_names)
print(glucose_levels)
#Combine the modified patient_names and glucose_levels lists by element (first patient name corresponds to first glucose level etc.).
# Can directly create a nested list without a for loop or append().
modified_patient_info = sorted(list(zip(glucose_levels, patient_names)), reverse=True) #can directly add sorted(), but cannot do .sort(). Why?
print(modified_patient_info)
#zip() automatically combines multiple lists by element but it returns a tuple with paired tuples for each item. Tuples are immutable so convert it to a list by using list() around the zip() expression.

#------------------------------------------------------------------------------
# Application with dictionaries
#------------------------------------------------------------------------------
patient_names = ["Alice", "Bob", "Charlie", "David", "Ted", "Sam", "Jennifer", "Tom"]
glucose_levels = [140, 155, 130, 180, 200, 160, 120, 190]

patients_dict = {"Alice":140, "Bob":155, "Charlie": 130, "David": 180,
                 "Ted":200, "Sam": 160, "Jennifer": 120, "Tom":190}

high_risk_patients = []
for name,glucose in patients_dict.items():
    if glucose > 150:
        high_risk_patients.append([glucose, name])
print(high_risk_patients)

#-------------------- Dictionary Method 2----------------------
patients_dict2 = dict(zip(patient_names, glucose_levels))
print(patients_dict2)
high_risk_patients = [[glucose, name] for name,glucose in patients_dict.items() if glucose > 150]
print(high_risk_patients)
