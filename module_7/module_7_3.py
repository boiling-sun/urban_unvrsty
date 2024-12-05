"""
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов 
и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. 
Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.

count(self, word) - метод, где word - искомое слово. 
Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.

В методах find и count пользуйтесь ранее написанным методом get_all_words для 
получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) 
можно воспользоваться методом словаря - item().
"""
import os

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    @property
    def file_names(self):
        return self._file_names
    
    @file_names.setter
    def file_names(self, names):
        fullnames = []
        for name in names:
            full_name = os.path.join('module_7', name)
            print(full_name)
            if not os.path.exists(full_name):
                print(f'Файл {name} не найден')
                continue
            fullnames.append(full_name)
        self._file_names = fullnames

    def get_all_words(self):
        """
        get_all_words - подготовительный метод, который возвращает словарь следующего вида:
        {
            'file1.txt': ['word1', 'word2'], 
            'file2.txt': ['word3', 'word4'], 
            'file3.txt': ['word5', 'word6', 'word7']
        }
        """
        words_dict = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                all_words = [word.casefold().strip(',.=!?;: - "|\\/') for word in f.read().split()]
                words_dict[file_name] = all_words
        return words_dict

    def get_word(function):
        def wrapper(self, word):
            result = {}
            word = word.casefold()
            for file, words in self.get_all_words().items():
                if word in words:
                    result[file] = function(self, words, word)
            if not result:
                print(f'Слово {word} не найдено')
            return result
        return wrapper

    @get_word
    def find(self, words, word):
        return list.index(words, word) + 1

    @get_word
    def count(self, words, word):
        return list.count(words, word)
    
    # def find(self, word):
    #     """
    #     word - искомое слово. 
    #     Возвращает словарь, где ключ - название файла, значение - позиция 
    #     первого такого слова в списке слов этого файла.
    #     """
    #     result = {}
    #     word = word.casefold()
    #     for file, words in self.get_all_words().items():
    #        if word in words:
    #            result[file] = words.index(word)
    #     if not result:
    #         print(f'Слово {word} не найдено')
    #     return result
        
    # def count(self, word):
    #     """
    #     word - искомое слово. 
    #     Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
    #     """
    #     result = {}
    #     word = word.casefold()
    #     for file, words in self.get_all_words().items():
    #        if word in words:
    #            result[file] = words.count(word)
    #     if not result:
    #         print(f'Слово {word} не найдено')
    #     return result


def main():
    finder2 = WordsFinder('test_file.txt', 'products.txt', 'test.txt')
    print(finder2.file_names)
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего

if __name__ == '__main__':
    main()