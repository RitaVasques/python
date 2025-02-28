class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents
  
  def set_numberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents
  
  def __repr__(self):
    return "A {level} school named {name} with {numberOfStudents} students.".format(level=self.level, name=self.name, numberOfStudents=self.numberOfStudents)

print("_____ TEST SCHOOL_____")
a = School("School A", "high", 100)
print(a)
print(a.get_name())
print(a.get_level())
a.set_numberOfStudents(200)
print(a.get_numberOfStudents())
print("_______________________")

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickUpPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickUpPolicy = pickUpPolicy

  def get_pickUpPolicy(self):
    return self.pickUpPolicy
  
  def __repr__(self):
    general = super().__repr__()
    return general + " The pick up policy is {pickUpPolicy}".format(pickUpPolicy = self.pickUpPolicy)

print("_____ TEST PRIMARY SCHOOL_____")
b = PrimarySchool("Primary School B", 300, "Pickup Allowed")
print(b.get_pickUpPolicy())
print(b)
print("___________________________")

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    general = super().__repr__()
    return general + " The sports available are: {sportsTeams}".format(sportsTeams = self.sportsTeams)

print("_____ TEST HIGHSCHOOL_____")
c = HighSchool("HighSchool C", 500, ["Tennis", "Basketball"])
print(c.get_sportsTeams())
print(c)
print("___________________________")gir 