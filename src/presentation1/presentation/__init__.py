import flet as ft
from src.domain.models import User
from src.interface.controllers.user_controller import UserController as uc
import src.presentation.switches as sw
from src.interface.controllers.user_session_controller import UserSessionController


def main(page: ft.Page):
    page.session["user_session"]: UserSessionController
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    sw.switch_to_login(page)


ft.app(target=main)
