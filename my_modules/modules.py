#modules.py

class MySortingClass:
    def __init__(self):
        pass

    def _find_smallest_id(self,l:list[int]):
        smallest = l[0]
        smallest_id = 0
        for i in range(len(l)):
            if l[i] < smallest:
                smallest_id, smallest = i, l[i]
        return smallest_id
    
    def _find_largest_id(self,l:list[int]):
        largest = l[0]
        largest_id = 0
        for i in range(len(l)):
            if l[i] > largest:
                largest_id, largest = i, l[i]
        return largest_id    
    
    def selection_sort(self,l:list[int],reverse = False):
        '''
        Return a new list containing all items from the iterable in ascending order.

        reverse - use if you want a list in descending order
        '''
        new_array = []
        array_copy = l.copy()
        for _ in range(len(l)):
            if reverse:
                largest_id = self._find_largest_id(array_copy)
                new_array.append(array_copy.pop(largest_id))
            else:
                smallest_id = self._find_smallest_id(array_copy)
                new_array.append(array_copy.pop(smallest_id))

        return new_array