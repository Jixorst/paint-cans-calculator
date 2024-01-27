
def paint_cans(width, length):
    width= float(width)
    length= float(length)
    surface_area = width*length
    number_of_cans = int(surface_area // 5)
    extra_paint = surface_area % 5

    if extra_paint != 0 :
     number_of_cans += 1
    print(f'the number of paint cans is: {number_of_cans}') 

paint_cans(input('the width: ') ,input('the length: '))


    