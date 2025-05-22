class WorkoutPlan:
    def __init__(self, plan_type):
        self.plan_type = plan_type

    def show_plan(self):
        print(f"Workout Plan: {self.plan_type}")

class Trainer:
    def __init__(self, name, workout_plan):
        self.name = name
        self.workout_plan = workout_plan

    def assign_plan(self):
        print(f"Trainer {self.name} assigned this plan:")
        self.workout_plan.show_plan()

# Create a workout plan
plan = WorkoutPlan("Full-body strength training")
plan2 = WorkoutPlan("Strength training")
plan3 = WorkoutPlan("Fast training")

# Create a trainer and assign the plan
trainer = Trainer("Stan", plan)
trainer2 = Trainer("David", plan2)
trainer3 = Trainer("Sarah", plan3)

# Use the method
trainer.assign_plan()
trainer2.assign_plan()
trainer3.assign_plan()