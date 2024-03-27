outie = "Excellent, press 'Exit' to return to home screen"

maintenance = "Call maintenance and return to home screen."

def table_check():
    """This prompts operator to check if the table is level"""
    check = input("Is the table level (Yes or No): ")
    check = check.title()
    if check == "Yes":
        print(maintenance)
    else:
        print("Level the table.")
        print("To level the table, first locate adjustment points P (tilt) and N (height).")
        e_check = input("Did this resolve the issue (Yes or No): ")
        e_check = e_check.title()
        if e_check == "Yes":
            print(outie)
        else:
            print(maintenance)

settings_check = input("Does height and angle of dual supply arm match our centerlines (Yes or No): ")
settings_check = settings_check.title()
if settings_check == "Yes":
    table_check()
else:
    print("Adjust dual supply arm height (U) to match centerlines for current bottle size.")
    e_check_0 = input("Did this resolve the issue (Yes or No): ")
    e_check_0 = e_check_0.title()
    if e_check_0 == "Yes":
        print(outie)
    else:
        print("Adjust the dual supply arm (Y), up or down to match centerlines for current bottle size.")
        e_check_1 = input("Did this resolve the issue (Yes or No): ")
        e_check_1 = e_check_1.title()
        if e_check_1 == 'Yes':
            print(outie)
        else:
            table_check()