# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st


fav_icon = "backend/assets/brand/reflex_logo.jpeg"
st.set_page_config(layout="wide", page_title="Reflex")

st.html("""
  <style>
    [alt=Logo] {
      height: 2rem;
    }
  </style>
        """)

sidear_logo = "backend/assets/brand/reflex_logo.jpeg"
main_body_logo = "backend/assets/brand/reflex_logo.jpeg"

st.logo(sidear_logo, icon_image=main_body_logo, size="large")



home_page = st.Page("pages/home.py", title = "Home", default=True)
dashboard_page = st.Page("pages/dashboard.py", title = "User Constrains")
# QA = st.Page("pages/chat.py", title = "Q&A", icon =":material/question_answer:")
# math_solver = st.Page("pages/math_solver.py", title = "Math Solver", icon =":material/function:")
# feedback_page = st.Page("pages/feedbacks.py", title = "Feedback", icon =":material/feedback:")
# documentation_page = st.Page("pages/documentation.py", title = "Documentation", icon =":material/book:")
# test_page = st.Page("pages/test.py", title = "Test", icon =":material/assessment:")
# about_page = st.Page("pages/about.py", title = "About", icon =":material/info:")
pg = st.navigation({
    # "Main Menu":[ home_page, dashboard_page,QA, math_solver, feedback_page, about_page, documentation_page]
    "Main Menu":[ home_page, dashboard_page]

})


pg.run()