#This is the final product for an interactive troubleshooting guide
import easygui

version = "Packaging TS Guide"

options = ['filler trays', 'filler cones', 'print issues', 'tilted labels', 'skewed caps', 'robot', 'cancel']

scope_ft = ["All trays", "One or few trays"]
scope_fc = ['All cones(8)', 'One head (4)', 'One set (2)', 'One cone']

light_stack = ['Solid Amber', 'Flashing Amber', 'Solid Red', 'Flashing Red', 'Flashing Green']

em = ['Exit','Also exit']

y_n = ['Yes', 'No']
r_l = ['Left', 'Right']

button = easygui.buttonbox(msg='Where/what is the problem occuring?', title=version, choices=options)

if button == options[0]:
    ft_ccbox_0 = easygui.ccbox(msg= 'Ensure all trays are in their proper positions, continue if problem persists.', title= options[0].title())
    if ft_ccbox_0 == 1:
        ft_button_1 = easygui.buttonbox(msg= 'Are all trays effected or just some of them?', title= options[0].title(), choices= scope_ft)
        if ft_button_1 == scope_ft[0]:
            ft_ccbox_1 = easygui.ccbox(msg='Adjust vibration amplitude as necessary, continue if problem persists.', title= options[0].title())
            if ft_ccbox_1 == 1:
                ft_ccbox_2 = easygui.ccbox(msg='Adjust gate height to control product flow', title=options[0].title())
                if ft_ccbox_2 == 1:
                    ft_end_box = easygui.buttonbox(msg= 'Call maintenance for assistance.',title=options[0].title(), choices=em[0])
        elif ft_button_1 == scope_ft[1]:
            ft_button_2 = easygui.buttonbox(msg='Check magnet polarity. Is polarity correct?', title=options[0].title(), choices=y_n)
            if ft_button_2 == y_n[0]:
                ft_end_box = easygui.buttonbox(msg= 'Call maintenance for assistance.',title=options[0].title(), choices=em[0])
            elif ft_button_2 == y_n[1]:
                ft_ccbox_3 = easygui.ccbox(msg="Swap out tray with its spare, press cancel if problem is resolved.")
                if ft_ccbox_3 == 1:
                    ft_end_box = easygui.buttonbox(msg= 'Call maintenance for assistance.',title=options[0].title(), choices=em)

elif button == options[1]:
    fc_button_0 = easygui.buttonbox(msg='How many filler cones are out of alignment', title=options[1].title(), choices=scope_fc)
    if fc_button_0 == scope_fc[0]:
        fc_button_1 = easygui.buttonbox(msg='Are cones out of alignment in the same direction?', title=options[1].title(), choices=y_n)
        if fc_button_1 == y_n[0]:
            fc_button_3 = easygui.buttonbox(msg='From the bottles perspective, are cones out of alignment to the left or right?',
                                            title=options[1].title(), choices=r_l)
            if fc_button_3 == r_l[1]:
                fc_button_4 = easygui.buttonbox(msg='Perform feedscrew alignment. If problem persists, call maintenance.',
                                                title=options[1].title(), choices=em)
            elif fc_button_3 == r_l[0]:
                fc_button_5 = easygui.buttonbox(msg='Adjust backrail toward bottles. If problem persists, call maintenance.',
                                                title=options[1].title(), choices=em)
        elif fc_button_1 == y_n[1]:
            fc_button_2 = easygui.buttonbox(msg='Adjust cone retaining assemblies for affected cones. If problem persists, call maintenance.',
                                                title=options[1].title(), choices=em)
    elif fc_button_0 == scope_fc[1]:
        fc_button_6 = easygui.buttonbox(msg='Are cones out of alignment in the same direction?', title=options[1].title(), choices=y_n)
        if fc_button_6 == y_n[0]:
            fc_ccbox_0 = easygui.ccbox(msg='Adjust feedscrew position. If problem persists, please continue.',
                                                title=options[1].title())
            if fc_ccbox_0 == 1:
                fc_button_7 = easygui.buttonbox(msg='Adjust cone retaining assemblies for affected cones. If problem persists, call maintenance.',
                                                title=options[1].title(), choices=em)
        elif fc_button_6 == y_n[1]:
            fc_button_8 = easygui.buttonbox(msg='Adjust cone retaining assemblies for affected cones. If problem persists, call maintenance.',
                                                title=options[1].title(), choices=em)
    elif fc_button_0 == scope_fc[2]:
        fc_button_9 = easygui.buttonbox(msg='Adjust cone retaining assemblies for affected cones. If problem persists, call maintenance.',
                                                title=options[1].title(), choices=em)
    elif fc_button_0 == scope_fc[3]:
        fc_button_10 = easygui.buttonbox(msg='Adjust cone retaining assemblies for affected cones. If problem persists, call maintenance.',
                                                title=options[1].title(), choices=em)
        
