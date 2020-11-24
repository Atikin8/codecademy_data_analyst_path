names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262, 4816, 6839, 5054, 14724, 5360, 7640, 6072, 2750, 12064]

# Add your code here
names.append('Priscilla')
insurance_costs.append(8320)
#print(names)
medical_records=list(zip(names,insurance_costs))
print(medical_records)
num_medical_records=len(medical_records)

print('There are {num} medical records.'.format(num=num_medical_records))
first_medical_record=medical_records[0]
print('Here is the first medical record: {record}'.format(record=first_medical_record))
sorted_rec=sorted(medical_records, key=lambda record: record[1])
print('Here are the medical records sorted by insurance cost: : {sorted}'.format(sorted=sorted_rec))

cheapest_three=sorted_rec[:3]
print("Here are the 3 cheapest insurance costs in our medical records: {cheapest}".format(cheapest=cheapest_three))
priciest_three=sorted_rec[-3:]
print("Here are the 3 cheapest most expensive costs in our medical records: {exp}".format(exp=priciest_three))

occurences_paul=names.count('Paul')
print('There are {num} individuals with the name Paul in our medical records'.format(num=occurences_paul))
