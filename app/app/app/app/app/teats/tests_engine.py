import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def pretty_print(title, data):
    print("\n" + "="*50)
    print(title)
    print("="*50)
    print(json.dumps(data, indent=4))
    print("\n")


def test_workflow_engine():
    # 1️⃣ Create Graph
    create_payload = {
        "nodes": {
            "extract": "app.workflows.code_review.extract_functions",
            "complexity": "app.workflows.code_review.check_complexity",
            "issues": "app.workflows.code_review.detect_issues",
            "improve": "app.workflows.code_review.suggest_improvements"
        },
        "edges": {
            "extract": "complexity",
            "complexity": "issues",
            "issues": "improve",
            "improve": "extract"
        }
    }

    print("➡️ Creating graph...")
    create_res = requests.post(f"{BASE_URL}/graph/create", json=create_payload)
    create_data = create_res.json()
    pretty_print("Graph Created", create_data)

    graph_id = create_data["graph_id"]

    # 2️⃣ Run Workflow
    run_payload = {
        "graph_id": graph_id,
        "initial_state": {
            "code": "def a(): pass\ndef b(): pass",
            "threshold": 3
        }
    }

    print("➡️ Running workflow...")
    run_res = requests.post(f"{BASE_URL}/graph/run", json=run_payload)
    run_data = run_res.json()
    pretty_print("Workflow Run Result", run_data)

    run_id = run_data["run_id"]

    # 3️⃣ Fetch Current State
    print("➡️ Fetching workflow state...")
    state_res = requests.get(f"{BASE_URL}/graph/state/{run_id}")
    state_data = state_res.json()
    pretty_print("Current Workflow State", state_data)


if __name__ == "__main__":
    print("🔥 Starting test of Workflow Engine...\n")
    test_workflow_engine()
