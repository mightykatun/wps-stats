print("please wait...")
from nltk.corpus import words
import matplotlib.pyplot as plt
import random as rd
import time as tm
done = 0
failed = 0
speeds = []
while True:
    rst = input("reset progress y/n ")
    if rst == "y":
        while True:
            check = input("are you sure y/n ")
            if check == "n":
                break
            if check == "y":
                file = open("progress.txt", "r")
                content = file.readlines()
                file.close()
                content[0] = "-1\n"
                content[1] = "[0]"
                output = open("progress.txt", "w")
                output.writelines(content)
                output.close()
                i = -1
                averages = []
                print("progress reset")
                break
            else:
                print("input exception")
        break
    if rst == "n":
        i = -1
        averages = []
        break
    else:
        print("input exception")
while True:
    if rst == "y" and check == "y":
        break
    load = input("load progress y/n ")
    if load == "y":
        file = open("progress.txt")
        content = file.readlines()
        i = float(content[0])
        list1 = list(content[1].strip("][").split(", "))
        averages = list(map(float, list1))
        file.close()
        print("progress loaded")
        break
    elif load == "n":
        i = -1
        averages = []
        break
    else:
        print("input exception")
while True:
    show = input("show data graph y/n ")
    if show == "n":
        break
    if show == "y":
        xs = averages
        plt.plot(xs)
        plt.xlabel("attempts")
        plt.ylabel("letters/s")
        plt.show()
        break
    else:
        print("input exception")
while True:
    lvl = input("level hard/easy ")
    if lvl == "hard":
        miss = 3
        break
    elif lvl == "easy":
        miss = 10
        break
    else:
        print("input exception")
while True:
    i = i + 1
    while int(failed) < miss:
        wordlist = words.words()
        word = wordlist[rd.randint(0, 236735)]
        length = len(word)
        tm1 = tm.time()
        written = input("%s " % word)
        tm2 = tm.time()
        time = tm2 - tm1
        if written == word:
            done = done + 1
            speed =  length / time
            speeds.append(round(speed, 3))
            print("%s letters/s" %(round(speed, 3)))
        else:
            failed = failed + 1
            if int(failed) < miss:
                print("%s mistakes left" %(miss - failed))
    print("out of attempts")
    print("success rate %s / %s | %s %%" %(done, (done + failed), round(done/(failed + done), 2)))
    try:
        averagei = round((sum(speeds) / len(speeds)), 3)
    except ZeroDivisionError:
        print("too many mistakes | 0 letters/s")
        averages.append(float(0))
    else:
        averages.append(float(averagei))
        print("average letters/s %s" %(averagei))
    if i > 0:
        av1 = averages[int(i)]
        av2 = averages[int(i - 1)]
        diff = av1 - av2
        if diff > 0:
            print("new average is %s letters/s faster" %(round(diff, 3)))
        else:
            print("new average is %s letters/s slower" %(abs(round(diff,3))))
    print("overall average %s" %(round((sum(averages) / len(averages)), 3)))
    while True:
        choice = input("continue y/n ")
        if choice == "y" or choice == "n":
            break
        else:
            print("input exception")
    if choice == "n":
        while True:
            save = input("save progress y/n ")
            if save == "y":
                file = open("progress.txt", "r")
                content = file.readlines()
                file.close()
                a = str(i), "\n"
                content[0] = "".join(map(str, a))
                b = str(averages), ""
                content[1] = "".join(map(str, b))
                output = open("progress.txt", "w")
                output.writelines(content)
                output.close()
                print("progress saved")
                break
            elif save == "n":
                break
            else:
                print("input exception")
        break
    else:
        failed = 0
        done = 0
        speeds = []
input("exit with enter")
quit()




