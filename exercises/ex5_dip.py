"""
Exercise 5 - Dependency Inversion Principle (DIP)

Race below is a high-level policy ("how to run a race") that is hard-
wired to two concrete, low-level vehicle classes: it builds its own
SportsCar and DeliveryVan inside __init__. Racing a different roster
today means editing Race itself -- exactly what DIP says we should
avoid.

YOUR TASK:
  1. Refactor Race so it receives its racers through the constructor
     (store them as `self.racers`) instead of creating them itself.
     Race must not import or know about SportsCar/DeliveryVan/RocketSled
     at all -- any object satisfying the Racer contract from
     `engine.track` (name, symbol, position, move()) should work.
  2. Add a `RocketSled` vehicle class (any speed you like).
  3. In main(), build two different rosters and run Race with each,
     proving you never had to touch Race to change who races.

Run it to see the race(s):
    python -m exercises.ex5_dip

Check your work:
    pytest tests/test_ex5_dip.py -v
"""
from engine.track import Track


class SportsCar:
    symbol = "\U0001F3CE"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 6


class DeliveryVan:
    symbol = "\U0001F690"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 3


class RocketSled:
    symbol = "🚀"

    def __init__(self, name: str, speed: int = 5):
        self.name = name
        self.speed = speed
        self.position = 0

    def move(self) -> None:
        self.position += self.speed


class Race:
    """High-level policy refactored: depends only on the injected racers."""

    def __init__(self, racers, track=None):
        self.racers = racers
        self.track = track if track is not None else Track(length=30)

    def start(self):
        return self.track.run(self.racers)


def main():
    # Carrera 1
    roster_1 = [SportsCar("Flash"), DeliveryVan("Steady Eddie")]
    race_1 = Race(racers=roster_1)
    race_1.start()

    # Carrera 2 (usando RocketSled)
    roster_2 = [RocketSled("Apollo"), SportsCar("Red Bullet")]
    race_2 = Race(racers=roster_2)
    race_2.start()


if __name__ == "__main__":
    main()