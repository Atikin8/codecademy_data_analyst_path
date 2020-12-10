class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def patient_profile(self):
    patient_information={"name":self.name,
    "age":self.age,
    "sex":self.sex,
    "bmi":self.bmi,
    "num_of_children":self.num_of_children,
    "smoker":self.smoker}
    print(patient_information)

  def estimated_insurance_cost(self):
    estimated_cost=250*self.age-128*self.sex+370*self.bmi+425*self.num_of_children+24000*self.smoker - 12500
    print("{Name}'s estimated insurance cost is ${est_cost:,}.dollars".format(Name=self.name,est_cost=estimated_cost))

  def update_age(self,new_age):
    self.age = new_age
    print("{Name} is now {Age} years old".format(Name=self.name,Age=self.age))
    self.estimated_insurance_cost()
  
  def update_num_children(self,new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children>1:
      print("{Name} has {num_child} children".format(Name=self.name,num_child=self.num_of_children))
    else:
      print("{Name} has {num_child} child".format(Name=self.name,num_child=self.num_of_children))
      self.estimated_insurance_cost()
  
    # add more parameters here
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)

patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)
patient1.patient_profile()
