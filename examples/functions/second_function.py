#!/usr/bin/env python3
def wrap_with_border(some_text, char='#'):
    result = [len(some_text) * char]
    result.append(some_text)
    result.append(result[0])
    return "\n".join(result)


data = wrap_with_border("Hello")
print(data)
print(wrap_with_border("Goodbye"))
print(wrap_with_border('hoooooooo', '*'))

