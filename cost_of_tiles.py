def cost():
    width = int(input("width: "))
    height = int(input("length: "))
    enter_cost = int(input("Enter the cost: "))
    area_of_floor = width*height
    total_cost = area_of_floor*enter_cost
    print("total cost: ",total_cost)
    
cost()
