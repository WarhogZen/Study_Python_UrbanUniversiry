calls = 0
def count_calls() :
    global calls
    calls += calls
def string_info(string) :
    tup_info = (len(string),string.upper(), string.lower())
    return tup_info
def is_contains(string, list_of_strings) :
    cont = string.lower()
    for i in range(len(list_of_strings)) :
        container = list_of_strings[i].lower()
        if cont == container :
            flag = True
            break
        else :
            flag = False
    return flag
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)