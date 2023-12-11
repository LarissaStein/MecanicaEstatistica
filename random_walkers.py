import numpy as np
import random as rand

#Simulation
def simulation_steps(inicial_x,final_x,step_size):
    current_n=inicial_x/step_size
    n_steps = 0 #number of steps
    while current_n < final_x/step_size:
        if current_n == 0:
            step=1
        else:
            step=rand.choice([-1,1])
        current_n+=step
        n_steps+=1
    return n_steps

#Analytical
def MFPT(inicial_x,final_x,d):
    def sum_(n):
        lambda_n = ((2*n+1)*np.pi)/(2*final_x)
        s=(np.cos(lambda_n*inicial_x)/(lambda_n**3))*((-1)**n)
        return s
    s1=0
    for i in range(20):
        s1+=sum_(i)
    steps=(2*s1)/(final_x*d)
    return steps

N=1000 #walkers
x0, xf = 2, 5
div=[20,50,100] #dividers
tau=1

for divider in div:
    size=xf/divider #step size
    D=(size**2)/(2*tau)
    sum_steps=0
    for walker in range(N):
        sum_steps+=simulation_steps(x0,xf,size)
    simulation=sum_steps/N
    analytical= MFPT(x0,xf,D)
    print(f'Number of dividers: {divider}')
    print(f'Simulation result = {round(simulation, 2)}')
    print(f'Analytical result = {round(analytical, 2)}')
    print( )
