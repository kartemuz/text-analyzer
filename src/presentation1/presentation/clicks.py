import asyncio

import flet as ft
import src.presentation.switches as sw
from src.interface.controllers.user_session_controller import UserSessionController
from src.domain.exceptions import *


def login_click(page: ft.Page):
    try:
        sw.switch_to_mainpage(page)
    except InvalidLoginException or InvalidPasswordException:
        sw.switch_to_login_error(page)


def register_click(page: ft.Page):
    s = "abcdefghijklmnopqrstuvwxyz0123456789"
    page.session.set('user_session', asyncio.run(
        UserSessionController(str(page.session.get('login_input').value),
                              str(page.session.get('password_input').value)).create(True)))
    for el in page.session.get("login_input"):
        if el not in s:
            sw.switch_to_register_error_login(1, page)
            return 0
    for el in page.session.get("password_input"):
        if el not in s:
            sw.switch_to_register_error_pass(2, page)
            return 0
    if len(page.session.get("password_input")) < 8:
        sw.switch_to_register_error_pass(1, page)
        return 0
    elif page.session.get("password_input") != page.session["confirm_password_input"]:
        sw.switch_to_register_error_pass(3, page)
        return 0
    try:
        page.session.set("confirm_password_input", "")
        sw.switch_to_mainpage(page)
        topics = page.session["user_session"].get_tags()
        print(topics)
    except LoginNotUniqueException:
        sw.switch_to_register_error_login(2, page)


def delete_click(tag):
    return 0


def search_click(e):
    return 0


def view_click(e):
    return 0


def exit_click(page: ft.Page):
    page.session["user_session"].delete()
    sw.switch_to_login(page)


def change_pass_click(page: ft.Page):
    if len(page.session.get("new_pass")) < 8:
        sw.switch_to_change_error_pass(1, page)
    elif page.session.get("old_pass") == page.session.get("new_pass"):
        sw.switch_to_change_error_pass(2, page)
    else:
        page.session.get("old_pass")
        page.session.get("new_pass")
        sw.switch_to_settings(page)
