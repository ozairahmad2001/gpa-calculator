import streamlit as st

st.set_page_config( page_title = "GPA Calculator", page_icon = ":computer:") 



def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0
    
    return grade



def calc(sem):
    theory_subjects = {}
    practical_labs = {}
    GPA = 0
    flag = 0  
    credits = 0
    col1, col2 = st.columns(2)  

    if sem == 1 :
        theory_subjects = { 'Applied Mathematics-I' : 4, 'Applied Physics-I' : 3, 'Manufacturing Processes' : 3, 'Electrical Tech.' : 3, 'HVPE' : 1, 'Fundamentals of Computing' : 2, 'Applied Chemistry' : 3 }
        practical_labs = { 'Applied Physics Lab-I' : 1, 'Elecrical Tech. Lab' : 1, 'Workshop' : 2, 'Engg. Graphics Lab' : 2, 'FOC Lab' : 1, 'Applied Chemistry Lab' : 1 }
        credits = 27

    elif sem == 2:
        theory_subjects = { 'Applied Mathematics-II' : 4, 'Applied Physics-II' : 3, 'Electronic Devices' : 3, 'Intro To Programming' : 3, 'Engineering Mechanics' : 3, 'Communication Skills' : 3, 'Environmental Studies' : 3 }
        practical_labs = { 'Applied Physics Lab-II' : 1, 'Programming Lab' : 1, 'Electronics Lab' : 1, 'Engineering Mechanics Lab' : 1, 'EVS Lab' : 1 }
        credits = 27

    elif sem == 3:
        theory_subjects = { 'Applied Mathematics-III' : 4, 'Analog Electronics-I' : 4, 'Switching Theory & Logic Design' : 4, 'EIM' : 4, 'Data Structures' : 4, 'Signal and Systems' : 4 }
        practical_labs = { 'AE Lab' : 1, 'STLD Lab' : 1, 'EIM Lab' : 1, 'DS Lab' : 1, 'SnS Lab' : 1 }
        credits = 29

    elif sem == 4:
        theory_subjects = { 'Applied Mathematics-IV' : 4, 'Analog Electronics-II' : 4, 'Network Analysis and Synthesis' : 4, 'Communication System' : 4, 'EMFT' : 3, 'COA' : 3 }
        practical_labs = { 'Applied Mathematics Lab' : 1, 'NAS Lab' : 1, 'CS Lab' : 1, 'AE-II Lab' : 1, 'COA Lab' : 1 }
        credits = 27

    elif sem == 5:
        theory_subjects = { 'Communication Skills for Professionals' : 1, 'Digital Communication' : 4, 'Microprocessors and Microcontrollers' : 4, 'Control Systems' : 4, 'Digital System Design' : 4, 'Industrial Managment' : 3 }
        practical_labs = { 'CSP Lab' : 1, 'DSD Lab' : 1, 'CS Lab' : 1, 'MnM Lab' : 1, 'DC Lab' : 1, 'Industrial Training Workshop' : 1 }
        credits = 26

    elif sem == 6:
        theory_subjects = { 'Microwave Engg.' : 4, 'Information Theory and Coding' : 4, 'Digital Signal Processing' : 4, 'VLSI Design' : 4, 'Data Communication and Network' : 4, 'Antenna and Wave Propagation' : 4 }
        practical_labs = { 'ME Lab' : 1, 'VLSI Design Lab' : 1, 'DSP Lab' : 1, 'DCN Lab' : 1, 'Industrial House Training' : 1 }
        credits = 29

    elif sem == 7:
        theory_subjects = { 'Embedded Systems' : 4, 'Optoelectronics and Optical Communication' : 4, 'Wireless Communication' : 4, 'DBMS' : 3, 'Grid Computing' : 3 }
        practical_labs = { 'OnWC Lab' : 1, 'Embeddes System Lab' : 1, 'DBMS Lab' : 1, 'Seminar' : 1, 'Minor Project' : 3, 'Industrial Training' : 1 }
        credits = 26
  
    elif sem == 8:
        theory_subjects = { 'HVPE-II' : 1, 'Satellite Communication' : 4, 'AD HOC and Sensors Network' : 3, 'Introduction to NanoTech.' : 3, 'Computer Graphics and Multimedia' : 3 }
        practical_labs = { 'SnA Lab' : 1, 'INTC Lab' : 1, 'Major Project' : 8 }
        credits = 24

    with col1:
        with st.expander("Theory Subjects"):    
            for subject in theory_subjects:
                marks = st.number_input("{}:".format( subject ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * theory_subjects[subject]

    with col2:
        with st.expander("Practical Labs"):
            for lab in practical_labs:
                marks = st.number_input("{}:".format( lab ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * practical_labs[lab]

    if flag:
        st.warning("You haven't entered the marks of all subjects!")

    GPA = GPA / credits
    return GPA

    
title1='<h1 style="font-family:garamond;color:red; text-align: center;">GPA Calculator</h1>'
title2='<h3 style="font-family:bookman;color:white; text-align: center;">Semester GPA Calculator of B.Tech(ECE)</h3>'
st.markdown(title1, unsafe_allow_html=True)
st.markdown(title2, unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hey there! {}!".format(name))
        sem = st.selectbox("Select Semester", [1, 2, 3, 4, 5, 6, 7, 8])

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Pleade Enter your Marks</h3>", unsafe_allow_html=True)

            GPA = calc(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9) 
            with cl5:
                ans = st.button("Submit")
                
            
            
    
            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()
                    st.snow()
                    st.balloons()