elif button == options[2]:
    pi_ccbox_0 = easygui.ccbox(msg='Check pad behind the hot stamp. Replace pad if worn. If problem persists, select continue.',
                               title=options[2].title())
    if pi_ccbox_0 == 1:
        pi_ccbox_1 = easygui.ccbox(msg='Check dwell time on hot stamp. Adjust dwell time if necessary. If problem persists please continue.',
                                   title=options[2].title())
        if pi_ccbox_1 == 1:
            pi_ccbox_2 = easygui.ccbox(msg='Ensure hot stamp is printing inside of the no varnish square on the label. If problem persists please continue.',
                                       title=options[2].title())
            if pi_ccbox_2 == 1:
                pi_ccbox_3 = easygui.ccbox(msg='Check labeler air pressure. Adjust as needed in accordance with centerlines. If problem persists please continue.',
                                           title=options[2].title())
                if pi_ccbox_3 == 1:
                    pi_ccbox_4 = easygui.ccbox(msg='Adjust block distance from label as necessary. If problem persists please continue.',
                                                    title=options[2].title())
                    if pi_ccbox_4 == 1:
                        pi_button_0 = easygui.buttonbox(msg='Clean hot stamp. If that does not work, replace the hot stamp with a new one. If problem persists, call maintenance.',
                                                        title=options[2].title(), choices=em)    
                          
elif button == options[3]:
    tl_button_0 = easygui.buttonbox(msg='Does the height and angle of the dual supply arm match the centerlines?',
                                    title=options[3].title(), choices=y_n)
    if tl_button_0 == y_n[0]:
        tl_button_1 = easygui.buttonbox(msg='Is the table level?', title=options[3].title(), choices=y_n)
        if tl_button_1 == y_n[0]:
            tl_button_end = easygui.buttonbox('Call maintenance for assistance.', title=options[3].title(), choices=em)
        elif tl_button_1 == y_n[1]:
            tl_button_end_2 = easygui.buttonbox(msg='Level the table using adjustment points "P" and "N". If problem persists, call maintenance for assistance.',
                                                title=options[3].title(), choices=em)
    elif tl_button_0 == y_n[1]:
        tl_ccbox_0 = easygui.ccbox(msg='Adjust dual supply arm height (U) to match the centerlines for current bottle size. Continue if problem persists.',
                                   title=options[3].title())
        if tl_ccbox_0 == 1:
            tl_ccbox_1 = easygui.ccbox(msg='Adjust dual supply arm angle (Y) to matche the centerlines for current bottle size. Continue if problem persists.',
                                       title=options[3].title())
            if tl_ccbox_1 == 1:
                tl_button_1 = easygui.buttonbox(msg='Is the table level?', title=options[3].title(), choices=y_n)
        if tl_button_1 == y_n[0]:
            tl_button_end = easygui.buttonbox('Call maintenance for assistance.', title=options[3].title(), choices=em)
        elif tl_button_1 == y_n[1]:
            tl_button_end_2 = easygui.buttonbox(msg='Level the table using adjustment points "P" and "N". If problem persists, call maintenance for assistance.',
                                                title=options[3].title(), choices=em)
            
