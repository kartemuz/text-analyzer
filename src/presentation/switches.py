import flet as ft
import src.presentation.views as vw


def switch_to_register(page: ft.Page):
    page.controls.clear()
    page.add(vw.register_view(page))
    page.update()


def switch_to_register_error_login(type, page: ft.Page):
    page.controls.clear()
    page.add(vw.register_view_error_login(type, page))
    page.update()


def switch_to_register_error_pass(type, page: ft.Page):
    page.controls.clear()
    page.add(vw.register_view_error_pass(type, page))
    page.update()


def switch_to_login(page: ft.Page):
    page.controls.clear()
    page.add(vw.login_view(page))
    page.update()


def switch_to_login_error(page: ft.Page):
    page.controls.clear()
    page.add(vw.login_view_error(page))
    page.update()


def switch_to_mainpage(page: ft.Page):
    page.controls.clear()
    page.add(vw.mainpage_view(page))
    page.update()


def switch_to_mythemes(page: ft.Page):
    page.controls.clear()
    page.add(vw.mythemes_view(page))
    page.update()


def switch_to_settings(page: ft.Page):
    page.controls.clear()
    page.add(vw.settings_view(page))
    page.update()


def switch_to_change_error_pass(type_err, page: ft.Page):
    page.controls.clear()
    page.add(vw.change_password_error(type_err, page))
    page.update()


def switch_to_feed(page: ft.Page):
    page.controls.clear()
    page.add(vw.feed_view(page))
    page.update()


def switch_to_search(page: ft.Page):
    page.controls.clear()
    page.add(vw.search_view(page))
    page.update()


def switch_to_search_show(page: ft.Page):
    page.controls.clear()
    page.add(vw.search_show_view(page))
    page.update()


def switch_to_search_error(page: ft.Page):
    page.controls.clear()
    page.add(vw.search_show_error(page))
    page.update()
