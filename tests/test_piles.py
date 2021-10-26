"""
test_structures: unit tests for piles structures
Corey Rayburn Yung <coreyrayburnyung@gmail.com>
Copyright 2020-2021, Corey Rayburn Yung
License: Apache-2.0 (https://www.apache.org/licenses/LICENSE-2.0)
"""
import dataclasses
import inspect 
import types

import piles


@dataclasses.dataclass
class Something(piles.Node):
    
    pass


@dataclasses.dataclass
class AnotherThing(piles.Node):
    
    pass


@dataclasses.dataclass
class EvenAnother(piles.Node):
    
    pass


def test_graph() -> None:
    edges = tuple([('a', 'b'), ('c', 'd'), ('a', 'd'), ('d', 'e')])
    dag = piles.System.create(item = edges)
    dag.add(node = 'cat')
    dag.add(node = 'dog', ancestors = 'e', descendants = ['cat'])
    adjacency = {
        'tree': {'house', 'yard'},
        'house': set(),
        'yard': set()}
    assert piles.Adjacency.__instancecheck__(adjacency)
    another_dag = piles.System.create(item = adjacency)
    dag.append(item = another_dag)
    print('test print dag', dag)
    return

def test_pipeline() -> None:
    
    return

def test_tree() -> None:
    
    return


if __name__ == '__main__':
    test_graph()
    test_pipeline()
    test_tree()
    