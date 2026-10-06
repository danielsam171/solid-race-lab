[1mdiff --git a/exercises/ex2_ocp.py b/exercises/ex2_ocp.py[m
[1mindex d7d1d6f..5590722 100644[m
[1m--- a/exercises/ex2_ocp.py[m
[1m+++ b/exercises/ex2_ocp.py[m
[36m@@ -23,9 +23,12 @@[m [mRun it to watch the race:[m
 Check your work:[m
     pytest tests/test_ex2_ocp.py -v[m
 """[m
[32m+[m
[32m+[m[32mimport random[m
 from engine.track import Track[m
 [m
 [m
[32m+[m
 class Vehicle:[m
     """Base type every racer in this exercise extends."""[m
 [m
[36m@@ -58,7 +61,7 @@[m [mclass Motorcycle(Vehicle):[m
 [m
     def move(self) -> None:[m
         # TODO(OCP): move forward by a varying, sometimes-large amount.[m
[31m-        raise NotImplementedError("Implement Motorcycle.move()")[m
[32m+[m[32m        self.position += random.randint(1, 9)[m
 [m
 [m
 class Bicycle(Vehicle):[m
[36m@@ -67,11 +70,14 @@[m [mclass Bicycle(Vehicle):[m
     def __init__(self, name: str):[m
         super().__init__(name)[m
         # TODO(OCP): add any state you need to track fatigue over time.[m
[32m+[m[32m        self.ticks = 0[m
 [m
     def move(self) -> None:[m
         # TODO(OCP): move forward by a shrinking amount as ticks go by[m
         # (never less than 1).[m
[31m-        raise NotImplementedError("Implement Bicycle.move()")[m
[32m+[m[32m        step = max(1, 5 - self.ticks // 4)[m
[32m+[m[32m        self.position += step[m
[32m+[m[32m        self.ticks += 1[m
 [m
 [m
 def main():[m
