__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    output = True
    if number > 1:
      for i in range(2,number-1):
        if number%i == 0:
          output = False
          break
    else:
      output = False
    return output
