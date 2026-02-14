import streamlit as st

st.title("🔐 Aparajita's Password Generator")

city = st.text_input("Which city did you grow up in?").strip().upper()
city = city.replace(" ","")
animal = st.text_input("What is your favorite animal?").strip().lower()
animal = animal.replace(" ","")
fav_num = st.text_input("What is your favorite number? Enter a positive whole number.").strip()
special_char = st.text_input("Choose ONE special character from these choices: !@#$%^&*", max_chars=1).strip() #Can;t use "select" for some reason
#fav_num = int(fav_num) Won't work here, need to put after

if st.button("Generate password"): #== True is implied
    valid = True
    if not city.isalpha():
        st.error("City must contain letters only.")
        valid = False

    if not animal.isalpha(): #same as if animal.isalpha() != True:
        st.error("Animal must contain letters only.")
        valid = False

    if not fav_num.isdigit():
        st.error("Favorite number must be a positive whole number.")
        valid = False

    allowed_chars = "!@#$%^&*"
    #if (len(special_char)!=1) and (special_char not in allowed_chars):
    if (len(special_char) != 1) or (special_char not in allowed_chars):
        st.error(f"Special character must be one of the following characters:{allowed_chars}")
        valid = False

    if valid: #== True is implied
        fav_num = int(fav_num)
        user_password = city[:2] + animal[-2:] + str(fav_num*2) + len(city)*special_char #Use string concatenation
        st.success("Your password is generated!")
        st.code(user_password)
