import streamlit as st

pages = {
    "Menu" : [
        st.Page("../navigations/up_and_down.py",
                title = "🎮 Up & down Game")
    ]
}
page = st.navigation(pages)
page.run()