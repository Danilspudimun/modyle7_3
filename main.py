class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for punctuation in punctuations:
                    text = text.replace(punctuation, '')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
