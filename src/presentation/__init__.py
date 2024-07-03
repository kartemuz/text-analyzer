import flet as ft
from src.domain.models import User
from src.interface.controllers.user_controller import UserController as uc
from src.interface.controllers.user_session_controller import UserSessionController
from src.domain.exceptions import *
login_input = ""
password_input = ""
confirm_password_input = ""
old_pass = ""
new_pass = ""
c_session = UserSessionController(login_input, password_input).create(True)


def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def login_click():
        global c_session
        try:
            c_session = UserSessionController(login_input, password_input).create(False)
            switch_to_mainpage()
        except InvalidLoginException or InvalidPasswordException:
            switch_to_login_error()

    # Define the Login View
    def login_view():
        global login_input, password_input
        login_input = ft.TextField(label="Логин", width=300)
        password_input = ft.TextField(label="Пароль", password=True, width=300)
        register_link = ft.TextButton("Зарегистрироваться", on_click=lambda _: switch_to_register())
        login_button = ft.ElevatedButton(
            content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            on_click=lambda _: login_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(10, 10, 10, 10),
            ),
        )
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Вход в систему", size=24, weight=ft.FontWeight.BOLD),
                    login_input,
                    password_input,
                    register_link,
                    login_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            alignment=ft.alignment.center,
            expand=True,
        )

    def login_view_error():
        global login_input, password_input
        login_input = ft.TextField(label="Логин", width=300, border_color="red")
        password_input = ft.TextField(label="Пароль", password=True, width=300, border_color="red")
        error_text = ft.Text("Неверный логин или пароль", size=18, weight=ft.FontWeight.NORMAL, color="red")
        register_link = ft.TextButton("Зарегистрироваться", on_click=lambda _: switch_to_register())
        login_button = ft.ElevatedButton(
            content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            on_click=lambda _: login_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(10, 10, 10, 10),
            ),
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Вход в систему", size=24, weight=ft.FontWeight.BOLD),
                    login_input,
                    password_input,
                    error_text,
                    register_link,
                    login_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )

    def register_click(e):
        global confirm_password_input, c_session
        s = "abcdefghijklmnopqrstuvwxyz0123456789"
        for el in login_input:
            if el not in s:
                switch_to_register_error_login(1)
                return 0
        for el in password_input:
            if el not in s:
                switch_to_register_error_pass(2)
                return 0
        if len(password_input) < 8:
            switch_to_register_error_pass(1)
            return 0
        elif password_input != confirm_password_input:
            switch_to_register_error_pass(3)
            return 0
        try:
            c_session = UserSessionController(login_input, password_input).create(True)
            confirm_password_input = ""
            switch_to_mainpage()
        except LoginNotUniqueException:
            switch_to_register_error_login(2)

    # Define the Register View
    def register_view():
        global login_input, password_input, confirm_password_input
        username_input = ft.TextField(label="Логин", width=300)
        password_input = ft.TextField(label="Пароль", password=True, width=300)
        confirm_password_input = ft.TextField(label="Повторите пароль", password=True, width=300)
        register_button = ft.ElevatedButton(
            content=ft.Text("Зарегистрироваться", size=16, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            on_click=lambda _: register_click,
            style=ft.ButtonStyle(
                padding=ft.Padding(10, 10, 10, 10),
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Регистрация", size=24, weight=ft.FontWeight.BOLD),
                    username_input,
                    password_input,
                    confirm_password_input,
                    register_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )

    def register_view_error_login(type):
        global login_input, password_input, confirm_password_input
        if type == 1:
            error_text = ft.Text("Логин может содержать только строчные\nбуквы латинского алфавита и цифры.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.alignment.center)
        else:
            error_text = ft.Text("Пользователь с таким логином\nуже зарегистрирован.",
                                 size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.alignment.center)
        username_input = ft.TextField(label="Логин", width=300, border_color="red")
        password_input = ft.TextField(label="Пароль", password=True, width=300)
        confirm_password_input = ft.TextField(label="Повторите пароль", password=True, width=300)
        register_button = ft.ElevatedButton(
            content=ft.Text("Зарегистрироваться", size=16, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            style=ft.ButtonStyle(
                padding=ft.Padding(10, 10, 10, 10),
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Регистрация", size=24, weight=ft.FontWeight.BOLD),
                    error_text,
                    username_input,
                    password_input,
                    confirm_password_input,
                    register_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )

    def register_view_error_pass(type):
        global login_input, password_input, confirm_password_input
        if type == 1:
            error_text = ft.Text("Пароль должен содержать не менее 8 символов.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
        elif type == 2:
            error_text = ft.Text("Пароль может содержать только\nбуквы латинского алфавита и цифры.",
                                 size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
        else:
            error_text = ft.Text("Введённые значения не совпадают.",
                                 size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
        username_input = ft.TextField(label="Логин", width=300)
        password_input = ft.TextField(label="Пароль", password=True, width=300, border_color="red")
        confirm_password_input = ft.TextField(label="Повторите пароль", password=True, width=300, border_color="red")
        register_button = ft.ElevatedButton(
            content=ft.Text("Зарегистрироваться", size=16, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            on_click=lambda _: register_click,
            style=ft.ButtonStyle(
                padding=ft.Padding(10, 10, 10, 10),
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
        )
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Регистрация", size=24, weight=ft.FontWeight.BOLD),
                    username_input,
                    password_input,
                    confirm_password_input,
                    error_text,
                    register_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )

    def mainpage_view():
        settings = ft.TextButton(content=ft.Text("Настройки", size=20, color=ft.colors.BLUE_ACCENT_700), on_click=lambda _: switch_to_settings())
        themes = ft.TextButton(content=ft.Text("Мои темы", size=20, color=ft.colors.BLUE_ACCENT_700), on_click=lambda _: switch_to_mythemes())

        profile = ft.Text(login_input, size=22)
        a = ft.Row(
            [
                ft.Icon(name=ft.icons.SUPERVISED_USER_CIRCLE, color=ft.colors.BLUE_ACCENT_700, size=30),
                profile,
                settings,
                themes,
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=5,
        )
        feed_button = ft.ElevatedButton(
            width=200,
            height=50,
            content=ft.Text("Лента", size=24, color=ft.colors.WHITE),
            bgcolor=ft.colors.ON_PRIMARY_CONTAINER,
            on_click=lambda _: switch_to_feed(),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
        )
        newtheme_button = ft.ElevatedButton(
            width=200,
            height=50,
            content=ft.Text("Новая тема", size=24, color=ft.colors.BLUE_ACCENT_700),
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            on_click=lambda _: switch_to_search(),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
        )
        return ft.Container(content=ft.Column([a, ft.Row(
                [
                    feed_button,
                    newtheme_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            )],
            alignment=ft.alignment.center,
            expand=True,
        ), )

    def delete_click(tag):
        return 0

    def mythemes_view():
        global c_session
        topics = c_session.
        b = ft.TextButton(content=ft.Row(
                [
                    ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
                    ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            width=200,
            on_click=lambda _: switch_to_mainpage(),
        )

        topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
        for topic in topics:
            topic_row = ft.Row(
                controls=[
                    ft.Text(topic["name"], size=18),
                    ft.ElevatedButton(content=ft.Text("Удалить", size=18, color=ft.colors.WHITE), bgcolor=ft.colors.BLUE_ACCENT_700, on_click=lambda _: delete_click(topic["name"]))
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.alignment.top_center,
            )
            topics_list.controls.append(topic_row)
        return ft.Container(content=ft.Column([b, ft.Text("Мои темы", size=24,  weight=ft.FontWeight.BOLD), topics_list,]), alignment=ft.alignment.top_left, expand=True,)

    def exit_click(e):
        global login_input, password_input
        login_input = ""
        password_input = ""
        del c_session
        switch_to_login()

    def change_pass_click(e):
        global old_pass, new_pass, c_session
        if len(new_pass) < 8:
            switch_to_change_error_pass(1)
        elif old_pass == new_pass:
            switch_to_change_error_pass(2)
        else:
            old_pass = ""
            new_pass = ""
            c_session = UserSessionController(login_input, new_pass).create(False)
            switch_to_settings()

    def settings_view():
        global old_pass, new_pass
        old_pass = ft.TextField(label="Старый пароль", width=300)
        new_pass = ft.TextField(label="Новый пароль", password=True, width=300)
        exit_button = ft.ElevatedButton(
            content=ft.Text("Выйти из профиля", size=20, color=ft.colors.RED),
            bgcolor=ft.colors.DEEP_ORANGE_100,
            color=ft.colors.WHITE,
            on_click=lambda _: exit_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(10, 10, 10, 10),
            ),
        )
        b = ft.TextButton(content=ft.Row(
            [
                ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
                ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
            width=200,
            on_click=lambda _: switch_to_mainpage(),
        )
        save_button = ft.ElevatedButton(
            content=ft.Text("Сохранить", size=20, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            on_click=lambda _: change_pass_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(10, 10, 10, 10),
            ),
        )
        return ft.Container(
            content=ft.Column(
                [
                    b,
                    ft.Text("Изменить пароль", size=24, weight=ft.FontWeight.BOLD),
                    old_pass,
                    new_pass,
                    save_button,
                    ft.Text(" "),
                    exit_button,
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=20
            ),
            alignment=ft.alignment.top_left,
            expand=True,
        )

    def change_password_error(type):
        global old_pass, new_pass
        if type == 1:
            error_text = ft.Text("Пароль должен содержать не менее 8 символов.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
        elif type == 2:
            error_text = ft.Text("Введённые значения не должны совпадать.",
                                 size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
        else:
            error_text = ft.Text("Неверный пароль.",
                                 size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
        old_pass = ft.TextField(label="Старый пароль", width=300, border_color="red")
        new_pass = ft.TextField(label="Новый пароль", password=True, width=300, border_color="red")
        exit_button = ft.ElevatedButton(
            content=ft.Text("Выйти из профиля", size=20, color=ft.colors.RED),
            bgcolor=ft.colors.DEEP_ORANGE_100,
            color=ft.colors.WHITE,
            on_click=lambda _: exit_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(10, 10, 10, 10),
            ),
        )
        b = ft.TextButton(content=ft.Row(
            [
                ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
                ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
            width=200,
            on_click=lambda _: switch_to_mainpage(),
        )
        save_button = ft.ElevatedButton(
            content=ft.Text("Сохранить", size=20, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            on_click=lambda _: change_pass_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(10, 10, 10, 10),
            ),
        )
        return ft.Container(
            content=ft.Column(
                [
                    b,
                    ft.Text("Изменить пароль", size=24, weight=ft.FontWeight.BOLD),
                    error_text,
                    old_pass,
                    new_pass,
                    save_button,
                    ft.Text(" "),
                    exit_button,
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=20
            ),
            alignment=ft.alignment.top_left,
            expand=True,
        )

    def view_click(e):
        return 0

    def feed_view():
        topics = [
            {"name": "Котики признаны жидкостью!", "media": "rbk.ru", "date": "17.02.2024"},
            {"name": "Инвестиции в симелеоны приводят к банкротству.", "media": "Mash", "date": "22.02.2024"}
        ]
        b = ft.TextButton(content=ft.Row(
            [
                ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
                ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
            width=200,
            on_click=lambda _: switch_to_mainpage(),
        )
        topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
        for topic in topics:
            topic_row = ft.Row(
                controls=[
                    ft.Text(topic["name"], size=18),
                    ft.Row(controls=[ft.Text(topic["media"], size=18, color=ft.colors.TERTIARY,  weight=ft.FontWeight.BOLD),ft.Text(topic["date"], size=18, color=ft.colors.SECONDARY),
                                     ft.ElevatedButton(content=ft.Text("Смотреть", size=18, color=ft.colors.BLUE_ACCENT_700), on_click=lambda _:view_click,
                                                    bgcolor=ft.colors.WHITE,)], alignment=ft.MainAxisAlignment.END, ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.alignment.top_center,
            )
            topics_list.controls.append(topic_row)
        return ft.Container(
            content=ft.Column(
                [
                    b,
                    ft.Text("Лента новостей", size=26, weight=ft.FontWeight.BOLD),
                    topics_list,
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=20
            ),
            alignment=ft.alignment.top_left,
            expand=True,
        )

    def search_click(e):
        return 0

    def search_view():
        search_field = ft.TextField(label="Введите текст", text_size=20, width=1100, height=45, border_color="blue")
        b = ft.TextButton(content=ft.Row(
            [
                ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
                ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
            width=200,
            on_click=lambda _: switch_to_mainpage(),
        )
        search_button = ft.ElevatedButton(
            content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            on_click=lambda _: search_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(35, 15, 35, 15),
            ),
        )
        return ft.Container(
            content=ft.Column(
                [
                    b,
                    ft.Text("Новая тема", size=26, weight=ft.FontWeight.BOLD),
                    ft.Row(controls=[search_field, search_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, )
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=20
            ),
            alignment=ft.alignment.top_left,
            expand=True,
        )

    def search_show_view():
        topics = [
            {"name": "Котики признаны жидкостью!", "media": "rbk.ru", "date": "17.02.2024"},
            {"name": "Инвестиции в симелеоны приводят к банкротству.", "media": "Mash", "date": "22.02.2024"}
        ]
        topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
        for topic in topics:
            topic_row = ft.Row(
                controls=[
                    ft.Text(topic["name"], size=18),
                    ft.Row(
                        controls=[ft.Text(topic["media"], size=18, color=ft.colors.TERTIARY, weight=ft.FontWeight.BOLD),
                                  ft.Text(topic["date"], size=18, color=ft.colors.SECONDARY),
                                  ft.ElevatedButton(content=ft.Text("Смотреть", size=18, color=ft.colors.BLUE_ACCENT_700),
                                                    bgcolor=ft.colors.WHITE, on_click=None, )],
                        alignment=ft.MainAxisAlignment.END, ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.alignment.top_center,
            )
            topics_list.controls.append(topic_row)
        search_field = ft.TextField(label="Введите текст", text_size=20, width=1100, height=45, border_color="blue")
        b = ft.TextButton(content=ft.Row(
            [
                ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
                ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
            width=200,
            on_click=lambda _: switch_to_mainpage(),
        )
        search_button = ft.ElevatedButton(
            content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            on_click=lambda _: search_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(35, 15, 35, 15),
            ),
        )
        return ft.Container(
            content=ft.Column(
                [
                    b,
                    ft.Text("Новая тема", size=26, weight=ft.FontWeight.BOLD),
                    ft.Row(controls=[search_field, search_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, ),
                    topics_list
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=20
            ),
            alignment=ft.alignment.top_left,
            expand=True,
        )

    def search_show_error():
        search_field = ft.TextField(label="Введите текст", text_size=20, width=1100, height=45, border_color="blue")
        b = ft.TextButton(content=ft.Row(
            [
                ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
                ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
            width=200,
            on_click=lambda _: switch_to_mainpage(),
        )
        search_button = ft.ElevatedButton(
            content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            on_click=lambda _: search_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.Padding(35, 15, 35, 15),
            ),
        )
        return ft.Container(
            content=ft.Column(
                [
                    b,
                    ft.Text("Новая тема", size=26, weight=ft.FontWeight.BOLD),
                    ft.Row(controls=[search_field, search_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, ),
                    ft.Text("По запросу ничего не найдено.", size=20, weight=ft.FontWeight.NORMAL, color=ft.colors.SECONDARY),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=20
            ),
            alignment=ft.alignment.top_left,
            expand=True,
        )
    def switch_to_register():
        page.controls.clear()
        page.add(register_view())
        page.update()

    def switch_to_register_error_login(type):
        page.controls.clear()
        page.add(register_view_error_login(type))
        page.update()

    def switch_to_register_error_pass(type):
        page.controls.clear()
        page.add(register_view_error_pass(type))
        page.update()

    # Function to switch to the Login View
    def switch_to_login():
        page.controls.clear()
        page.add(login_view())
        page.update()

    def switch_to_login_error():
        page.controls.clear()
        page.add(login_view_error())
        page.update()

    def switch_to_mainpage():
        page.controls.clear()
        page.add(mainpage_view())
        page.update()

    def switch_to_mythemes():
        page.controls.clear()
        page.add(mythemes_view())
        page.update()

    def switch_to_settings():
        page.controls.clear()
        page.add(settings_view())
        page.update()

    def switch_to_change_error_pass(type):
        page.controls.clear()
        page.add(change_password_error(type))
        page.update()

    def switch_to_feed():
        page.controls.clear()
        page.add(feed_view())
        page.update()

    def switch_to_search():
        page.controls.clear()
        page.add(search_view())
        page.update()

    def switch_to_search_show():
        page.controls.clear()
        page.add(search_show_view())
        page.update()

    def switch_to_search_error():
        page.controls.clear()
        page.add(search_show_error())
        page.update()

    switch_to_search_error()


ft.app(target=main)
