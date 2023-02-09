from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    text = text.strip().replace(',','')
    text_list = text.split()
    if len(text) == 0:
      output = (None,None)
    else:
      word_len = [len(word) for word in text_list]
      output = (text_list[word_len.index(min(word_len))],text_list[word_len.index(max(word_len))])
    return output
