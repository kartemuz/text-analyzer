# модуль графического интерфейса
import flet as ft


def main(page: ft.Page):
    page.title = "Вход в систему"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    login_input = ft.TextField(label="Логин", width=300)
    password_input = ft.TextField(label="Пароль", password=True, width=300)
    register_link = ft.TextButton("Зарегистрироваться")

    # Create the styled login button with larger text
    login_button = ft.ElevatedButton(
        content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )

    page.add(
        ft.Column(
            [
                ft.Text("Вход в систему", size=24, weight=ft.FontWeight.BOLD),
                login_input,
                password_input,
                register_link,
                login_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


ft.app(target=main)
