# Add your code here
medical_costs={}
medical_costs["Marina"]=6607.0
medical_costs["Vinay"]=3225.0
medical_costs.update({"Connie":8886.0,"Isaac":16444.0,"Valentina":6420.0})
print(medical_costs)
medical_costs["Vinay"]=3325.0

total_cost=0
for item in medical_costs:
  total_cost+=medical_costs[item]

average_cost=total_cost/len(medical_costs)
print("Average Insurance Cost: {cost}".format(cost=average_cost))

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

zipped_ages=list(zip(names,ages))
print(zipped_ages)

names_to_ages={key:value for key, value in zipped_ages}
print(names_to_ages)

marina_age=names_to_ages.get("Marina",None)
print("Marina's age is {age}".format(age=marina_age))
medical_records = {}
medical_records["Marina"] = {"Age":27,"Sex":"Female","BMI":31.1, "Children": 2,"Smoker":"Non-smoker","Insurance_cost":6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(medical_records)

print("Connie's insurance cost is ${cost}".format(cost=medical_records["Connie"]['Insurance_cost']))

medical_records.pop('Vinay')
#print(medical_records)

for record in medical_records:
  print("{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of ${Insurance_cost}".format(Name=record,Age=medical_records[record]["Age"],Sex=medical_records[record]["Sex"],Smoker=medical_records[record]["Smoker"],BMI=medical_records[record]["BMI"],Insurance_cost=medical_records[record]["Insurance_cost"]))

print("")

def update_medical_records(name,attribute,value):
  medical_records[name][attribute]=value

update_medical_records('Marina','BMI',25)
print(medical_records)
