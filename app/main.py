"""Main module for the streamlit template app"""
import streamlit as st
import pandas as pd


@st.cache(allow_output_mutation=True)
def persistdata():
    defs = {
        "Dragos": "V",
        "Kat": "T",
        "Mukund": "V",
        "Viral": "M"
    }
    return defs


def main():
    """Main function of the App"""
    signups = persistdata()
    st.title("Ski 2023")
    # with st.form("signups"):
    #     fn = st.text_input("First name", value='Rando')
    #     li = st.text_input("Last initial", value='X')
    #     stoked = st.checkbox("Are you stoked?")
   
    #     submitted = st.form_submit_button("Submit")

    #     if submitted:
    #         if not stoked:
    #             st.error("ARE YOU STOKED?")
    #         if fn not in signups.keys():
    #             signups[fn] = li

    #     st.snow()
        
    spots_remaining = 22 - len(signups)
    st.write(f"Spots remaining: {spots_remaining}")

    st.write("Current signups")
    df = pd.Series(signups).to_frame().reset_index()
    df.columns = ['First Name', 'Last Initial']
    st.write(df)
    st.subheader("Sign me up")
    stoked = st.checkbox("Are you stoked?", value=False)
    if stoked:
        st.snow()

if __name__ == "__main__":
    main()
