import pytest
from data_sifter import Block, Connection, Workflow, validate_connections, save_workflow, load_workflow

def test_validate_connections():
    blocks = [Block('Start URL', 1), Block('Selector', 2)]
    connections = [Connection(1, 2)]
    workflow = Workflow(blocks, connections)
    assert validate_connections(workflow) == True

def test_validate_connections_invalid():
    blocks = [Block('Start URL', 1), Block('Selector', 2)]
    connections = [Connection(2, 1)]
    workflow = Workflow(blocks, connections)
    assert validate_connections(workflow) == False

def test_save_workflow():
    blocks = [Block('Start URL', 1), Block('Selector', 2)]
    connections = [Connection(1, 2)]
    workflow = Workflow(blocks, connections)
    json_data = save_workflow(workflow)
    assert json_data == '{"blocks": [{"type": "Start URL", "id": 1}, {"type": "Selector", "id": 2}], "connections": [{"from": 1, "to": 2}]}'

def test_load_workflow():
    json_data = '{"blocks": [{"type": "Start URL", "id": 1}, {"type": "Selector", "id": 2}], "connections": [{"from": 1, "to": 2}]}'
    workflow = load_workflow(json_data)
    assert len(workflow.blocks) == 2
    assert len(workflow.connections) == 1
