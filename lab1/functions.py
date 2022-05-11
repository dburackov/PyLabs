import statistics
import constants


def check_input_text(text: str):
    result: bool = True
    if len(get_words(text)) == 0:
        result = False
    return result


def is_word(word: str):
    result: bool = False
    if word.strip(constants.WORD_SEPARATOR).isalpha():
        result = True
    return result


def get_words(text: str):
    result: list[str] = []
    words: list[str] = text.split()
    for item in words:
        if is_word(item):
            result.append(item.strip(constants.WORD_SEPARATOR))
    return result


def get_words_number(words):
    result: dict[str, int] = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result


def get_sentences_word_number(text: str):
    result: list[int] = [0]
    words: list[str] = text.split()

    for word in words:
        if is_word(word):
            result[-1] += 1
            if constants.END_SYMBOL.find(word[-1]) != -1:
                result.append(0)

    if result[-1] == 0:
        result.pop()

    return result


def get_n_grams(word: str, n: int):
    result: list[str] = []
    for i in range(0, len(word) - n + 1):
        result.append(word[i: i + n])
    return result


def n_grams_compare_func(item):
    return item[1]


def get_top_n_grams(words, k: int, n: int):
    result: list[(str, int)] = []
    n_grams_dict: dict[str, int] = {}

    for word in words:
        n_grams: list[str] = get_n_grams(word, n)
        for n_gram in n_grams:
            n_grams_dict[n_gram] = n_grams_dict.get(n_gram, 0) + 1

    while len(n_grams_dict) > 0:
        result.append(n_grams_dict.popitem())

    result.sort(reverse=True, key=n_grams_compare_func)

    while len(result) > k:
        result.pop()

    return result


def print_results(words_number, average_words_number: float, median_words_number: float,
                  top_n_grams):
    print("\nWords numbers:\n")
    for word, number in words_number.items():
        print(f"\"{word}\" in text {number} times")

    print(f"\nAverage words number in sentences = {average_words_number}")
    print(f"\nMedian words number in sentences = {median_words_number}")

    print("\nTop K most recurring N gramms:\n")
    for item in top_n_grams:
        print(f"\"{item[0]}\" in text {item[1]}")


def solve(text: str, k: int, n: int):
    text = text.lower()

    words_number = get_words_number(get_words(text))

    average_words_number: float = statistics.fmean(get_sentences_word_number(text))
    median_words_number: float = statistics.median(get_sentences_word_number(text))

    top_n_grams = get_top_n_grams(get_words(text), k, n)

    print_results(words_number, average_words_number, median_words_number, top_n_grams)
