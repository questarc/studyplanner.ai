from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from typing import TypedDict, List, Dict

class PlannerState(TypedDict):
    subjects: List[str]
    exams: Dict[str, int]
    plan: Dict[str, List[str]]
    quote: str

def collect_subjects(state: PlannerState) -> PlannerState:
    return {"subjects": state["subjects"], "exams": state["exams"]}

def generate_plan(state: PlannerState) -> PlannerState:
    subjects = state["subjects"]
    exams = state["exams"]
    plan = {}
    for subject in subjects:
        days_left = exams.get(subject, 7)
        plan[subject] = [f"Day {i+1}: Study {subject}" for i in range(days_left)]
    return {"plan": plan}

def motivate(state: PlannerState) -> PlannerState:
    from utils.quotes import get_motivational_quote
    return {"quote": get_motivational_quote()}

graph = StateGraph(PlannerState)
graph.add_node("collect", RunnableLambda(collect_subjects))
graph.add_node("plan", RunnableLambda(generate_plan))
graph.add_node("motivate", RunnableLambda(motivate))

graph.add_edge("collect", "plan")
graph.add_edge("plan", "motivate")
graph.set_entry_point("collect")

study_planner_agent = graph.compile()
