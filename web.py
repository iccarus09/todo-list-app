import streamlit as st
import main_functions

my_list = main_functions.get_todos()
my_deletes = main_functions.get_deletes()

def add_todo():
    todo = st.session_state["new_todo"].title()+'\n'
    my_list.append(todo)
    main_functions.write_todos(my_list)
    st.session_state["new_todo"] = ""

st.title("To-do list")
st.subheader("Newly added items")

for index, item in enumerate(my_list):
    check_box = st.checkbox(item, key=item)
    if check_box:
        my_deletes.append(item)
        main_functions.write_deletes(my_deletes)
        my_list.pop(index)
        main_functions.write_todos(my_list)
        main_functions.get_todos()
        del st.session_state[item]
        st.rerun()


st.text_input(label='Enter your todo', placeholder='enter', on_change=add_todo, key='new_todo')

st.subheader("Completed items")
for item in my_deletes:
    st.write(item)
