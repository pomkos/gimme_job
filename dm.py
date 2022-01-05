import streamlit as st

st.title("LinkedIn DM Template")

recruiter = st.text_input("Recruiter Name")
company = st.text_input("Company")

col1, col2 = st.columns(2)
with col1:
    role = st.text_input("Role", value="Data Science")
with col2:
    position = st.text_input("Position")

name = st.text_input("Your Name", value="Peter Gates")

if not position:
        st.info("Fill in the above variables to continue")
        st.stop()
if not company:
        st.info("Fill in the above variables to continue")
        st.stop()
if not recruiter:
        st.info("Fill in the above variables to continue")
        st.stop()

message = f"""Hello {recruiter}!
 
My name is {name}, I'm a recent PHD graduate and am looking for a {role} role. I recently applied to the {position} position at {company}. Is there anyone I can speak with to find out more about {company} and {role}?
 
Thanks,
{name}
"""

st.write('----------------------')
st.write(message)
st.write('----------------------')