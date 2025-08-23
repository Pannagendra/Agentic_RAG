import typer
from src.graph import build_graph

app = typer.Typer()

@app.command()
def query(query: str):
    workflow = build_graph()
    result = workflow.invoke({"query": query})
    print("Answer:", result["answer"])

if __name__ == "__main__":
    app()
