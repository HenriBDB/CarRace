from Car import Car
from Race import Race

""" A simple car racing program where several cars race against
    each other and print out the race's progress.
    
    @author Henri Boistel de Belloy
    @version 1.0 """

# Create the cars
cico = Car("Cico", "BMW", "Matte Black", 330)
henri = Car("Henri", "VW", "Red", 120)
william = Car("William", "Mercedes", "Grey", 300)
old_jaguar = Car("Vintage", "Jaguar", "Black" ,100)


# Create a list of all the racers and put them in a race.
racers = [cico, henri, william, old_jaguar]
race = Race("Rio de Janeiro", 1000, racers)

# Run the race
race.welcome_message()
race.start()
race.finish()