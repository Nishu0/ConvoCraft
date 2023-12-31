import time
import os
import re
from typing import Dict, Union

import streamlit as st
from hydralit import HydraHeadApp
from streamlit.delta_generator import DeltaGenerator
import streamlit.components.v1 as components

from auth.auth_connection import AuthSingleton


class SignUpApp(HydraHeadApp):
    """
    This is an example signup application to be used to secure access
    within a HydraApp streamlit application.

    This application is an example of allowing an application to run
    from the login without requiring authentication.

    """

    def __init__(self, title="", **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self) -> None:
        """
        Application entry point.

        """

        st.markdown(
            "<h1 style='text-align: center;'>Signup to ConvoCraft</h1>",
            unsafe_allow_html=True,
        )

        pretty_btn = """
        <style>
        div[class="row-widget stButton"] > button {
            width: 100%;
        }
        </style>
        <br><br>
        """
        _, c2, _ = st.columns([2, 2, 2])
        # c2.markdown(pretty_btn,unsafe_allow_html=True)

        if "MSG" in os.environ.keys():
            st.info(os.environ["MSG"])

        form_data, message_placeholder = self._create_signup_form(c2)

        pretty_btn = """
        <style>
        div[class="row-widget stButton"] > button {
            width: 100%;
        }
        </style>
        <br><br>
        """
        c2.markdown(pretty_btn, unsafe_allow_html=True)

        if form_data["submitted"]:
            self._do_signup(form_data, message_placeholder)

    def _create_signup_form(self, parent_container) -> Union[Dict, DeltaGenerator]:
        signup_form = parent_container.form(key="login_form")

        signup_message = parent_container.empty()

        form_state = {}
        form_state["username"] = signup_form.text_input("Username")
        form_state["password"] = signup_form.text_input("Password", type="password")
        form_state["password2"] = signup_form.text_input(
            "Confirm Password", type="password"
        )
        form_state["email"] = signup_form.text_input("email")
        form_state["submitted"] = signup_form.form_submit_button("Sign Up")

        # Add the javascript to submit the form on enter
        components.html(
            """
        <script>
        const doc = window.parent.document;
        buttons = Array.from(doc.querySelectorAll('button[kind=secondaryFormSubmit]'));
        const submit = buttons.find(el => el.innerText === 'Login');

        doc.addEventListener('keydown', function(e) {
            switch (e.keyCode) {
                case 13: // (37 = enter)
                    submit.click();
            }
        });
        </script>
        """,
            height=0,
            width=0,
        )

        if parent_container.button("Login", key="loginbtn"):
            self.set_access(0, None)
            self.do_redirect()

        return form_state, signup_message

    def _do_signup(self, form_data, msg_container):
        # Check if all fields are filled
        for key, value in form_data.items():
            if key != "submitted" and value == "":
                msg_container.error("Please fill in all fields")
                return

        if AuthSingleton().get_instance().is_mail_exists(form_data["username"]):
            msg_container.error("Email is already taken.")

        if form_data["submitted"] and (form_data["password"] != form_data["password2"]):
            msg_container.error("Passwords do not match, please try again.")

        elif form_data["submitted"] and not self._email_is_valid(form_data["email"]):
            msg_container.error("Email format is invalid, please try again.")

        # Check if the user already exists
        elif (
            AuthSingleton()
            .get_instance()
            .check_user(form_data["username"], form_data["password"])
        ):
            msg_container.error("User already exists, please login instead.")
        else:
            with msg_container:
                with st.spinner("now redirecting to login...."):
                    self._save_signup(form_data)
                    time.sleep(2)
                    self.set_access(0, None)
                    self.do_redirect()

    @staticmethod
    def _email_is_valid(email):
        regex = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )
        return re.search(regex, email)

    def _save_signup(self, signup_data) -> int:
        # get the user details from the form and save somehwere

        # this is the data submitted
        AuthSingleton().get_instance().add_user(
            signup_data["username"], signup_data["password"], signup_data["email"]
        )

        if (
            AuthSingleton()
            .get_instance()
            .check_user(signup_data["username"], signup_data["password"])
        ):
            return (
                AuthSingleton()
                .get_instance()
                .get_user_id(signup_data["username"], signup_data["password"])
            )
        return None
