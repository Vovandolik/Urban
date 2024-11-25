class WordsFinder:

    def __init__(self, *files):
        self.file_names = []
        self.file_names.extend(files)

    def get_all_words(self):
        all_words = {}
        for files in self.file_names:
            with open(files, encoding='utf-8') as file:
                words = []
                for line in file:
                    _line = line.lower()
                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        _line = _line.replace(symbol, '')
                    words = words + _line.split()
                all_words.update({files: words})
        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_dict.update({name: words.index(word.lower()) + 1})
        return find_dict

    def count(self, word):
        cont_dict = {}
        for name, words in self.get_all_words().items():
            word_count = 0
            for i in range(len(words)):
                if word.lower() == words[i]:
                    word_count += 1
            cont_dict.update({name: word_count})
        return cont_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего