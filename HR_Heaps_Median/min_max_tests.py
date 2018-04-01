from min_max_heap import MinMaxHeap


def test_min_heapify_head():
    heap_obj = MinMaxHeap()
    heap_obj.min_high_heap.append(4)
    heap_obj.min_high_heap.append(1)
    heap_obj.min_high_heap.append(3)
    heap_obj.min_high_heap.append(5)
    heap_obj.min_high_heap.append(6)
    heap_obj.min_high_heap.append(4)

    heap_obj.min_heapify_from_head()
    assert heap_obj.min_high_heap[2] is 4

def test_min_heapify_leaf():
    heap_obj = MinMaxHeap()
    heap_obj.min_high_heap.append(1)
    heap_obj.min_high_heap.append(3)
    heap_obj.min_high_heap.append(5)
    heap_obj.min_high_heap.append(6)
    heap_obj.min_high_heap.append(4)
    heap_obj.min_high_heap.append(2)

    heap_obj.min_heapify_from_head()
    assert heap_obj.min_high_heap[3] is 2


if __name__ is '__main__':
    test_min_heapify_head()
    test_min_heapify_leaf()