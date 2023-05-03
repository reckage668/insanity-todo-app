import functions
import PySimpleGUI as sg

label = sg.Text("Type in a task to do.")
input_box = sg.InputText(tooltip="Enter a to do")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
print("Hello.")
window.read()
print("Goodbye.")
window.close()