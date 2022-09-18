def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'): # value is given object and fmt is its format
    return value.strftime(fmt)
