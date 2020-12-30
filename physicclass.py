train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#input f_temp
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp 
f100_in_celcius = f_to_c(100)

#input c_temp
def c_to_f(c_temp):
  f_temp = (c_temp) * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)

#input mass and acceleration
def get_force(mass, acceleration):
  return mass*acceleration
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#input mass and c
def get_energy(mass, c=3*10**8):
  return mass*c**2
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#input mass, acceleration, force and distance
def get_work(mass, acceleration, distance):
  #Opsi 1 -> force = get_force(mass, acceleration)
  #Lanjutan Opsi 1 -> return force*distance
  force = get_force(mass, acceleration)
  return force*distance
  #Opsi 2 (instant)-> return get_force(mass, acceleration)*distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

