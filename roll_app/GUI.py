from functions import roll, get_data, get_order
import PySimpleGUI as sg

data = get_data()
keyes = [k for k in data[0]][1:]
results = []
order = []

print(keyes)

label_sk = sg.Text("Skills:")
label_to = sg.Text("Turn Order:")

add_turn = sg.InputText(key="turn", do_not_clear=False, size=30)

skill_list = sg.Listbox(values=keyes, key="skill", enable_events=True, size=(20, len(keyes)))
results_list = sg.Listbox(values=results, key="result", size=(30, len(data)))
turn_order = sg.Listbox(values=order, key="order", enable_events=True, size=(30, 10))

roll_button = sg.Button("Roll")
exit_button = sg.Button("Exit")
add_button = sg.Button("Add Turn")
next_button = sg.Button("Next")
remove_button = sg.Button("Remove")

col_1 = sg.Column([
    [label_sk],
    [skill_list, roll_button, results_list]
])

col_2 = sg.Column([
    [label_to],
    [turn_order, next_button, remove_button],
    [add_turn, add_button],
])

layout = [[col_1, sg.VerticalSeparator(), col_2]]

window = sg.Window("roll App", layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Roll":
            try:
                results.clear()
                for player in data:
                    results.append(roll(values["skill"][0], player))
                window["result"].update(values=results)
            except IndexError:
                continue

        case "Add Turn":
            try:
                turn = values["turn"]
                order = get_order(turn, order)
                window["order"].update(values=order)
            except IndexError:
                continue

        case "Next":
            try:
                order.append(order.pop(0))
                window["order"].update(values=order)
            except IndexError:
                continue

        case "Remove":
            try:
                turn = values["order"][0]
                index = order.index(turn)
                order.pop(index)
                window["order"].update(values=order)
            except IndexError:
                continue

        case "Exit" | sg.WIN_CLOSED:
            break

window.close()
