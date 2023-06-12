# ..........................Question1....................................
class Ankara:
    def __init__(self,temperature,mood):
        self.temperature=temperature
        self.mood=mood
    def predict_pattern_change(self):
        # if its hot ,one is happy
        if self.temperature > 30 and self.mood=="happy":
            return "The pattern will be dotted."
        # if its cold,one is sad
        elif self.mood=="sad" and self.temperature <30 :
            return "The pattern will be striped."
        elif self.temperature == 30 and self.mood=="neutral":
            return "The pattern will not change."
        # cater for mood input that is not happy,sad or neutral and for when one inputs neutral as mood but temperature is not between 11-29 
        else:
            return "Unable to predict changes"
        
wearer1=Ankara(31,"happy")  
print(wearer1.predict_pattern_change())#The pattern will be dotted.

wearer3=Ankara(29,"sad")  
print(wearer3.predict_pattern_change())#The pattern will be striped.

wearer5=Ankara(30,"neutral")  
print(wearer5.predict_pattern_change())#The pattern will not change.

wearer6=Ankara(35,"Neutral")  
print(wearer6.predict_pattern_change())#Unable to predict changes. 


# ..........................Question2....................................
class Migration:
    def __init__(self,weather_patterns,river_levels):
        self.weather_patterns=weather_patterns
        self.river_levels=river_levels
    def predict_migration(self):
        if self.weather_patterns=="wet" and self.river_levels=="high":
            return "Animal migration will be slow."
        elif self.weather_patterns=="dry" and self.river_levels=="low":
            return "Animal migration will be fast."
        else:
            return "Unable to predict changes."
        
zebra1=Migration("wet","high")
print(zebra1.predict_migration())#Animal migration will be slow.


zebra2=Migration("dry","low")
print(zebra2.predict_migration())#Animal migration will be fast.

zebra3=Migration("dry","high")
print(zebra3.predict_migration())#Unable to predict changes.


# ..........................Question3....................................
from datetime import datetime, timedelta

class Producer:
    def __init__(self, budget):
        self.budget = budget
        
class Movie:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

class Schedule:
    def __init__(self, movie, shooting_dates, shooting_location):
        self.movie = movie
        self.shooting_dates = shooting_dates
        self.shooting_location = shooting_location

# Budget
def check_budget(movie1,movie2):
    budget_sum = movie1.budget + movie2.budget
    if budget_sum <= producer1.budget:
        print(f"The sum of {movie1.name} and {movie2.name} budgets is within the producer's budget")
    else:
        print(f"The sum of {movie1.name} and {movie2.name} budgets is not within the producer's budget")


# Location conflict
def check_location_conflict(schedule1, schedule2):

    if schedule1.shooting_location != schedule2.shooting_location:
        return "The schedules don't clash because they have different locations"
    else:
        return f"Warning: {schedule1.movie.name} and {schedule2.movie.name} have conflicting shooting locations."
        

#Date conflict
def check_date_conflict(schedule1, schedule2):
    # Convert string dates to datetime objects for comparison
    date1 = datetime.strptime(schedule1.shooting_dates, '%d/%m/%Y')
    date2 = datetime.strptime(schedule2.shooting_dates, '%d/%m/%Y')

    # Check if there is a clash in shooting dates
    if abs(date1 - date2) < timedelta(days=1):
        print(f"Warning: {schedule1.movie.name} and {schedule2.movie.name} have conflicting shooting schedules.")
    else:
        print("No schedule conflicts found.")


# create instance of a producer's budget
producer1=Producer(10000)


# Creating Movie instances with different budgets
movie1 = Movie("A Wrinkle in Time", 500)
movie2 = Movie("Divergent", 750)

# Creating Schedule instances with different shooting locations and dates
schedule1 = Schedule(movie1, "20/05/2022", "Los Angeles")
schedule2 = Schedule(movie2, "20/05/2022", "Los Angeles")
check_budget(movie1,movie2)
check_date_conflict(schedule1, schedule2)
print(check_location_conflict(schedule1,schedule2))



# ..........................Question4....................................

class Baobab:
   def __init__(self,season):
       self.season=season


   def predictFruitType(self):
       if self.season == "dry":
          print("The fruit type is small and it has a power of 0")
       elif self.season == "wet":
           print("The fruit type is large and it has a power of 1")    
       else:
           print("Unable to predict changes")


   def predictEffect(self,power):
       if power==0:
          print("The person can fly")
       elif power==1:
           print("The person can sing")
       else:
           print("Unable to predict changes")
        

baobab1=Baobab("dry")
print(baobab1.predictFruitType())
print(baobab1.predictEffect(0))

baobab2=Baobab("wet")
print(baobab2.predictFruitType())
print(baobab2.predictEffect(1))

baobab3=Baobab("Wet")
print(baobab3.predictFruitType())
print(baobab3.predictEffect(12))

# ..........................Question5....................................

class Drum:
    def __init__(self,material,size):
        self.material=material
        self.size=size

    def make_sound(self,tone):
        return f"The drum which is made of {self.material} and is {self.size} makes a {tone} tone"
    
class Djembe(Drum):
    def __init__(self,material,size):
        self.material=material
        self.size=size
    def make_sound(self,tone):
        return f"The djembe which is made of {self.material} and is {self.size} makes a {tone} tone"
    
   
class TalkingDrum (Drum):
    def __init__(self,material,size):
        self.material=material
        self.size=size
    def make_sound(self,tone):
        return f"The talking drum which is made of {self.material} and is {self.size} makes a {tone} tone"
    

class Bougarabou(Drum):
    def __init__(self,material,size):
        self.material=material
        self.size=size
    def make_sound(self,tone):
        return f"The bougarabou which is made of {self.material} and is {self.size} makes a {tone} tone"
    


drum1 =Drum("hides","large")
print(drum1.make_sound("high"))

djembe=Djembe("wood","small")
print(djembe.make_sound("wide range of tones"))

talkingDrum=TalkingDrum("metal","medium")
print(talkingDrum.make_sound("human-like"))

bougarabou=Bougarabou("plastic","small")
print(bougarabou.make_sound("deep, rich bass"))


# option2
# same material and size
class Drum:
    def __init__(self,material,size) :
        self.material=material
        self.size = size
    def get_common_qualities(self):
        print(f"The {self.__class__.__name__} is {self.size} and is made of {self.material}.")
    def predict_sound(self):
        print(f"The {self.__class__.__name__} {self.sound}")
class Djembe1(Drum):
    sound=("produces a wide range of sound")
class TalkingDrum1(Drum):
    sound=("mimics lines of human speech")
class Bougarabou1(Drum):
    sound=("produces deep,rich base tones")


djembe2=Djembe1("wood","small")
print(djembe2.get_common_qualities())
print(djembe2.predict_sound())

talkingDrum2=TalkingDrum1("metal","medium")
print(talkingDrum2.predict_sound())
print(talkingDrum2.get_common_qualities())

bougarabou2=Bougarabou1("plastic","small")
print(bougarabou2.predict_sound())
print(bougarabou2.get_common_qualities())
