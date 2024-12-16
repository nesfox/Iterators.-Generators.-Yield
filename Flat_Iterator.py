class FlatIterator:
    """A custom iterator that flattens a nested list into a single sequence."""

    def __init__(self, list_of_lists):
        """
        Initialize the FlatIterator with a nested list.

        :param list_of_lists: A list of lists to be flattened.
        """
        self.flattened_list = []  # Initialize an empty list to store flattened elements.

        # Flatten the nested list by extending each sublist to the flattened list.
        for sublist in list_of_lists:
            self.flattened_list.extend(sublist)

        self.index = 0  # Initialize the index to start from the first element.

    def __iter__(self):
        """
        Return the iterator object itself.

        :return: The iterator instance.
        """
        return self

    def __next__(self):
        """
        Return the next element in the flattened list or raise StopIteration if there are no more elements.

        :return: The next element in the flattened list.
        :raises: StopIteration if all elements have been iterated over.
        """
        if self.index >= len(self.flattened_list):
            raise StopIteration

        item = self.flattened_list[self.index]  # Get the current element at the given index.
        self.index += 1  # Increment the index to point to the next element.
        return item


def test_1():
    """
    Test the functionality of the FlatIterator class.

    This function creates a nested list, initializes a FlatIterator,
    and checks if the iterator returns the correct flattened sequence.
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # Iterate through the flattened list and compare it with the expected result.
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    # Check if converting the iterator to a list produces the same result as the expected flattened list.
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()