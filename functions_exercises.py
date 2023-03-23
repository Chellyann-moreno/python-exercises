def is_two(a):
    if a== 2 or a=='2':
        return True
    else:
      return False
    
def is_vowel(char):
    return char.lower() in 'aeiou'


def is_consonant(char):
    return char.lower() not in 'aeiou'


def is_consonant(char):
  return char.lower() not in 'aeiou'


def is_word(string):
    if is_consonant(string[0]):
        string = string.capitalize()
    return string
def is_word(string):
    if is_consonant(string[0]):
        string=string.capitalize()
        return string
  
def calculate_tip(bill,tip):
    return bill*tip+bill

def apply_discount(discount,price):
    return price -(discount * price)

def handle_commas(input_string): 
    return int(input_string.replace(',',''))

def get_letter_grade(grade):
    if grade >=90:
        letter_grade='A'
    elif grade >=80:
        letter_grade= 'B'
    elif grade >=70:
        letter_grade= 'C'
    elif grade >=60:
        letter_grade= "D"
    else:
        letter_grade ='F'
    return letter_grade

def remove_vowels(string):
    new_string=''

    for char in string:
        if not is_vowel(char):
            new_string +=char
    return new_string

def correct_name(string):
    string = string.strip().lower().replace(' ','_')
    
    new_string = ''

    for char in string:
        if char.isalpha() or char.isdigit() or char == '_':

            new_string += char

    new_string = new_string.strip('_')
    
    return new_string

def cumulative_sum(ls):
    total = 0 
    some_sums = []

    for numb in ls:
    #     print(numb)
        total += numb
#         print(total)
        some_sums.append(total)

    return some_sums
    