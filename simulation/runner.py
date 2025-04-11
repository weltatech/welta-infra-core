# simulation/runner.py

from infra.workflow import InfrastructureNode

def run_simulation():
    nodes = [
        InfrastructureNode(region="Singapore", zoning_level="Tier-1"),
        InfrastructureNode(region="Berlin", zoning_level="Tier-2"),
        InfrastructureNode(region="Dubai", zoning_level="Special-Economic-Zone")
    ]

    for node in nodes:
        node.ingest_data("mock_registry_source")
        node.align_with_ai()
        node.deploy()
        print(f"STATUS: {node.status()}")
        print("-" * 40)

if name == "__main__":
    run_simulation()
