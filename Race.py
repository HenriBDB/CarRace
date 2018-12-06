import time

""" Creates a Race object with a welcome, start and finish function that takes in
    at track name and length, and a list of Car objects: racers"""

class Race:

    def __init__(self, track_name, track_length, racers):
        self.track_name = track_name
        self.cars = racers
        self.track_length = track_length
        self.winner = racers[0].get_name()

    def welcome_message(self):
        print(f"Welcome to {self.track_name}!")
        print("Make yourself comfortable,\n"
              "buy a hot dog and a drink,\n"
              "and get ready to witness today's race featuring: \n")
        time.sleep(1)
        for car in self.cars:
            print(car.get_name())
            time.sleep(1)
        print()

    def start(self):
        won = False
        race_progress = {}

        print("---- START! ----")
        print()
        time.sleep(1)

        while not won:
            for car in self.cars:
                car.move_forward()
                race_progress[car.get_name()] = car.get_distance_covered()
                if car.get_distance_covered() >= self.track_length:
                    won = True
            for key, value in reversed(sorted(race_progress.items(), key=lambda kv: kv[1])):
                if race_progress[self.winner] < value:
                    self.winner = key
                print("%s: %.2fm." % (key, value))
            print()
            time.sleep(1)

    def finish(self):
        print(f"Cogratulation to {self.winner} for winning the race!")
        print()
        print("We hope you enjoyed this race and will come to our next VINTGAGE race on Saturday!")
