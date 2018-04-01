class WordTries:
    class TryNode:
        __slots__ = ['valid_chars_after', 'word_count']

        def __init__(self): #, is_complete=False):
            self.valid_chars_after = dict()
            #self.is_complete_word = is_complete
            self.word_count = 0

        def get_child(self, value):
            if value in self.valid_chars_after.keys():
                return self.valid_chars_after[value]
            else:
                return None

    def __init__(self):
        self.start_node = self.TryNode()

    def add(self, word):
        current_node = self.start_node
        for char in word:
            new_node = current_node.get_child(char)
            if new_node is None:
                new_node = self.TryNode()
                current_node.valid_chars_after[char] = new_node
            current_node = new_node
            current_node.word_count += 1
        #current_node.is_complete_word = True

    def find(self, prefix):
        current_node = self.start_node
        for i in range(len(prefix)):
            if prefix[i] in current_node.valid_chars_after.keys():
                current_node = current_node.valid_chars_after[prefix[i]]
            else:
                return 0

        return current_node.word_count

