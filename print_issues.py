#After users have selected machine and issue

outie = "Excellent, please select 'Exit' to return to the home screen."
#Hot stamp back plate pad check
print("Check pad behind the hot stamp.")
print("If the pad is worn, replace with new pad.")
#Dwell time setting check
check_0 = input("Did this resolve the issue (Yes or No): ")
check_0 = check_0.title()
if check_0 == "Yes":
    print(outie)
else:
    print('\nCheck dwell time setting.')
    print('If dwell time is incorrect, adjust as necessary.')
#Making sure print is in the no varnish zone
    check_1 = input(" Did this resolve the issue (Yes or No): ")
    check_1 = check_1.title()
    if check_1 == "Yes":
        print(outie)
    else:
        print("\nEnsure hot stamp is printing in the no varnish square.")
        print("Adjust print position to ensure print is in the no varnish square")
#Air pressure in the hot stamp check
        check_2 = input("Did this resolve the issue (Yes or No): ")
        check_2 = check_2.title()
        if check_2 == "Yes":
            print(outie)
        else:
            print("\nCheck air pressure at hot stamp.")
            print("Adjust air pressure to correct settings. Refer to centerlines as needed.")
#Stamp block distance from label check
            check_3 = input("Did this resolve the issue (Yes or No): ")
            check_3 = check_3.title()
            if check_3 == "Yes":
                print(outie)
            else:
                print("\nCheck stamp block's distance from the label.")
                print("If the block is too far/close to the label, adjust as necessary.")
#Making sure the hot stamp is clean
                check_4 = input("Did this resolve the issue (Yes or No): ")
                check_4 = check_4.title()
                if check_4 == "Yes":
                    print(outie)
                else:
                    print("\nRemove and clean hot stamp.")
                    print("Replace hot stamp when finished")
#Changing out the hot stamp. Should be last resort
                    check_5 = input("Did this resolve the issue (Yes or No): ")
                    check_5 = check_5.title()
                    if check_5 == "Yes":
                        print(outie)
                    else:
                        print("\nReplace hot stamp.")
#Maintenance call
                        check_6 = input("Did this resolve the issue (Yes or No): ")
                        check_6 = check_6.title()
                        if check_6 == "Yes":
                            print(outie)
                        else:
                            print("\nCall maintenance")