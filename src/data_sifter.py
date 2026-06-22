import json
from dataclasses import dataclass
from typing import List

@dataclass
class Block:
    type: str
    id: int

@dataclass
class Connection:
    from_block: int
    to_block: int

@dataclass
class Workflow:
    blocks: List[Block]
    connections: List[Connection]

def validate_connections(workflow: Workflow) -> bool:
    """Validate connections between blocks"""
    for connection in workflow.connections:
        from_block = next((block for block in workflow.blocks if block.id == connection.from_block), None)
        to_block = next((block for block in workflow.blocks if block.id == connection.to_block), None)
        if from_block is None or to_block is None:
            return False
        if from_block.type == 'Selector' and connection.from_block != connection.to_block - 1:
            return False
    return True

def save_workflow(workflow: Workflow) -> str:
    """Save workflow to JSON"""
    data = {
        'blocks': [{'type': block.type, 'id': block.id} for block in workflow.blocks],
        'connections': [{'from': connection.from_block, 'to': connection.to_block} for connection in workflow.connections]
    }
    return json.dumps(data)

def load_workflow(json_data: str) -> Workflow:
    """Load workflow from JSON"""
    data = json.loads(json_data)
    blocks = [Block(block['type'], block['id']) for block in data['blocks']]
    connections = [Connection(connection['from'], connection['to']) for connection in data['connections']]
    return Workflow(blocks, connections)
