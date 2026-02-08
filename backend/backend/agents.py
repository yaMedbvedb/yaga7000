def planner(task):
    return f"План выполнения задачи: {task}"

def executor(plan):
    return f"Выполнение плана: {plan}"

def memory(result):
    return f"Результат сохранён: {result}"

def run_agent(user_input):
    plan = planner(user_input)
    execution = executor(plan)
    memory_result = memory(execution)

    return f"""
🧠 PLAN:
{plan}

⚙ EXECUTION:
{execution}

💾 MEMORY:
{memory_result}
"""
