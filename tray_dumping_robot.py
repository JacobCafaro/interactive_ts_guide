outie = "Excellent, select 'Exit' to return to home screen."
maintenance = "Call maintenance and return to home screen."
light_color_orientation = input("Is the light stack SOLID AMBER (1), FLASHING AMBER (2), RED (3), SOLID GREEN (4), or FLASHING GREEN (5): ")
light_color_orientation = int(light_color_orientation)

if light_color_orientation == 1:
    pause = input("Does the HMI screen display 'Robot is Paused' (Yes or No): ")
    pause = pause.title()
    if pause == "Yes":
        print("Press 'play' to resume operation.")
    if pause == "No":
        wait_status = input("Is robot waiting in front of HMI without a tray in the grippers (Yes or No): ")
        wait_status = wait_status.title()
        if wait_status == "Yes":
            dolly_load = input("Is there at lease one dolly with gummy product loaded and locked into one of the docks (Yes or No): ")
            dolly_load = dolly_load.title()
            if dolly_load == "Yes":
                print(maintenance)
            else:
                print('Load dolly with full trays into at least one dock to resume operations.')
        if wait_status == "No":
            print(maintenance)

if light_color_orientation == 2:
    holding_tray = input("Is robot holding empty tray above Washer Infeed Conveyor (Yes or No): ")
    holding_tray = holding_tray.title()
    if holding_tray == "Yes":
        conveyor_op = input("Are Tray Washer chain and infeed conveyor powered on and running (Yes or No): ")
        conveyor_op = conveyor_op.title()
        if conveyor_op == "Yes":
            jam_check = input("Is there a tray jammed on either conveyor (Yes or No): ")
            jam_check = jam_check.title()
            if jam_check == "Yes":
                print("Please stop and physically clear the jam, then press 'Play' to resume operation.")
            if jam_check == "No":
                wash_e = input("Is HMI home screen displaying 'Washer Empty' (Yes or No): ")
                wash_e = wash_e.title()
                if wash_e == "Yes":
                    print("Press stop, gently wipe Washer Infeed sensors free of dust with a clean cloth.")
                    print("Press play to resume operations.")
                if wash_e == "No":
                    print(maintenance)
        if conveyor_op == "No":
            turn_on = input("Are both machines powered on and washer button on HMI is toggled 'ON' (Yes or No): ")
            turn_on = turn_on.title()
            if turn_on == "Yes":
                print(maintenance)
            else:
                print("Turn the machine on.")
    if holding_tray == "No":
        hopper_check = input("Is HMI home screen displaying 'Hopper Full' (Yes or No): ")
        hopper_check = hopper_check.title()
        hopper_check1 = input("Is hopper actually full (Yes or No): ")
        hopper_check1 = hopper_check1.title()
        if hopper_check == hopper_check1:
            print("Inform lead and downstairs team of the bottleneck at the filler - Operation of robot is unaffected.")
        if hopper_check != hopper_check1:
            print(maintenance)

if light_color_orientation == 3:
    fault_check = input("Does HMI display a fault message (Yes or No): ")
    fault_check = fault_check.title()
    if fault_check == "No":
        print(maintenance)
    if fault_check == "Yes":
        print("Read message/follow prompt to address the fault concern as necessary.")
        print("Reset the the E-stop if necessary, then press 'Reset' on the HMI home screen.")
        tray_check = input("Is robot holding a tray in its grippers (Yes or No): ")
        tray_check = tray_check.title()
        if tray_check == "Yes":
            print("From HMI home screen, press 'Release Tray' button to drop tray from gippers.")
            print("From HMI home screen press 'Reset' then 'Play.")
        else:
            print("From HMI home screen press 'Reset' then 'Play'.")
    
if light_color_orientation == 4:
    print("Machine is ready to run!")

if light_color_orientation == 5:
    dolly_empty_check = input("Does the current dolly being picked from have less than half the trays remaining (Yes or No): ")
    dolly_empty_check = dolly_empty_check.title()
    if dolly_empty_check == "Yes":
        print("System is informing operator that dolly is low on trays. Operation is unaffected.")
    if dolly_empty_check == "No":
        print(maintenance)