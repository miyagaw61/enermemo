#       RevTrace - Register/Valiable Tracer For Reversing
#
#       Copyright (C) 2017 miyagaw61 <miyagaw61 at miyagaw61.github.io>
#
#       License: see LICENSE file for details
#

from enert import *
import re
import better_exceptions
better_exceptions.MAX_LENGTH = None

if len(sys.argv) < 2:
    print("Usage: python enermemo.py [conf_file/snapshot_file]")
    exit()

regex_n = re.compile(r"\n")
data = file(sys.argv[1]).linedata()
lst = []
tags = []
default = []
history = []
if data[0] == "[+]snapshot\n":
    history_lst = []
    lst = data[1].split(":")
    tags = data[2].split(":")
    counter = 0
    for lines_i in range(3, len(data)):
        lines_splited = data[lines_i].split(":")
        history.append([])
        for split_i in range(len(lines_splited)):
            history[counter].append(lines_splited[split_i])
        counter = counter + 1
else:
    for var in data:
        lst.append(regex_n.sub("", var.split(":")[1]))
    for var in data:
        tags.append(regex_n.sub("", var.split(":")[0]))
    for var in data:
        default.append(regex_n.sub("", var.split(":")[2]))
    for i in range(len(lst)):
        history.append([default[i]])
term_y, term_x = get_term_size()
print("="*term_x)
sys.stdout.write(red("[+]EnerMemo", "bold"))
s = screen()
print("\n" + "="*term_x)
for i in range(len(lst)):
    print(black_white(" ") + " " + regex_n.sub("", lst[i]) + " : " + regex_n.sub("", history[i][-1]))
header = 2
footer = 0
i = 0
up(header + len(lst) + footer)
sys.stdout.write(red("[+]EnerMemo : ", "bold"))
save()
s.addstr(1, header+0, black_red("> ", "bold") + black_green(lst[0], "bold") + black_white(" : ", "bold") + black_white(history[0][-1], "bold"))

