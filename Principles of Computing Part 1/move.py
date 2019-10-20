
height = 5
width  = 4

def generate(direction):
    idx = 0 # outer loop counter
    jdx = 0 # inner loop counter
    
    print('-'*20,direction,'+'*20)

    if direction in ('up', 'down'):
        idx, jdx = width, height
    else:
        idx, jdx = height, width


    # generat the index
    data = [ [12, 22, 789, 90, 4],
    		 [10, 45, 55, 65, 6],
    		 [8, 9, 10, 22, 7],
    		 [16, 13, 312, 356, 8],
    		]
    for out in range(idx):
    	temp = []

    	for inn in range(jdx):
    		temp.append(data[out][inn])

    	# if direction in ('down', 'left'):
    	# 	temp = temp[::-1]
    	print(temp)






if __name__ == '__main__':
    generate('up')
    generate('down')
    generate('left')
    generate('right')

