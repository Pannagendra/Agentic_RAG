# src/graph.py
from langgraph.graph import StateGraph, END
from langchain_community.llms import Ollama
from typing import TypedDict

# Use the updated langchain-ollama package (preferred):
# from langchain_ollama import OllamaLLM
# llm = OllamaLLM(model="llama3.1:8b")

llm = Ollama(model="llama3.1:8b")

class GraphState(TypedDict):
    query: str
    answer: str

def build_graph():
    workflow = StateGraph(GraphState)

    def query_node(state: GraphState):
        response = llm.invoke(state["query"])
        return {"answer": response}

    workflow.add_node("query", query_node)
    workflow.set_entry_point("query")
    workflow.add_edge("query", END)

    return workflow.compile()
