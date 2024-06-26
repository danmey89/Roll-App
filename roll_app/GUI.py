from functions import roll, get_data, get_order, update_characters, get_labels
import PySimpleGUI as sg
import json


sg.theme("DarkAmber")

try:
    data = get_data()
except FileNotFoundError:
    update_characters()
    data = get_data()
except json.decoder.JSONDecodeError:
    update_characters()
    data = get_data()

try:
    keys = [k for k in data[0]["proficiencies"]]
    characters = [k for k in get_labels(data)]
except IndexError:
    update_characters()
    data = get_data()
    keys = [k for k in data[0]["proficiencies"]]
    characters = [k for k in get_labels(data)]

results = []
order = []


label_sk = sg.Text("Skills:")
label_to = sg.Text("Turn Order:")
label_nt = sg.Text("Enter new turn:")
label_ch = sg.Text("Characters")

add_turn = sg.InputText(tooltip="Name", key="turn", do_not_clear=False, size=20)
add_num = sg.InputText(tooltip="Number", key="num_t", do_not_clear=False, size=5)

skill_list = sg.Listbox(values=keys, key="skill", enable_events=True, no_scrollbar=True,
                        size=(20, len(keys)))
results_list = sg.Listbox(values=results, key="result", size=(45, 10))
turn_order = sg.Listbox(values=order, key="order", enable_events=True, size=(30, 10))

roll_button = sg.Button("Roll")
exit_button = sg.Button("Exit")
add_button = sg.Button("Add Turn")
next_button = sg.Button("Next")
remove_button = sg.Button("Remove")
clear_t_button = sg.Button("Clear", key="Clear_t")
clear_r_button = sg.Button("Clear", key="Clear_r")
update_button = sg.Button("Update all characters", key="update")

char_list_l = [[sg.Text(ch)] for ch in characters]
char_list = sg.Frame('Characters', char_list_l)

col_1 = sg.Column([
    [label_sk],
    [skill_list, sg.Column([[char_list], [roll_button, clear_r_button], [results_list], [update_button]])]
])

col_2 = sg.Column([
    [label_to],
    [turn_order, sg.Column([[next_button], [remove_button], [clear_t_button]])],
    [label_nt],
    [add_turn, add_num, add_button],
])

layout = [[col_1, sg.VerticalSeparator(), col_2]]

window = sg.Window("Game Mastery App", layout, font=("Helvetica", 14))

while True:
    event, values = window.read()
    match event:
        case "Roll":
            try:
                results.append(values["skill"][0])
                for player in data:
                    results.append(roll(values["skill"][0], player))
                window["result"].update(values=results)
                window["result"].set_vscroll_position(1)
            except IndexError:
                continue

        case "Add Turn":
            try:
                turn = values["turn"]
                number = values["num_t"]
                order = get_order(number, turn, order)
                window["order"].update(values=order)
            except IndexError:
                continue
            except ValueError:
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

        case "Clear_t":
            order.clear()
            window["order"].update(values=order)

        case "Clear_r":
            results.clear()
            window["result"].update(values=results)

        case "update":
            update_characters()

        case "Exit" | sg.WIN_CLOSED:
            break

window.close()
