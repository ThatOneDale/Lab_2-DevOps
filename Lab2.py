def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)

def display_main_menu():
    print("Enter Some Numbers Seperated by Commas: ")


def calc_average_temperature(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]

    average = sum/len(x)
    print("The average of the numbers is " + str(average))

def calc_min_max_temperature(x):
    min = x[0]
    max = x[0]

    for i in range(len(x)):
        if x[i] > max:
            max = x[i]
        if x[i] < min:
            min = x[i]

    print("The biggest number is " + str(max))
    print("The smallest number is " + str(min))
def get_user_input():
    x = input()
    x = x.split(",")
    for i in range(len(x)):
        x[i] = float(x[i])
    return x


if __name__ == "__main__":
    main()