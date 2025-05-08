print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
     print("Enter some numbers separated by commas (e.g. 5, 67,32)")
def get_user_input():
     x = input ()
     y = x.split(", ")
     float_list = [float(y.strip()) for x in y]
     return float_list

def find_min_max():
     print("find_min_max")
def sort_temperature():
     print("sort_temperature") 
def calc_median_temperature():
     print("calc_median_temperature")   
     
def calc_average(listfloat):
    print("calc_average temperature")
    m = (len(listfloat))
    n = (sum(listfloat))
    average = n / m
    print("Average temperature: " + str(average))

def calc_min_max_temperature(listfloat):
    minimum_value = min(listfloat)
    print("Minimum temperature: " + str(minimum_value))
    maximum_value = max(listfloat)
    print("Maximum temperature: " + str(maximum_value))