elif button == options[4]:
    sc_ccbox_0 = easygui.ccbox(msg='Verify bottles are flowing evenly into red belts. Adjust red belts if necessary. Continue if problem persists.',
                               title=options[4].title())
    if sc_ccbox_0 == 1:
        sc_ccbox_1 = easygui.ccbox(msg='Evaluate cap pickoff angle (use photo on capper for reference). Adjust as necessary. If problem persists, please continue',
                                   title=options[4].title())
        if sc_ccbox_1 == 1:
            sc_ccbox_2 = easygui.ccbox(msg='Adjust capper height up 5mm. If problem persists call maintenance.',
                                       title=options[4].title())
            if sc_ccbox_2 == 1:
                sc_button_0 = easygui.buttonbox(msg='Are caps loose?', title=options[4].title(), choices=y_n)
                if sc_button_0 == y_n[0]:
                    sc_button_exit = easygui.buttonbox(msg='Adjust capper height down 5mm. If problem persists, call maintenance.',
                                                       title=options[4].title(),choices=em)
                elif sc_button_0 == y_n[1]:
                    sc_button_exit_2 = easygui.buttonbox(msg='Evaluate quality of caps. If caps are out of specification contact QA. If caps are okay call maintenance.',
                                                         title=options[4].title(),choices=em)