def enter_function():
    restore()
    all_delete()
    sys.stdout.write(red("[+]EnerMemo : ", "bold") + green(lst[i], "bold"))
    save()
    input_data = raw_input(blue(" --> ", "bold"))
    if not len(input_data) == 0:
        history[i].append(input_data)
        up(1)
        all_delete()
        sys.stdout.write(red("[+]EnerMemo : ", "bold"))
        save()
        s.overwrite(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold") + black_white(" : ", "bold") + black_white(input_data, "bold"))
        restore()
    else:
        up(1)
        all_delete()
        sys.stdout.write(red("[+]EnerMemo : ", "bold"))
        save()
        restore()

def clear_history():
    down(header+len(lst))
    lines_delete(100)
    restore()

def print_history():
    clear_history()
    s.overwrite(1, header+len(lst), "="*term_x)
    s.overwrite(1, header+len(lst)+1, blue("[+]HISTORY : ", "bold") + green(lst[i], "bold"))
    j = 0
    for var in history[i]:
        j = j + 1
        s.overwrite(1, header+len(lst)+1+j, var)

print_history()
while 1:
    key = getch()
    if (key == "j" or ord(key) == DOWN):
        old = i
        i = i + 1
        if old == len(lst)-1:
            i = 0
        s.overwrite(1, header+old, black_green(" ") + " " + lst[old] + " : " + history[old][-1])
        s.overwrite(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold") + black_white(" : " + history[i][-1], "bold"))
        print_history()
    elif (key == "k" or ord(key) == UP):
        old = i
        i = i - 1
        if old == 0:
            i = len(lst)-1
        s.overwrite(1, header+old, black_green(" ") + " " + lst[old] + " : " + history[old][-1])
        s.overwrite(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold") + black_white(" : " + history[i][-1], "bold"))
        print_history()
    elif key in tags:
        old = i
        varlst = []
        if tags.count(key) > 1:
            for j in range(len(tags)):
                if key == tags[j]:
                    varlst.append(j)
            if old in varlst:
                oldindex = varlst.index(old)
                if varlst[oldindex] == varlst[-1]:
                    i = varlst[0]
                else:
                    i = varlst[oldindex+1]
            else:
                i = varlst[0]
        else:
            i = tags.index(key)
        s.overwrite(1, header+old, black_green(" ") + " " + lst[old] + " : " + history[old][-1])
        s.overwrite(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold") + black_white(" : " + history[i][-1], "bold"))
#    elif key == "@": #for 2byte tags
#        while 1:
#            key = getch()
#            if key == "a":
#                old = i
#                i = 4
#                s.addstr(1, header+old, black_green(" ") + " " + lst[old])
#                s.addstr(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold"))
#                break
#            elif key == "b":
#                old = i
#                i = 5
#                s.addstr(1, header+old, black_green(" ") + " " + lst[old])
#                s.addstr(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold"))
#                break
#            elif key == "@":
#                continue
#            else:
#                break
    elif key == "g" or key == "0":
        old = i
        i = 0
        s.overwrite(1, header+old, black_green(" ") + " " + lst[old] + " : " + history[old][-1])
        s.overwrite(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold") + black_white(" : " + history[i][-1], "bold"))
    elif key in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if int(key) < len(lst):
            old = i
            i = int(key)
            s.overwrite(1, header+old, black_green(" ") + " " + lst[old] + " : " + history[old][-1])
            s.overwrite(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold") + black_white(" : " + history[i][-1], "bold"))
    elif key == "G" or key == "$":
        old = i
        i = len(lst)-1
        s.overwrite(1, header+old, black_green(" ") + " " + lst[old] + " : " + history[old][-1])
        s.overwrite(1, header+i, black_red("> ", "bold") + black_green(lst[i], "bold") + black_white(" : " + history[i][-1], "bold"))
    elif key == "+":
        restore()
        all_delete()
        name = raw_input(red("[+]name : ", "bold"))
        up(1)
        all_delete()
        tag = raw_input(red("[+]tag : ", "bold"))
        tags.append(tag)
        up(1)
        all_delete()
        default_data = raw_input(red("[+]default : ", "bold"))
        history.append([default_data])
        up(1)
        all_delete()
        sys.stdout.write(red("[+]EnerMemo : ", "bold"))
        save()
        lst.append(name)
        s.overwrite(1, header+len(lst)-1, black_white(" ", "bold") + " " + name + " : " + default_data)
        restore()
        print_history()
    elif ord(key) == ENTER:
        enter_function()
        print_history()
    elif ord(key) == SPACE:
        clear_history()
    elif key == "q" or ord(key) == CTRL_C or ord(key) == CTRL_D:
        up(1)
        lines_delete(100)
        exit()
    elif ord(key) == CTRL_S:
        restore()
        all_delete()
        snapshot_name = raw_input(red("[+]snapshot_name : ", "bold"))
        f = file(snapshot_name)
        if f.exist():
            while 1:
                up(1)
                all_delete()
                ans = raw_input(red("[!]already existed. overwrite? [y/n] : ", "bold"))
                if ans == "y":
                    up(1)
                    all_delete()
                    sys.stdout.write(red("[+]EnerMemo : ", "bold"))
                    save()
                    f.write("[+]snapshot\n")
                    f.add(lst[0])
                    for lst_i in range(1, len(lst)):
                        f.add(":" + lst[lst_i])
                    f.add("\n")
                    f.add(tags[0])
                    for tags_i in range(1, len(tags)):
                        f.add(":" + tags[tags_i])
                    for lst_i in range(len(lst)):
                        f.add("\n")
                        f.add(history[lst_i][0])
                        for history_i in range(1, len(history[lst_i])):
                            f.add(":" + history[lst_i][history_i])
                    break
                elif ans == "n":
                    break
                else:
                    continue
        else:
            up(1)
            all_delete()
            sys.stdout.write(red("[+]EnerMemo : ", "bold"))
            save()
            f.write("[+]snapshot\n")
            f.add(lst[0])
            for lst_i in range(1, len(lst)):
                f.add(":" + lst[lst_i])
            f.add("\n")
            f.add(tags[0])
            for tags_i in range(1, len(tags)):
                f.add(":" + tags[tags_i])
            for lst_i in range(len(lst)):
                f.add("\n")
                f.add(history[lst_i][0])
                for history_i in range(1, len(history[lst_i])):
                    f.add(":" + history[lst_i][history_i])
        restore()
        print_history()
