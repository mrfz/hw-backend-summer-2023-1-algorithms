__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even_sum = 0.0
    odd_sum = 0.0

    for i in range(len(arr)):
      if arr[i]%2 == 0:
        even_sum += arr[i]
      else:
        odd_sum += arr[i]
    if odd_sum != 0.0:
      output = even_sum/odd_sum
    else:
      output = 0
     
    return output