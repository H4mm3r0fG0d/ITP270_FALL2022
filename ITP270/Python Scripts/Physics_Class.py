# Writing a Fahrenheit(F) to Celsius(C) converter
def f_to_c():
    f_temp = int(input("Please enter a temperature in degrees Fahrenheit: "))
    c_temp = (f_temp - 32) * (5/9)
    return c_temp

# Testing the function and printing the value to screen
f100_in_celsius = f_to_c()
f100_in_celsius = round(f100_in_celsius, 2)
print(f100_in_celsius)

# Writing a Celsius(C) to Fahrenheit(F) converter
def c_to_f():
    c_temp = int(input("Please enter a temperature in degrees Celsius: "))
    f_temp = (c_temp *(9/5) + 32)
    return f_temp

#Testing the function and printing the value to screen
c0_in_fahrenheit = c_to_f()
c0_in_fahrenheit = round(c0_in_fahrenheit, 2)
print(c0_in_fahrenheit)

# Defining the Force function
def get_force():
    m = input("Please enter mass amount(in pounds): ")
    a = input("Please enter speed of acceleration(in mph): ")
    m = float(m)
    a = float(a)

    f = m * a
    f = round(f, 2)
    return f

# Test the function using train_force and print it as a string
train_force = get_force()
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Defining the get_energy function with the bomb_mass variable
def get_energy():
    bomb_mass = input("Please enter mass of the bomb: ")
    bomb_mass = float(bomb_mass)
    c = float(3*(10**8))

    e = bomb_mass * (c**2)
    return e

# Testing the function with the variable bomb_energy defined as get_energy function
bomb_energy = get_energy()
bomb_energy = round(bomb_energy, 4)
print("A 1 kg bomb supplies " + str(bomb_energy) + " Joules.")

# Defining the get_work function
def get_work():
    force = get_force()
    distance = input("Please enter distance(in meters): ")
    distance = float(distance)

    work = force * distance
    work = round(work, 4)
    return work

# Testing the function using train_work variable defined as get_work function and printing it to screen
train_work = get_work()
distance = 2500
print("The GE train does " + str(train_work) + " Joules of work over " + str(distance) + " meters.")
