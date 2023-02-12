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
      'd' : int_to_2dig_str(seconds//86400)
    }

    time_dict['h'] = int_to_2dig_str((seconds - int(time_dict['d'])*86400) // 3600)
    time_dict['m'] = int_to_2dig_str((seconds - int(time_dict['d'])*86400 - int(time_dict['h'])*3600) // 60)
    time_dict['s'] = int_to_2dig_str(seconds % 60)
  
    write_value = False
  
    for key, value in time_dict.items():
      
      if (value != '00' and key != 's') or write_value == True or key == 's':
        write_value = True
        output = output + value + key
    return output

def int_to_2dig_str (input: int) -> str:
    '''
    add 0 to the one digit int input and returns string, for input bigger than 99 returns None
    '''
    if input < 10:
      output = ''.join(('0',str(input)))
    elif input < 100:
      output = ''.join(str(input)) 
    else:
      return None
  
    return output