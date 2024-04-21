from functions import roll, get_data
import PySimpleGUI as sg

data = get_data()
keyes = [k for k in data[0]][1:]
results = []

print(keyes)

label_sk = sg.Text("Skills:")
skill_list = sg.Listbox(values=keyes, key="skill", enable_events=True, size=(20, len(keyes)))
results_list = sg.Listbox(values=results, key="result", size=(30, len(data)))
roll_button = sg.Button("Roll")
exit_button = sg.Button("Exit")


layout = [
    [label_sk],
    [skill_list, roll_button, results_list],
    [exit_button]
]

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

        case "Exit" | sg.WIN_CLOSED:
            break

window.close()
