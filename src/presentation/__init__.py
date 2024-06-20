# модуль графического интерфейса
import flet as ft
from flet_core import margin




def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Define the Login View
    def login_view():
        login_input = ft.TextField(label="Логин", width=300)
        password_input = ft.TextField(label="Пароль", password=True, width=300)
        register_link = ft.TextButton("Зарегистрироваться", on_click=lambda _: switch_to_register())
        login_button = ft.ElevatedButton(
            content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
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
        login_input = ft.TextField(label="Логин", width=300, border_color="red")
        password_input = ft.TextField(label="Пароль", password=True, width=300, border_color="red")
        error_text = ft.Text("Неверный логин или пароль", size=18, weight=ft.FontWeight.NORMAL, color="red")
        register_link = ft.TextButton("Зарегистрироваться", on_click=lambda _: switch_to_register())
        login_button = ft.ElevatedButton(
            content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
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

    # Define the Register View
    def register_view():
        username_input = ft.TextField(label="Логин", width=300)
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

    def register_view_error_login():
        error_text = ft.Text("Логин может содержать только строчные\nбуквы латинского алфавита и цифры.",
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
        settings = ft.TextButton(content=ft.Text("Настройки", size=20, color=ft.colors.BLUE_ACCENT_700), on_click=None)
        themes = ft.TextButton(content=ft.Text("Мои темы", size=20, color=ft.colors.BLUE_ACCENT_700), on_click=lambda _:switch_to_mythemes())

        profile = ft.Text("dd", size=22)
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
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
        )
        newtheme_button = ft.ElevatedButton(
            width=200,
            height=50,
            content=ft.Text("Новая тема", size=24, color=ft.colors.BLUE_ACCENT_700),
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
        )
        page.add(a)
        page.update()
        return ft.Container(
            content=ft.Row(
                [
                    feed_button,
                    newtheme_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )

    def mythemes_view():
        topics = [
            {"name": "Котики", "date": "17.02.2024"},
            {"name": "Инвестиции", "date": "22.02.2024"}
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
        page.add(b)
        page.update()
        topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
        for topic in topics:
            topic_row = ft.Row(
                controls=[
                    ft.Text(topic["name"], size=18),
                    ft.ElevatedButton(content=ft.Text("Удалить", size=18, color=ft.colors.WHITE), bgcolor=ft.colors.BLUE_ACCENT_700, on_click=None, )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.alignment.top_center,
            )
            topics_list.controls.append(topic_row)
        return topics_list
    
    def settings_view():
        return None

    def switch_to_register():
        page.controls.clear()
        page.add(register_view())
        page.update()

    def switch_to_register_error_login():
        page.controls.clear()
        page.add(register_view_error_login())
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
        
        
    switch_to_mainpage()


username = "aboba"
ft.app(target=main)
