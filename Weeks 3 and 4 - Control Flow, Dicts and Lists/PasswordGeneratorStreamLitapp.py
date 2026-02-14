import streamlit as st

st.title("🔐 Password Generator")

allowed_chars = "!@#$%^&*"

city = st.text_input("Which city did you grow up in?")
animal = st.text_input("What is your favorite animal?")
fav_input = st.text_input("What is your favorite number?")
special_char = st.text_input(
    "Choose ONE special character: !@#$%^&*",
    max_chars=1
)

if st.button("Generate Password"):

    valid = True
    # CITY CHECK
    if not city.strip().isalpha():
        st.error("City must contain letters only.")
        valid = False

    # ANIMAL CHECK
    if not animal.strip().isalpha():
        st.error("Animal must contain letters only.")
        valid = False

    # INTEGER CHECK (no try/except)
    fav_input = fav_input.strip()
    if not (
        fav_input.isdigit() or
        (fav_input.startswith("-") and fav_input[1:].isdigit())
    ):
        st.error("Favorite number must be a whole number.")
        valid = False

    # SPECIAL CHARACTER CHECK
    if len(special_char.strip()) != 1 or special_char not in allowed_chars:
        st.error("Invalid special character.")
        valid = False

    # IF ALL VALID → GENERATE PASSWORD
    if valid:
        city_clean = city.strip().upper()
        animal_clean = animal.strip().lower()
        fav_num = int(fav_input)
        special_clean = special_char.strip()

        user_password = (
            city_clean[:2]
            + animal_clean[-2:]
            + str(fav_num * 2)
            + special_clean * len(city_clean)
        )

        st.success("Password Generated!")
        st.code(user_password)
