import streamlit as st

pages = {
    "Menu" : [
        st.Page("../navigations/up_and_down.py",
                title = "🎮 Up & down Game"),
        st.Page("../navigations/lotto.py",
                title = "🎈 로또 번호 생성"),
    ]
}
page = st.navigation(pages)
page.run()