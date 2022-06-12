'''Set of progress bars for projects.'''
import sys

class SetBar:
    '''Main bar method.'''
    def __init__(self, text: str, total: int, filler='#'):
        self.text = text
        self.total = total
        self.current_progress = 0
        self.green = '\033[0;32m'
        self.endc = '\033[0m'
        self.filler = filler

    def print_bar(self):
        '''Print & update bar'''
        percent = 100 * (self.current_progress / float(self.total))
        progress_bar = self.filler * int(percent) \
             + '-' * (100 - int(percent))

        sys.stdout.write("\033[K")
        if self.current_progress == self.total:
            return print(f'\r{self.green}Done |{progress_bar}|[{self.current_progress}/{self.total}]{self.endc}', end='\n')
        return print(f'\r{self.text} |{progress_bar}|[{self.current_progress}/{self.total}]', end ='\r')

    def update_bar(self):
        '''Progress updater.'''
        self.current_progress += 1
        return SetBar.print_bar(self)

if __name__ == '__main__':
    num_lst = range(0, 100099)
    Bar = SetBar(text='Progress', total=len(num_lst), filler='#')

    for i in num_lst:
        Bar.update_bar()
