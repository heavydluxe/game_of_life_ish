import os, sys, time, numpy

# set the base array shape (h,w)
dimension = (10,5)
generation = 0

def generate_base(dimension):
    # create a array with 0/1 random in each cell
    arr = numpy.random.randint(2,size=dimension)
    
    # display it
    os.system('clear')
    print(arr)
    print("Generation # ",generation)
    time.sleep(2)
    os.system('clear')
    return arr

def alivedead(input):
    # create a new array to hold transformed values
    global dimension
    global generation
    new_arr = numpy.empty(dimension,dtype=int)
    generation = generation + 1
    
    # process input array
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
          cell = int(input[i,j])
          if input[i,j] == 0:
             new_arr[i,j] = 0
          elif input[i,j] <= 3:
             new_arr[i,j] = cell + 1
          elif input[i,j] == 4:
              new_arr[i,j] = 0
    print(new_arr)
    print("Generation #",generation)
    time.sleep(2)
    return new_arr

def make_life(input_arr):
    generation = int(1)
    while True:
        os.system('clear')
        print(input_arr)
        
        # write new array based on rules
        # 
        # print new_arr, gen num, and update gen num
        print("Generation #",generation)
        time.sleep(2)
        generation=generation+1
        
def main():
    arr=generate_base(dimension)
    alivedead(arr)
    print("Again \n",new_arr)

main()

