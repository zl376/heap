import pytest

from Heap.Heap import Heap
import heapq
from copy import deepcopy



test_data_1 = [
    [(2, 1), (-5, 2), (1, 9), (-2, -5), (0, -8), (3, 2), (-100, 100), (100, -100)],
]

@pytest.mark.parametrize('data', test_data_1)
def test_no_update(data):
    # use heapq
    data_1 = deepcopy(data)
    heapq.heapify(data_1)
    # use Heap
    data_2 = Heap()
    for weight, item in data:
        data_2.push(item, weight)
    # compare equal
    while not (len(data_1) == data_2.size == 0):
        assert heapq.heappop(data_1)[1] == data_2.pop()
        
        
test_data_2 = [
    [(15, 87), (10, 92), (13, 37), (1, 58), (18, 20), (9, 39), (19, 55), (0, 83), (4, 7), (7, 73), (5, 60), (3, 86), (17, 91), (6, 41), (14, 24), (16, 99), (2, 64), (12, 20), (11, 80), (8, 30)],
]
test_data_3 = [
    [(10.5, 20), (18.5, 86), (5.5, 99)]
]
test_data_4 = [
    [(15, 87), (10, 92), (13, 37), (1, 58), (10.5, 20), (9, 39), (19, 55), (0, 83), (4, 7), (7, 73), (5, 60), (18.5, 86), (17, 91), (6, 41), (14, 24), (5.5, 99), (2, 64), (12, 20), (11, 80), (8, 30)],
]

@pytest.mark.parametrize('data_old, update, data_new', zip(test_data_2, test_data_3, test_data_4))
def test_update(data_old, update, data_new):
    # use heapq
    data_1 = deepcopy(data_new)
    heapq.heapify(data_1)
    # use Heap
    data_2 = Heap()
    for weight, item in data_old:
        data_2.push(item, weight)
    for weight, item in update:
        data_2.update(item, weight)
    # compare equal
    while not (len(data_1) == data_2.size == 0):
        assert heapq.heappop(data_1)[1] == data_2.pop()
