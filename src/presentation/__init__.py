# модуль графического интерфейса
import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Define the Login View
    def login_view():
        login_input = ft.TextField(label="Логин", width=300)
        password_input = ft.TextField(label="Пароль", password=True, width=300)
        register_link = ft.TextButton("Зарегистрироваться", on_click=lambda _: switch_to_register_view())
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
        register_link = ft.TextButton("Зарегистрироваться", on_click=lambda _: switch_to_register_view())
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
                             size=18, weight=ft.FontWeight.NORMAL, color="red")
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
                             size=18, weight=ft.FontWeight.NORMAL, color="red")
        elif type == 2:
            error_text = ft.Text("Пароль может содержать только\nбуквы латинского алфавита и цифры.",
                                 size=18, weight=ft.FontWeight.NORMAL, color="red")
        else:
            error_text = ft.Text("Введённые значения не совпадают.",
                                 size=18, weight=ft.FontWeight.NORMAL, color="red")
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
                    error_text,
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

    def mainpage_view(username):
        banner = ft.Banner(
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            content=ft.Column([
                ft.TextButton(
                    content=ft.Text("Настройки", size=20, color=ft.colors.BLUE_ACCENT_700), on_click=None),
                ft.TextButton(content=ft.Text("Мои темы", size=20, color=ft.colors.BLUE_ACCENT_700), on_click=None),
            ],
            ),
            actions=[ft.TextButton("Закрыть", icon=ft.icons.CANCEL_OUTLINED, icon_color=ft.colors.SECONDARY,
                                   on_click=lambda _: close_banner())],
            force_actions_below=True,
            open=False,
        )

        def open_banner():
            banner.open = True
            page.update()

        def close_banner():
            banner.open = False
            page.update()

        profile = ft.TextButton(username, on_click=lambda _: open_banner())
        a = ft.Row(
            [
                ft.Icon(name=ft.icons.SUPERVISED_USER_CIRCLE, color=ft.colors.BLUE_ACCENT_700),
                profile,
                banner,
            ],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=10,
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


    # Function to switch to the Register View
    def switch_to_register_view():
        page.controls.clear()
        page.add(register_view())
        page.update()

    def switch_to_register_view_error_login():
        page.controls.clear()
        page.add(register_view_error_login())
        page.update()

    def switch_to_register_view_error_pass(type):
        page.controls.clear()
        page.add(register_view_error_pass(type))
        page.update()

    # Function to switch to the Login View
    def switch_to_login_view():
        page.controls.clear()
        page.add(login_view())
        page.update()

    def switch_to_login_view_error():
        page.controls.clear()
        page.add(login_view_error())
        page.update()

    def switch_to_mainpage_view(username):
        page.controls.clear()
        page.add(mainpage_view(username))
        page.update()

    # Initialize the app with the Login View
    switch_to_login_view()


ft.app(target=main)
