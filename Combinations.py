class MinimalChangeCombinations:
    def __init__(self, elements):
        self.elements = list(elements)

    def successor(self, subset):
        return self.unrank(self.rank(subset) + 1)

    def predecessor(self, subset):
        return self.unrank(self.rank(subset) - 1)

    def rank(self, subset):
        gray_code = [0] * len(self.elements)
        for i in range(0, len(self.elements)):
            if self.elements[i] in subset:
                gray_code[i] = 1

        binary = self.__gray_code_to_binary(gray_code)
        return int("".join(map(str, binary)), 2)

    def unrank(self, rank_value):
        binary = self.__int_to_binary(rank_value)
        gray_code = self.__binary_to_gray_code(binary)
        subset = set()
        for i in range(0, len(gray_code)):
            if gray_code[i] == 1:
                subset.add(self.elements[i])
        return subset

    def __int_to_binary(self, integer):
        binary = list(map(int, bin(integer)[2:]))
        return [0] * (len(self.elements) - len(binary)) + binary if len(binary) < len(self.elements) else binary

    @staticmethod
    def __binary_to_gray_code(binary):
        gray_code = [binary[0]]
        for i in range(1, len(binary)):
            gray_code.append(binary[i - 1] ^ binary[i])
        return gray_code

    @staticmethod
    def __gray_code_to_binary(gray_code):
        binary = [gray_code[0]]
        for i in range(1, len(gray_code)):
            binary.append((binary[i - 1] + gray_code[i]) % 2)
        return binary
