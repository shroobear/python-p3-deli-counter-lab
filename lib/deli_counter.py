KATZ_DELI = []
OTHER_DELI = ["Logan", "Avi", "Spencer"]
ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_list = [f"{index + 1}. {name}" for index, name in enumerate(katz_deli)]    
        print("The line is currently: " + ' '.join(line_list))
        
def take_a_number(list, name):
    list.append(name)
    position = len(list)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
        customer = list.pop(0)
        print(f"Currently serving {customer}.")

now_serving(KATZ_DELI)