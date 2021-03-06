from advent_of_code import AdventOfCode
import math


class Day16(AdventOfCode):
    def __init__(self, test = False):
        self.test = test
        super().__init__(16, test)
        self.data = self.load_data()

        self.functions = {
            0: sum,
            1: math.prod,
            2: min,
            3: max,
            5: lambda i: 1 if i[0] > i[1] else 0,
            6: lambda i: 1 if i[0] < i[1] else 0,
            7: lambda i: 1 if i[0] == i[1] else 0
        }

        self.part1and2()

    def load_data(self):
        tab = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
        }

        data = super().load_list_from_file(str, 'transmission')[0]
        return ''.join(tab.get(d) for d in data)

    def get_value_from_literal(self, shift):
        result = ""
        for i in range(6+shift, len(self.data), 5):
            result += self.data[i+1:i+5]
            if self.data[i] == '0':
                break
        return int(result, 2)

    def calculate(self, shift=0):
        version = int(self.data[shift:3+shift], 2)
        sum_of_version = version
        type_id = int(self.data[3+shift:6+shift], 2)
        length_type_id = int(self.data[6+shift])
        result = []

        def get_end():
            for i in range(6+shift, len(self.data), 5):
                if self.data[i] == '0':
                    return i+5

        if type_id == 4:
            return get_end(), sum_of_version, self.get_value_from_literal(shift)

        if length_type_id == 0:
            length = int(self.data[7+shift:22+shift], 2)
            shift += 22

            while length > 0:
                end, version, value = self.calculate(shift)
                sum_of_version += version
                length -= end
                length += shift
                shift = end
                result.append(value)
        else:
            count = int(self.data[7+shift:18+shift], 2)
            shift += 18

            for _ in range(count):
                end, version, value = self.calculate(shift)
                sum_of_version += version
                shift = end
                result.append(value)

        function = self.functions.get(type_id)
        return end, sum_of_version, function(result)

    def part1and2(self):
        answers = self.calculate()[1:]
        super().print_answer(1, answers[0])
        super().print_answer(2, answers[1])