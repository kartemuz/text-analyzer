import flet as ft
import src.presentation.switches as sw
from src.interface.controllers.user_session_controller import UserSessionController
from src.domain.exceptions import *
import asyncio


def login_click(page: ft.Page):
    try:
        page.session.set('user_session', asyncio.run(
            UserSessionController(page.session.get("login_input").value,
                                  page.session.get("password_input").value).create()))
        sw.switch_to_mainpage(page)
    except InvalidLoginException or InvalidPasswordException:
        sw.switch_to_login_error(page)


def register_click(page: ft.Page):
    s = "abcdefghijklmnopqrstuvwxyz0123456789"
    for el in page.session.get("password_input").value:
        if el not in s:
            sw.switch_to_register_error_pass(2, page)
            return 0
    if len(page.session.get("password_input").value) < 8:
        sw.switch_to_register_error_pass(1, page)
        return 0
    elif page.session.get("password_input").value != page.session.get("confirm_password_input").value:
        sw.switch_to_register_error_pass(3, page)
        return 0
    try:
        page.session.set('user_session', asyncio.run(
            UserSessionController(page.session.get("password_input").value,
                                  page.session.get("password_input").value).create(True)))
        sw.switch_to_mainpage(page)
    except LoginNotUniqueException:
        sw.switch_to_register_error_login(2, page)


async def delete_click(tag, page: ft.Page):
    asyncio.run(page.session.get("user_session").delete_tag(tag))
    sw.switch_to_mythemes(page)


def view_click(url):
    return 0


def search_click(tag, page: ft.Page):
    if len(asyncio.run(page.session.get("user_session").search_by_tag(tag))) == 0:
        sw.switch_to_search_error(page)
    else:
        asyncio.run(page.session.get("user_session").add_tag(tag))
        sw.switch_to_search_show(page, tag)


def exit_click(page: ft.Page):
    asyncio.run(page.session.get("user_session").delete())
    sw.switch_to_login(page)


def change_pass_click(page: ft.Page):
    if len(page.session.get("new_pass").value) < 8:
        sw.switch_to_change_error_pass(1, page)
    elif page.session.get("old_pass").value == page.session.get("new_pass").value:
        sw.switch_to_change_error_pass(2, page)
    else:
        asyncio.run(page.session.get("user_session").change_password(page.session.get("new_pass").value))
        sw.switch_to_settings(page)
