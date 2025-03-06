import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"].strip()
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()


st.title("My Todo App")
st.subheader("Mobin says Hey!!")
st.write("Start to manage your time from today!!")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index+1})todo")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{index+1})todo"]
        st.rerun()

st.text_input(label="Enter your todo",placeholder="add your todo here",
              on_change= add_todo, key= 'new_todo')
print("hello")

# st.session_state