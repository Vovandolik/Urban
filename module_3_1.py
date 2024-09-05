calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in range(0, len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
        if list_to_search[i] == string:
            return True
        elif i == len(list_to_search) - 1:
            return False
        else: continue

print(string_info('Unbelievable'))
print(string_info('Pepperoni'))
print(is_contains('Urban', ['urBAN', 'BaNaN', 'ban']))
print(is_contains('Tasty', ['Toast', 'tAnk', 'NaStY']))
print(calls)