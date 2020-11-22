# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age,sex,bmi,num_of_children,smoker,name):
  estimated_cost=250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for {name} is $".format(name=name) + str(estimated_cost) + " dollars.")
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28,0,26.2,3,0,"Maria")

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35,1,22.2,0,1,"Omar")


#difference function

def insurance_cost_diff(cost_a,cost_b):
  difference=cost_a-cost_b
  print("The difference in insurance cost is ${difference}".format(difference=difference))
  return difference

print(insurance_cost_diff(omar_insurance_cost,maria_insurance_cost))