elif button == options[5]:
    r_button_0 = easygui.buttonbox("What is the lightstack on the robot displaying?", title=options[5].title(),
                                   choices= light_stack)
    if r_button_0 == light_stack[0]:
        r_button_1 = easygui.buttonbox('Does the HMI display "Robot is paused"?', title=options[5].title(),
                                       choices=y_n)
        if r_button_1 == y_n[0]:
            r_button_exit_0 = easygui.buttonbox(msg='Press play to resume operation.', title=options[5].title(),
                                                choices=em)
        elif r_button_1 == y_n[1]:
            r_button_2 = easygui.buttonbox(msg='Is robot waiting in front of HMI without a tray in its grippers?',
                                           title=options[5].title(), choices=y_n)
            if r_button_2 == y_n[1]:
                r_button_exit_1 = easygui.buttonbox(msg='Call maintenance for assistance.', title=options[5].title(),
                                                    choices=em)
            elif r_button_2 == y_n[0]:
                r_button_3 = easygui.buttonbox(msg='Is there at least one dolly with gummy product loaded and locked into one of the docks?',
                                                title=options[5].title(), choices=y_n)
                if r_button_3 == y_n[0]:
                    r_button_exit_2 = easygui.buttonbox(msg='Call maintenance for assistance.', title=options[5].title(),
                                                    choices=em)
                elif r_button_3 == y_n[1]:
                    r_button_exit_3 = easygui.buttonbox(msg='Load a full dolly into at least one dock to resume operation.',
                                                        title=options[5].title(), choices=em)
    elif r_button_0 == light_stack[1]:
        r_button_4 = easygui.buttonbox(msg='Is robot holding empty tray above washer infeed conveyor?', title=options[5].title(),
                                       choices=y_n)
        if r_button_4 == y_n[1]:
            r_button_5a = easygui.buttonbox(msg='Is HMI Home Screen displaying "Hopper Full"?', title=options[5].title(),
                                            choices=y_n)
            if r_button_5a == y_n[0]:
                r_button_5b = easygui.buttonbox(msg='Is hopper actually full?', title=options[5].title(), choices=y_n)
                if r_button_5b == r_button_5a:
                    r_button_exit_3 = easygui.buttonbox(msg='Inform lead and downstairs team of bottleneck at filler. Robot is unaffected.',
                                                        title=options[5].title(), choices=em)
                elif r_button_5b != r_button_5a:
                    r_button_exit_4 = easygui.buttonbox(msg='Call maintenance for assistance.', title=options[5].title(),
                                                    choices=em)
            if r_button_5a == y_n[1]:
                r_button_5b = easygui.buttonbox(msg='Is hopper actually full?', title=options[5].title(), choices=y_n)
                if r_button_5b == r_button_5a:
                    r_button_exit_3 = easygui.buttonbox(msg='Inform lead and downstairs team of bottleneck at filler. Robot is unaffected.',
                                                        title=options[5].title(), choices=em)
                elif r_button_5b != r_button_5a:
                    r_button_exit_4 = easygui.buttonbox(msg='Call maintenance for assistance.', title=options[5].title(),
                                                    choices=em)
        elif r_button_4 == y_n[0]:
            r_button_6 = easygui.buttonbox(msg='Are tray washer chain and conveyor powered on and moving?',
                                           title=options[5].title(), choices=y_n)
            if r_button_6 == y_n[1]:
                r_button_7 = easygui.buttonbox(msg='Are both machines powered on and washer button on HMI is toggled ON (Green)?',
                                               title=options[5].title(), choices=y_n)
                if r_button_7 == y_n[0]:
                    r_button_exit_5 = easygui.buttonbox(msg='Call maintenance for assistance.', title=options[5].title(),
                                                    choices=em)
                elif r_button_7 == y_n[1]:
                    r_button_exit_6 = easygui.buttonbox(msg='Turn on tray wash chain and conveyor. If problem persists, call maintenance for assistance.',
                                                        title=options[5].title(), choices=em)
            elif r_button_6 == y_n[0]:
                r_ccbox_0 = easygui.ccbox(msg="Check for tray jam, and clear jammed tray if one is found. If problem persists, please continue.",
                                          title=options[5].title())
                if r_ccbox_0 == 1:
                    r_button_8 = easygui.buttonbox(msg='Is HMI Home Screen displaying "Washer Empty"?', title=options[5].title(),
                                                   choices=y_n)
                    if r_button_8 == y_n[0]:
                        r_button_exit_7 = easygui.buttonbox(msg='Press Stop, gently wipe washer infeed sensor with a clean cloth.',
                                                            title=options[5].title(), choices=em)
                    if r_button_8 == y_n[1]:
                        r_button_exit_8 = easygui.buttonbox(msg='Call maintenance for assistance.', title=options[5].title(),
                                                    choices=em)
    elif r_button_0 == light_stack[2]:
        r_button_9 = easygui.buttonbox(msg='Does the HMI display a fault message?', title=options[5].title(), choices=y_n)
        if r_button_9 == y_n[1]:
            r_button_exit_9 = easygui.buttonbox(msg='Call maintenance for assistance.', title=options[5].title(),
                                                    choices=em)
        elif r_button_9 == y_n[0]:
            r_ccbox_1 = easygui.ccbox(msg='Follow prompt on HMI to address fault. Reset E-stop if necessary and hit reset on HMI panel.',
                                      title=options[5].title())
            if r_ccbox_1 == 1:
                r_button_exit_10 = easygui.buttonbox(msg='Robot should not be holding tray in grippers. If it is, make arrangment to safely drop tray, then press "Release Tray".',
                                                     title=options[5].title(), choices=em)
    elif r_button_0 == light_stack[3]:
        r_button_9 = easygui.buttonbox(msg='Does the HMI display a fault message?', title=options[5].title(), choices=y_n)
        if r_button_9 == y_n[1]:
            r_button_exit_9 = easygui.buttonbox(msg='Call maintenance for assistance.', title=options[5].title(),
                                                    choices=em)
        elif r_button_9 == y_n[0]:
            r_ccbox_1 = easygui.ccbox(msg='Follow prompt on HMI to address fault. Reset E-stop if necessary and hit reset on HMI panel.',
                                      title=options[5].title())
            if r_ccbox_1 == 1:
                r_button_exit_10 = easygui.buttonbox(msg='Robot should not be holding tray in grippers. If it is, make arrangment to safely drop tray, then press "Release Tray".',
                                                     title=options[5].title(), choices=em)
    elif r_button_0 == light_stack[4]:
        r_button_exit_11 = easygui.buttonbox(msg='If current dolly has less than half of its stack remaining, the machine is telling you to feed it more. Otherwise contact maintenance.',
                                             title=options[5].title(), choices=em)
            
else:
    'No troubleshooting required.'
