from random import choice, randint
import time

def get_localtime() -> str: # return localtime
    tt = time.localtime()
    return f'the time is {tt.tm_year}/{tt.tm_mon}/{tt.tm_mday}, {tt.tm_hour:02d}:{tt.tm_min:02d}'

def raf_response() -> str:
    return choice(['raf is gay',
                  'raf is so gay',
                  'raf is such a gay',
                  'raf is gay as f*ck'])

# NO USED
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == 'what time is it':
        return get_localtime()
    elif 'hello' in lowered:
        return 'hello there'
    elif 'pien' in lowered:
        return 'pien party'
    elif 'nmsl' in lowered:
        return 'stfu'
    elif lowered == 'yo':
        return 'check it out'
    else:
        return choice(['i don\'t understand',
                       'huh',
                       'really?',
                       'lmao'])
