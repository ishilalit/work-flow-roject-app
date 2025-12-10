Minimal Workflow / Graph Engine

Nodes = Python functions

State passed between nodes

Edges define order of execution

Looping support

Basic branching support

Execution log returned as part of /graph/run

✔ Tool Registry

A simple dictionary where helper functions can be registered and used inside nodes.

✔ FastAPI Endpoints
Endpoint	Description
POST /graph/create	Create a workflow graph (nodes + edges)
POST /graph/run	Run the workflow with an initial state
GET /graph/state/{run_id}	Fetch current state of a workflow run
