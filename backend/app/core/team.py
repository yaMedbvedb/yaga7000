class Planner:
    def think(self, goal):
        return f"Plan steps for: {goal}"

class Developer:
    def execute(self, plan):
        return f"Executed: {plan}"

class Critic:
    def review(self, result):
        return f"Review: {result}"

class AutoTeam:
    def __init__(self):
        self.planner = Planner()
        self.dev = Developer()
        self.critic = Critic()

    def run(self, goal):
        plan = self.planner.think(goal)
        result = self.dev.execute(plan)
        review = self.critic.review(result)

        return {
            "goal": goal,
            "plan": plan,
            "result": result,
            "review": review
        }
