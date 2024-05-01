import os

def perceptron():
    os.system("clear")
    
    title = """
   ___                        _                   
  / _ \___ _ __ ___ ___ _ __ | |_ _ __ ___  _ __  
 / /_)/ _ \ '__/ __/ _ \ '_ \| __| '__/ _ \| '_ \ 
/ ___/  __/ | | (_|  __/ |_) | |_| | | (_) | | | |
\/    \___|_|  \___\___| .__/ \__|_|  \___/|_| |_|
                       |_|                        
    """

    print(title)
    print('Hello to this small perceptron educational example. For learning reasons this perceptron needs all input values and does not work with learning algorithm. There are four x values with one weight each you need to define. Have fun :)')

    meaning_ques = "\nType in meaning of value x (question): "
    value_ques = "Type in first binary value x (0 - false/ 1 -  true): "
    weight_ques = "Type in weight of first value w (0.0-1.0, 0.0 = general / 1.0 very meanigful): "

    run = str(input("Do you want to start? (y/n): "))

    while run == "y":
        m1 = input(f"{meaning_ques}")
        if m1 == "":
            run = "n"
            break
        x1 = input(f"{value_ques}")
        w1 = input(f"{weight_ques}")
        try:
            x1 = int(x1)
            w1 = float(w1)
        except ValueError:
            print("Please input correct format")
            while True:
                try:
                    x1 = int(input(f"{value_ques}"))
                    w1 = float(input(f"{weight_ques}"))
                    break
                except ValueError:
                    print("Please input correct format")

        sum1 = x1 * w1
        print(f"\nfirst input {m1}: {sum1}")

        m2 = input(f"{meaning_ques}")
        if m2 == "":
            run = "n"
            break
        x2 = input(f"{value_ques}")
        w2 = input(f"{weight_ques}")
        try:
            x2 = int(x2)
            w2 = float(w2)
        except ValueError:
            print("Please input correct format")
            while True:
                try:
                    x2 = int(input(f"{value_ques}"))
                    w2 = float(input(f"{weight_ques}"))
                    break
                except ValueError:
                    print("Please input correct format")

        sum2 = x2 * w2
        print(f"\nsecond input {m2}: {sum2}")

        m3 = input(f"{meaning_ques}")
        if m3 == "":
            run = "n"
            break
        x3 = input(f"{value_ques}")
        w3 = input(f"{weight_ques}")
        try:
            x3 = int(x3)
            w3 = float(w3)
        except ValueError:
            print("Please input correct format")
            while True:
                try:
                    x3 = int(input(f"{value_ques}"))
                    w3 = float(input(f"{weight_ques}"))
                    break
                except ValueError:
                    print("Please input correct format")

        sum3 = x3 * w3
        print(f"\nthird input {m3}: {sum3}")

        m4 = input(f"{meaning_ques}")
        if m4 == "":
            run = "n"
            break
        x4 = input(f"{value_ques}")
        w4 = input(f"{weight_ques}")
        try:
            x4 = int(x4)
            w4 = float(w4)
        except ValueError:
            print("Please input correct format")
            while True:
                try:
                    x4 = int(input(f"{value_ques}"))
                    w4 = float(input(f"{weight_ques}"))
                    break
                except ValueError:
                    print("Please input correct format")


        sum4 = x4 * w4
        print(f"\nfourth input {m4}: {sum4}")

        decision = input("Type in what the decision is about: ")
        threshold = (input("Type in your threshold (higher values are true, lower are false (default 2.0 if no input)): "))
        if threshold == "":
            threshold = 2.0
        else:
            float(threshold)

        if sum1 + sum2 + sum3 + sum4 >= threshold:
            print(f"\nThe decision '{decision}' has made: it is true!")
        else: 
            print(f"\nThe decision '{decision}' has made: it is false!")
    
        run = str(input("Do you want to continue with a new perceptron?: (y/n)"))


    if run == "n":
        print("\n\nThank you for learning :) You have now exited the perceptron learning program.")

perceptron()
