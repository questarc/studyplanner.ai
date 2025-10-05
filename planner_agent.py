from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

def collect_subjects(state):
    subjects = state["subjects"]
    exams = state["exams"]
    return {"subjects": subjects, "exams": exams}

def generate_plan(state):
    subjects = state["subjects"]
    exams = state["exams"]
    plan = {}
    for subject in subjects:
        days_left = exams.get(subject, 7)
        plan[subject] = [f"Day {i+1}: Study {subject}" for i in range(days_left)]
    return {"plan": plan}

def motivate(state):
    from utils.quotes import get_motivational_quote
    return {"quote": get_motivational_quote()}

graph = StateGraph()
graph.add_node("collect", RunnableLambda(collect_subjects))
graph.add_node("plan", RunnableLambda(generate_plan))
graph.add_node("motivate", RunnableLambda(motivate))

graph.add_edge("collect", "plan")
graph.add_edge("plan", "motivate")
graph.set_entry_point("collect")

study_planner_agent = graph.compile()
