import streamlit as st
import app1_functions


# to run, type in the Terminal window:
# streamlit run web_gui.py

todos = app1_functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    print(todo + " to append")
    todos.append(todo)

    app1_functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app subheader")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        app1_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

