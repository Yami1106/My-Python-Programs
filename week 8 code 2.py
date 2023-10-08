import threading

class CharacterDictBuilder(threading.Thread):
    def __init__(self, input_str):
        threading.Thread.__init__(self)
        self.input_str = input_str
        self.char_dict = {}

    def run(self):
        for char in self.input_str:
            if char in self.char_dict:
                self.char_dict[char] += 1
            else:
                self.char_dict[char] = 1

    def get_char_dict(self):
        return self.char_dict

# Instantiate the subclass and start the thread
input_str = "Hello, World!"
char_dict_builder = CharacterDictBuilder(input_str)
char_dict_builder.start()

# Wait for the thread to finish and get the resulting character dictionary
char_dict_builder.join()
char_dict = char_dict_builder.get_char_dict()
print(char_dict)
