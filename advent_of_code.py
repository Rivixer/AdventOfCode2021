from typing import Type, Union


class AdventOfCode:
    def __init__(self, day: int, test: bool = False):
        self.day = day
        self.test = test
        
    def load_list_from_file(self, type: Union[Type[int], Type[str], Type[float], Type[bool]], filename: str = 'file', item: int = 0, splitter: str = ' ', oneline:bool = False) -> list:
        filename = 'test.txt' if self.test else f'{filename}.txt'
        
        with open(f'Day{("0" + str(self.day)) if self.day < 10 else self.day}/{filename}') as f:
            if oneline:
                result = list(map(type, f.readlines()[item].strip().split(splitter)))
            else:
                result = list(map(lambda i: type(i.split(splitter)[item].strip()), f.readlines()))
                
        return result

    def print_answer(self, part: int, answer, time = None):
        if self.test:
            print('TEST | ', end='')
        if isinstance(answer, list):
            if isinstance(answer[0], list):
                print(f'Day {self.day} / part {part}:' + (f' ({time}s)' if time else ''))
                for l in answer:
                    print(''.join(l))
                return
            else:
                answer = ', '.join(answer)
        print(f'Day {self.day} / part {part}: {answer}' + (f' ({time}s)' if time else ''))