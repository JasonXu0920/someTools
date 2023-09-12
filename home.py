import streamlit as st
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.markdown("""
    <style>
        .css-h5rgaw.ea3mdgi1
            {
                visibility: hidden;
            }
    </style>
""", unsafe_allow_html=True)



st.write("# Welcome to My Toolkit! 👋")

st.sidebar.success("Select a tool above.")

st.markdown(
    """
    This is a website for my tools collections!  
    
    **👈 Select a tool from the sidebar !** 
    ### What do I have?
    - tool1
    - tool2
    - tool3
    ### Want more tools?
    - Email me  

        xungui.xu@gmail.com
"""
)