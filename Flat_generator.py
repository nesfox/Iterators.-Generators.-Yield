import types


def flat_generator(list_of_lists):
    """Flatten a list of lists using a generator.

    Args:
        list_of_lists (List[List]): A list containing other lists.

    Yields:
        Any: Elements from the inner lists one-by-one.
    """
    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_2():
    """Test the flat_generator function.

    Creates a list of lists, passes it to the flat_generator,
    and asserts that the resulting items match the expected values.
    Also verifies that the returned object is indeed a generator type.
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()