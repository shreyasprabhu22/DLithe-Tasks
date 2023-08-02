#TWO_WHEELER AND FOR_WHEELER TCS PROBLEM

no_of_vech=int(input()) 
no_of_wheels=int(input()) 
    
four_wheel = (no_of_wheels-2*no_of_vech)/2;
    
two_wheel =no_of_vech-four_wheel
print(two_wheel,four_wheel)