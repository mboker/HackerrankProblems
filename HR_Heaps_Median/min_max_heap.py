from math import floor


class MinMaxHeap:
    def __init__(self):
        self.min_high_heap = [None]
        self.max_low_heap = [None]
        self.median = None
        self.append_count = 0

    def append(self, value):
        if len(self.min_high_heap) is 1:
            self.min_high_heap.append(value)
            self.max_low_heap.append(value)
            self.median = value
        elif value >= self.min_high_heap[1]:
            if self.append_count % 2 == 1:
                self.min_high_heap[1] = value
                self.min_heapify_from_head()
            else:
                self.min_high_heap.append(value)
                self.max_low_heap.append(self.min_high_heap[1])
                self.min_heapify_from_leaf()
                self.max_heapify_from_leaf()
            self.median = (self.min_high_heap[1] + self.max_low_heap[1]) / 2
        elif value <= self.max_low_heap[1]:
            if self.append_count % 2 == 1:
                self.max_low_heap[1] = value
                self.max_heapify_from_head()
            else:
                self.max_low_heap.append(value)
                self.min_high_heap.append(self.max_low_heap[1])
                self.min_heapify_from_leaf()
                self.max_heapify_from_leaf()
            self.median = (self.min_high_heap[1] + self.max_low_heap[1]) / 2
        else:
            if self.append_count % 2 == 1:
                self.max_low_heap[1] = value
                self.max_heapify_from_head()
            else:
                self.max_low_heap.append(value)
                self.min_high_heap.append(value)
                self.min_heapify_from_leaf()
                self.max_heapify_from_leaf()
            self.median = (self.min_high_heap[1] + self.max_low_heap[1]) / 2

        self.append_count += 1
        print(float(self.median))

    def min_heapify_from_head(self):
        position = 1
        while 2 * position < len(self.min_high_heap):
            two_children = False
            current_greater_than_first_child = self.min_high_heap[position] > self.min_high_heap[2 * position]
            if 2 * position + 1 < len(self.min_high_heap):
                two_children = True
            if two_children:
                current_greater_than_second_child = self.min_high_heap[position] > self.min_high_heap[2 * position + 1]
                current_greater_than_both = current_greater_than_first_child and current_greater_than_second_child
                if current_greater_than_both:
                    if self.min_high_heap[2 * position] > self.min_high_heap[2 * position + 1]:
                        self.min_high_heap[position], self.min_high_heap[2 * position + 1] = \
                            self.min_high_heap[2 * position + 1], self.min_high_heap[position]
                        position = 2 * position + 1
                    else:
                        self.min_high_heap[position], self.min_high_heap[2 * position] = self.min_high_heap[2 * position], \
                                                                                     self.min_high_heap[position]
                        position *= 2
                elif current_greater_than_first_child:
                    self.min_high_heap[position], self.min_high_heap[2 * position] = \
                        self.min_high_heap[2 * position], self.min_high_heap[position]
                    position *= 2
                elif current_greater_than_second_child:
                    self.min_high_heap[position], self.min_high_heap[2 * position + 1] = \
                        self.min_high_heap[2 * position + 1], self.min_high_heap[position]
                    position = 2 * position + 1
                else:
                    position = len(self.min_high_heap)
            elif current_greater_than_first_child:
                self.min_high_heap[position], self.min_high_heap[2 * position] = \
                    self.min_high_heap[2 * position], self.min_high_heap[position]
                position *= 2
            else:
                position = len(self.min_high_heap)

    def min_heapify_from_leaf(self):
        position = len(self.min_high_heap) - 1
        while position > 1:
            parent_position = floor(position / 2)
            if self.min_high_heap[position] < self.min_high_heap[parent_position]:
                self.min_high_heap[position], self.min_high_heap[parent_position] = \
                    self.min_high_heap[parent_position], self.min_high_heap[position]
                position = parent_position
            else:
                position = 1

    def max_heapify_from_head(self):
        position = 1
        while 2 * position < len(self.max_low_heap):
            two_children = False
            current_less_than_first_child = self.max_low_heap[position] < self.max_low_heap[2 * position]
            if 2 * position + 1 < len(self.max_low_heap):
                two_children = True
            if two_children:
                current_less_than_second_child = self.max_low_heap[position] < self.max_low_heap[2 * position + 1]
                current_less_than_both_children = current_less_than_first_child and current_less_than_second_child
                if current_less_than_both_children:
                    if self.max_low_heap[2 * position] < self.max_low_heap[2 * position + 1]:
                        self.max_low_heap[position], self.max_low_heap[2 * position + 1] = self.max_low_heap[
                                                                                           2 * position + 1], \
                                                                                       self.max_low_heap[position]
                        position = 2 * position + 1
                    else:
                        self.max_low_heap[position], self.max_low_heap[2 * position] = self.max_low_heap[2 * position], \
                                                                                   self.max_low_heap[position]
                        position *= 2
                elif current_less_than_first_child:
                    self.max_low_heap[position], self.max_low_heap[2 * position] = self.max_low_heap[2 * position], \
                                                                               self.max_low_heap[position]
                    position *= 2
                elif current_less_than_second_child:
                    self.max_low_heap[position], self.max_low_heap[2 * position + 1] = self.max_low_heap[2 * position + 1], \
                                                                                   self.max_low_heap[position]
                    position = 2 * position + 1
                else:
                    position = len(self.max_low_heap)
            elif current_less_than_first_child:
                self.max_low_heap[position], self.max_low_heap[2 * position] = self.max_low_heap[2 * position], \
                                                                               self.max_low_heap[position]
                position *= 2
            else:
                position = len(self.max_low_heap)

    def max_heapify_from_leaf(self):
        position = len(self.max_low_heap) - 1
        while position > 1:
            parent_position = floor(position / 2)
            if self.max_low_heap[position] > self.max_low_heap[parent_position]:
                self.max_low_heap[position], self.max_low_heap[parent_position] = \
                    self.max_low_heap[parent_position], self.max_low_heap[position]
                position = parent_position
            else:
                position = 1
