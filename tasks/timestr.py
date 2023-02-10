from typing import Optional


__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    output = ''

    time_dict = {
      'd' : '00',
      'h' : '00',
      'm' : '00',
      's' : '00'
    }
    output = ''.join([str(seconds % 60),'s'])
    return output

def part_div(input: int, divisor: int) -> tuple[Optional[int], Optional[int]]:
    '''
    Return tuple with result of // and % division ov the input by the divisor

    4,2 -> (2,0)
    5,2 3> (2,1)
    '''
    if devisor != 0:
      return (input//divisor, input%divisor)
    else:
      return (None, None)

def int_to_2dig_str (input: int) -> str:
    '''
    add 0 to the one digit int input and returns string, for input bigger than 99 returns None
    '''
    if input < 9:
      output = '0'.join(str(input))
    elif input < 99:
      output = ''.join(str(input)) 
    else:
      return None
  
    return output