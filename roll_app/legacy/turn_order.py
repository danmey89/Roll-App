

def get_order(set_l, order_l):
    new = [int(v) if v.isnumeric() else v for v in set_l.split()]
    new = [v.capitalize() if type(v) is str else v for v in new]
    if len(new) == 2:
        order_l.append(new)
        order_l = sorted(order_l, key=lambda pair: pair[1], reverse=True)
        return order_l
    else:
        print("please enter exactly two arguments.")


order = list()

while True:
    set_i = input("add name and initiative, remove name, show or next: ")
    if set_i.startswith("add"):
        set_i = set_i[4:]
        order = get_order(set_i, order)
        for i in order:
            print(i)
    elif set_i.startswith("remove "):
        set_i = set_i.split()
        try:
            for i in order:
                if i[0] == set[1]:
                    order.remove(i)
            for i in order:
                print(i)
        except IndexError:
            print("command not valid.")
            continue
    elif set_i.startswith("next"):
        order.append(order.pop(0))
        for i in order:
            print(i)
