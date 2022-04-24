class ReturnIndices:
    @staticmethod
    def hash_return(nums, given_integer) -> list:
        dct = {}
        for index, value in enumerate(nums):
            if given_integer - value in dct:
                return [dct[given_integer - value], index]
            dct[value] = index


if __name__ == "__main__":
    return_indices = ReturnIndices()
    input_nums = [5, 7, 9, 2, 3]
    input_integer = 9
    ans_index = return_indices.hash_return(input_nums, input_integer)
    print(f'the add up number index is: {ans_index}')
