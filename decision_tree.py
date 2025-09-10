print("Welcome to this here life simulator. You are a 4in tungsten cube which is somehow capable of making decisions. You are currently sitting on the edge of the roof of a 5 story building. The edge is slightly sloped towards the street. It is May 23rd, 1997. You decide to begin making decisions at exactly 08:07 AM.")

begin = int(input("(Type the number for the option you want to select.)\n1. Stay perfectly still.\n2. Slide off the edge of the roof.\n3. Destroy the building."))
if begin == 1:
    print("You remain still. Some moss begins to grow towards you.")
    remainingstill1 = int(input("(Type the number for the option you want to select.)\n1. Remain still.\n2. Slide off the roof.\n3. Fight the moss."))
    if remainingstill1 == 1:
        print("You continue to remain still. The moss grows closer.")
        remainingstill2 = int(input("1. Slide off the roof.\n2. Remain still.\n 3. Move to the other side of the building."))
        if remainingstill2 == 2:
            print("You continue to remain still. The moss has nearly reached you.")
            remainingstill3 = int(input("1. Remain still.\n2. Slide off the roof."))
            if remainingstill3 == 1:
                print("You continue to remain still. The moss has made contact.")
                remainingstill4 = int(input("1. Remain still.\n2. Roll away from the moss."))
                if remainingstill4 == 1:
                    print("You continue to remain still. The moss has taken over. This does not bode well for your continued ability to make decisions.")
                    print("-----GAME OVER-----")
                    quit(0)
                elif remainingstill4 == 2:
                    print("You attempt to roll away from the moss. The moss does not allow this. This does not bode well for your continued ability to make decisions.")
                    print("-----GAME OVER-----")
                    quit(0)
                else:
                    print("You attempt to do something that isn't possible. The universe was not happy about this. You suddenly get launched into the air. You appear to be flying directly into the sun. The sun could not withstand the impact, and supernovas.")
                    print("-----GAME OVER-----")
                    quit(42)
            elif remainingstill3 == 2:
                print("You slide off the edge of the building. The moss was not happy about this. You ignore it.\nYou land on the nearby sidewalk, smashing the rectangle you land on to pieces.")
                offbuildingpremoss1 = int(input("1. Roll away from the sidewalk.\n2. Remain still."))
                if offbuildingpremoss1 == 1:
                    print("You notice the moss is beginning to grow over the entire building. Seeing this, you roll away from it.\nYou find yourself sitting on the back edge of an armored truck.")
                    armoredtruck1 = int(input("1. Roll off the truck while it is moving.\n2. Wait until the truck stops."))
                    if armoredtruck1 == 1:
                        print("You roll off the truck while it's moving. You begin to slowly float upwards.")
                        armoredtruck2 = int(input("1. Do nothing.\n2. Redefine the laws of physics."))
                        if armoredtruck2 == 1:
                            print("You are now in the upper layers of the atmosphere.")
                            atmo = int(input("1. Drop back to the earth.\n2. Remain here."))
                            if atmo == 1:
                                print("You drop back towards the earth. For some reason, a bright red aircraft is in your path. You slam into it, piercing the hull, and falling through the vehicle. A rather large ruby shatters beneath you before you reach the lower hull.\nWhen you hit the earth, you are going so fast that you tunnel through the earth.\n You are now in outer space.")
                                print("A silver sphere floats towards you. For some reason, for a second you think you hear it shouting 'SPAAACE!'\n This was too much to handle.")
                                print("-----GAME OVER-----")
                            elif atmo == 2:
                                print("You decide that being in the upper atmosphere is rather nice. You give up your ability to make decisions.")
                                print("-----GAME OVER-----")
                            else:
                                print(
                                    "You attempt to do something that isn't possible. The universe was not happy about this. You suddenly get launched into the air. You appear to be flying directly into the sun. The sun could not withstand the impact, and supernovas.")
                                print("-----GAME OVER-----")
                                quit(42)
                    elif armoredtruck1 == 2:
                        print("You decide to wait until the truck stops. While you wait, you notice in the far distance some moss growing towards the road.\nThe truck has stopped.")
                        armoredtruckwait1 = int(input("1. Roll off the truck.\n2. Remain still."))
                        if armoredtruckwait1 == 1:
                            print("You roll off the truck. The ground could not handle the force of your landing. The only thing holding the planet together is the moss.\nYou fall towards the moss. The moss takes over. This is not good for your ability to make decisions.")
                            print("-----GAME OVER-----")
                        elif armoredtruckwait1 == 2:
                            print("You remain still. The truck driver notices you sitting on the truck, and decides to attempt to move you.")
                            armoredtruckwait2 = int(input("1. Allow yourself to be moved.\n2. Remove the truck driver."))
                            if armoredtruckwait2 == 1:
                                print("You allow yourself to be moved. The truck driver grabs you, tossing you on the ground nearby.\nYou land in a patch of moss.\nThe moss takes over.\nYou had no control over this.")
                                print("-----GAME OVER-----")
                                quit(0)
                            elif armoredtruckwait2 == 2:
                                print("You decide to remove the truck driver. You fly into their chest at a speed the truck itself cannot match. The truck driver is launched into the distance.\nYou aren't sure what to do now.\nYou can't go particularly far.")
                                armoredtruckwait3 = int(input("1. Go to the moss."))
                                if armoredtruckwait3 == 1:
                                    print("You move towards the moss.\nThe moss grows towards you.\nYou make contact with the moss.\nThe moss takes over.\nThis was entirely your decision.")
                                    print("-----GAME OVER-----")
                                    quit(0)
                                else:
                                    print(
                                        "You attempt to do something that isn't possible. The universe was not happy about this. You suddenly get launched into the air. It appears you are flying directly into the sun. The sun could not withstand the impact, and supernovas.")
                                    print("-----GAME OVER-----")
                                    quit(42)
                        else:
                            print(
                                "You attempt to do something that isn't possible. The universe was not happy about this. You suddenly get launched into the air. It appears you are flying directly into the sun. The sun could not withstand the impact, and supernovas.")
                            print("-----GAME OVER-----")
                            quit(42)
                    else:
                        print(
                            "You attempt to do something that isn't possible. The universe was not happy about this. You suddenly get launched into the air. It appears you are flying directly into the sun. The sun could not withstand the impact, and supernovas.")
                        print("-----GAME OVER-----")
                        quit(42)
                elif offbuildingpremoss1 == 2:
                    print("You remain where you are.\nSomeone decides to grab you, and throws you into the nearby swimming pool.\nThe lifeguard at the swimming pool jumps in after you.\nThey grab you.")
                    pool = int(input("1. Defy the laws of physics.\n2. Do not."))
