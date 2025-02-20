#People for game night
gamers = []

#Add gamers to the list above
def add_gamer(gamer, gamers_list):
  if "name" in gamer and "availability" in gamer:
    gamers_list.append(gamer)

kimberly = {"name" : "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

#Get availability per day of the week
def build_daily_frequency_table():
  days_of_week = []
  frequency = {}
  for gamer in gamers:
      days_of_week += gamer.get("availability")
  for day in days_of_week:
     frequency[day] = days_of_week.count(day)
  return frequency

count_availability = build_daily_frequency_table()

#Find the day of the week with heigher availability
#max(parameter) will look for max in keys, wee need it to look for max in values
def find_best_night(availability_table):
  return max(availability_table, key=availability_table.get)

game_night = find_best_night(count_availability)

#People available on game_night
def available_on_night(gamers_list, day):
  people = []
  for gamer in gamers_list:
    if day in gamer.get("availability"):
      people.append(gamer.get("name"))
  return people

attending_game_night = available_on_night(gamers, game_night)

#Email template for participants
form_email = "Hello {}, we can`t wait to see you on {}, to play {}"

def send_email(gamers_who_can_attend, day, game):
  for index in range(len(gamers_who_can_attend)):
    print(form_email.format(gamers_who_can_attend[index], day, game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")
