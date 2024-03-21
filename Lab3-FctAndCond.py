
# Conversion function placeholders
# Task 1: Create two functions to convert between pyeong and square meters.
def convert_mcp(m2):
    pyeong = 3.3058 * m2
    return pyeong
def convert_pcm(pyeong):
    m2 = 0.3025 * pyeong
    return m2

# Value calculation function placeholder
# Task 2: Create a function to calculate the value of an apartment based on size in m2, location, access quality, and view.
#    What parameters will this function need?
#    How will each parameter affect the apartment's value?
#    Remember to consider different factors like location premium, access quality, and the view premium.
def Access_premium(x):
    if (x=="Poor") :
      return 0.75
    elif (x=="Fair") :
         return 1
    elif(x=="Good"):
         return 1.25
    elif (x=="Very_Good"):
         return 1.5

def Location_premium(x):
    if (x=="Gangnam"):
        return 1.5
    else :
        return 1
    
def View_premium(x):
    if (x=="Han_river") :
        return 1.5
    else :
        return 1
    
def calculate_value(pyeong,location,access,view) :
    value = 13000*convert_pcm(pyeong)*Access_premium(access)*Location_premium(location)*View_premium(view)

    return value

# your main function here
def main():
    
    # Property 1 specifications
    surface_pyeong_1 = 25
    location_1 = "Gangnam"
    access_1 = "Good" # Poor / Fair / Good / Very Good
    view_1 = True # view on the Han River?
    
    # Property 2 specifications
    surface_pyeong_2 = 45
    location_2 = "Other"
    access_2 = "Poor" # Poor / Fair / Good / Very Good
    view_2 = False # view on the Han River?


    option1 = calculate_value(surface_pyeong_1,location_1,access_1,view_1)
    option2 = calculate_value(surface_pyeong_2,location_2,access_2,view_2)

    if (option1 > option2) :
        print("Apartment2")
    else :
        print("Apartment1")
    
    # Task 1: Convert pyeong to m2

    # Task 2: Calculate properties' values
    
    # Task 3: Find the cheapest one and print

# Call the main function here!
if __name__ == "__main__": # <-- # checks if being run directly (not imported)
    main()