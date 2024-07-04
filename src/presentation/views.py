import flet as ft
import src.presentation.switches as sw
import src.presentation.clicks as cl
import asyncio


def login_view(page: ft.Page):
    page.session.set("login_input", ft.TextField(label="Логин", width=300))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300))
    login_button = ft.ElevatedButton(
        content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.login_click(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            padding=ft.Padding(10, 10, 10, 10),
        ),
    )
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Вход в систему", size=24, weight=ft.FontWeight.BOLD),
                page.session.get("login_input"),
                page.session.get("password_input"),
                ft.TextButton("Зарегистрироваться", on_click=lambda _: sw.switch_to_register(page)),
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        expand=True,
    )


def login_view_error(page: ft.Page):
    page.session.set("login_input", ft.TextField(label="Логин", width=300, border_color="red"))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300))
    error_text = ft.Text("Неверный логин или пароль", size=18, weight=ft.FontWeight.NORMAL, color="red")
    register_link = ft.TextButton("Зарегистрироваться", on_click=lambda _: sw.switch_to_register(page))
    login_button = ft.ElevatedButton(
        content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.login_click(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            padding=ft.Padding(10, 10, 10, 10),
        ),
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Вход в систему", size=24, weight=ft.FontWeight.BOLD),
                page.session.get("login_input"),
                page.session.get("password_input"),
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


def register_view(page: ft.Page):
    page.session.set("login_input", ft.TextField(label="Логин", width=300))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300))
    page.session.set("confirm_password_input", ft.TextField(label="Повторите пароль", password=True, width=300))
    register_button = ft.ElevatedButton(
        content=ft.Text("Зарегистрироваться", size=16, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        on_click=lambda _: cl.register_click(page),
        style=ft.ButtonStyle(
            padding=ft.Padding(10, 10, 10, 10),
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Регистрация", size=24, weight=ft.FontWeight.BOLD),
                page.session.get("login_input"),
                page.session.get("password_input"),
                page.session.get("confirm_password_input"),
                register_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )


def register_view_error_login(type_err, page: ft.Page):
    if type_err == 1:
        error_text = ft.Text("Логин может содержать только строчные\nбуквы латинского алфавита и цифры.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.alignment.center)
    else:
        error_text = ft.Text("Пользователь с таким логином\nуже зарегистрирован.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.alignment.center)
    page.session.set("login_input", ft.TextField(label="Логин", width=300, border_color="red"))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300))
    page.session.set("confirm_password_input", ft.TextField(label="Повторите пароль", password=True, width=300))
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
                page.session.get("login_input"),
                page.session.get("password_input"),
                page.session.get("confirm_password_input"),
                register_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )


def register_view_error_pass(type_err, page: ft.Page):
    if type_err == 1:
        error_text = ft.Text("Пароль должен содержать не менее 8 символов.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    elif type_err == 2:
        error_text = ft.Text("Пароль может содержать только\nбуквы латинского алфавита и цифры.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    else:
        error_text = ft.Text("Введённые значения не совпадают.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)

    page.session.set("login_input", ft.TextField(label="Логин", width=300))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300, border_color="red"))
    page.session.set("confirm_password_input",
                     ft.TextField(label="Повторите пароль", password=True, width=300, border_color="red"))
    register_button = ft.ElevatedButton(
        content=ft.Text("Зарегистрироваться", size=16, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        on_click=lambda _: cl.register_click,
        style=ft.ButtonStyle(
            padding=ft.Padding(10, 10, 10, 10),
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Регистрация", size=24, weight=ft.FontWeight.BOLD),
                page.session.get("login_input"),
                page.session.get("password_input"),
                page.session.get("confirm_password_input"),
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


def mainpage_view(page: ft.Page):
    settings = ft.TextButton(content=ft.Text("Настройки", size=20, color=ft.colors.BLUE_ACCENT_700),
                             on_click=lambda _: sw.switch_to_settings(page))
    themes = ft.TextButton(content=ft.Text("Мои темы", size=20, color=ft.colors.BLUE_ACCENT_700),
                           on_click=lambda _: sw.switch_to_mythemes(page))

    profile = ft.Text(page.session.get("login_input").value, size=22)
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
        on_click=lambda _: sw.switch_to_feed(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    newtheme_button = ft.ElevatedButton(
        width=200,
        height=50,
        content=ft.Text("Новая тема", size=24, color=ft.colors.BLUE_ACCENT_700),
        bgcolor=ft.colors.SECONDARY_CONTAINER,
        on_click=lambda _: sw.switch_to_search(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    return ft.Column(
        [
            a,
            ft.Row([
                feed_button,
                newtheme_button,
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            ft.Text(""),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True,
    )


def settings_view(page: ft.Page):
    page.session.set("old_pass", ft.TextField(label="Старый пароль", width=300, password=True))
    page.session.set("new_pass", ft.TextField(label="Новый пароль", password=True, width=300))
    exit_button = ft.ElevatedButton(
        content=ft.Text("Выйти из профиля", size=20, color=ft.colors.RED),
        bgcolor=ft.colors.DEEP_ORANGE_100,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.exit_click(page),
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
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    save_button = ft.ElevatedButton(
        content=ft.Text("Сохранить", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.change_pass_click(page),
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
                page.session.get("old_pass"),
                page.session.get("new_pass"),
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


def change_password_error(type_err, page: ft.Page):
    if type_err == 1:
        error_text = ft.Text("Пароль должен содержать не менее 8 символов.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    elif type_err == 2:
        error_text = ft.Text("Введённые значения не должны совпадать.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    else:
        error_text = ft.Text("Неверный пароль.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    page.session.set("old_pass", ft.TextField(label="Старый пароль", width=300, password=True, border_color="red"))
    page.session.set("new_pass", ft.TextField(label="Новый пароль", password=True, width=300, border_color="red"))
    exit_button = ft.ElevatedButton(
        content=ft.Text("Выйти из профиля", size=20, color=ft.colors.RED),
        bgcolor=ft.colors.DEEP_ORANGE_100,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.exit_click(page),
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
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    save_button = ft.ElevatedButton(
        content=ft.Text("Сохранить", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.change_pass_click(page),
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
                page.session.get("old_pass"),
                page.session.get("new_pass"),
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


def feed_view(page: ft.Page):
    topics = asyncio.run(page.session.get("user_session").search_sorted())
    b = ft.TextButton(content=ft.Row(
        [
            ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
            ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
    ),
        width=200,
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
    for topic in topics:
        topic_row = ft.Row(
            controls=[
                ft.Text(topic.title, size=18),
                ft.Row(
                    controls=[ft.Text(topic.source_name, size=18, color=ft.colors.TERTIARY, weight=ft.FontWeight.BOLD),
                              ft.Text(topic.date, size=18, color=ft.colors.SECONDARY),
                              ft.ElevatedButton(
                                  content=ft.Text("Смотреть", size=18, color=ft.colors.BLUE_ACCENT_700),
                                  bgcolor=ft.colors.WHITE, url=topic.link, )],
                    alignment=ft.MainAxisAlignment.END, ),
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


def search_view(page: ft.Page):
    search_field = ft.TextField(label="Введите текст", text_size=20, width=1100, height=45, border_color="blue")
    b = ft.TextButton(content=ft.Row(
        [
            ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
            ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
    ),
        width=200,
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    search_button = ft.ElevatedButton(
        content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.search_click(search_field.value, page),
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


def mythemes_view(page: ft.Page):
    topics = page.session.get("user_session").get_tags()
    b = ft.TextButton(content=ft.Row(
        [
            ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
            ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
    ),
        width=200,
        on_click=lambda _: sw.switch_to_mainpage(page),
    )

    topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
    for topic in topics:
        topic_row = ft.Row(
            controls=[
                ft.Text(topic, size=18),
                ft.ElevatedButton(content=ft.Text("Удалить", size=18, color=ft.colors.WHITE),
                                  bgcolor=ft.colors.BLUE_ACCENT_700,
                                  on_click=lambda _: cl.delete_click(topic, page))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.alignment.top_center,
        )
        topics_list.controls.append(topic_row)
    return ft.Container(
        content=ft.Column([b, ft.Text("Мои темы", size=24, weight=ft.FontWeight.BOLD), topics_list, ]),
        alignment=ft.alignment.top_left, expand=True, )


def search_show_view(page: ft.Page, tag):
    topics = asyncio.run(page.session.get("user_session").search_by_tag(tag))
    topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
    for topic in topics:
        topic_row = ft.Row(
            controls=[
                ft.Text(topic.title, size=18),
                ft.Row(
                    controls=[ft.Text(topic.source_name, size=18, color=ft.colors.TERTIARY, weight=ft.FontWeight.BOLD),
                              ft.Text(topic.date, size=18, color=ft.colors.SECONDARY),
                              ft.ElevatedButton(
                                  content=ft.Text("Смотреть", size=18, color=ft.colors.BLUE_ACCENT_700),
                                  bgcolor=ft.colors.WHITE, url=topic.link, )],
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
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    search_button = ft.ElevatedButton(
        content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.search_click(search_field.value, page),
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


def search_show_error(page: ft.Page):
    search_field = ft.TextField(label="Введите текст", text_size=20, width=1100, height=45, border_color="blue")
    b = ft.TextButton(content=ft.Row(
        [
            ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
            ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
    ),
        width=200,
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    search_button = ft.ElevatedButton(
        content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.search_click(search_field.value, page),
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
                ft.Text("По запросу ничего не найдено.", size=20, weight=ft.FontWeight.NORMAL,
                        color=ft.colors.SECONDARY),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20
        ),
        alignment=ft.alignment.top_left,
        expand=True,
    )
import flet as ft
import src.presentation.switches as sw
import src.presentation.clicks as cl


def login_view(page: ft.Page):
    page.session.set("login_input", ft.TextField(label="Логин", width=300))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300))
    login_button = ft.ElevatedButton(
        content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.login_click(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            padding=ft.Padding(10, 10, 10, 10),
        ),
    )
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Вход в систему", size=24, weight=ft.FontWeight.BOLD),
                page.session.get("login_input"),
                page.session.get("password_input"),
                ft.TextButton("Зарегистрироваться", on_click=lambda _: sw.switch_to_register(page)),
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        expand=True,
    )


def login_view_error(page: ft.Page):
    page.session.set("login_input", ft.TextField(label="Логин", width=300, border_color="red"))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300))
    error_text = ft.Text("Неверный логин или пароль", size=18, weight=ft.FontWeight.NORMAL, color="red")
    register_link = ft.TextButton("Зарегистрироваться", on_click=lambda _: sw.switch_to_register(page))
    login_button = ft.ElevatedButton(
        content=ft.Text("Войти", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.login_click(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            padding=ft.Padding(10, 10, 10, 10),
        ),
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Вход в систему", size=24, weight=ft.FontWeight.BOLD),
                page.session.get("login_input"),
                page.session.get("password_input"),
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


def register_view(page: ft.Page):
    page.session.set("login_input", ft.TextField(label="Логин", width=300))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300))
    page.session.set("confirm_password_input", ft.TextField(label="Повторите пароль", password=True, width=300))
    register_button = ft.ElevatedButton(
        content=ft.Text("Зарегистрироваться", size=16, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        on_click=lambda _: cl.register_click(page),
        style=ft.ButtonStyle(
            padding=ft.Padding(10, 10, 10, 10),
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Регистрация", size=24, weight=ft.FontWeight.BOLD),
                page.session.get("login_input"),
                page.session.get("password_input"),
                page.session.get("confirm_password_input"),
                register_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )


def register_view_error_login(type_err, page: ft.Page):
    if type_err == 1:
        error_text = ft.Text("Логин может содержать только строчные\nбуквы латинского алфавита и цифры.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.alignment.center)
    else:
        error_text = ft.Text("Пользователь с таким логином\nуже зарегистрирован.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.alignment.center)
    page.session.set("login_input", ft.TextField(label="Логин", width=300, border_color="red"))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300))
    page.session.set("confirm_password_input", ft.TextField(label="Повторите пароль", password=True, width=300))
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
                page.session.get("login_input"),
                page.session.get("password_input"),
                page.session.get("confirm_password_input"),
                register_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )


def register_view_error_pass(type_err, page: ft.Page):
    if type_err == 1:
        error_text = ft.Text("Пароль должен содержать не менее 8 символов.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    elif type_err == 2:
        error_text = ft.Text("Пароль может содержать только\nбуквы латинского алфавита и цифры.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    else:
        error_text = ft.Text("Введённые значения не совпадают.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)

    page.session.set("login_input", ft.TextField(label="Логин", width=300))
    page.session.set("password_input", ft.TextField(label="Пароль", password=True, width=300, border_color="red"))
    page.session.set("confirm_password_input",
                     ft.TextField(label="Повторите пароль", password=True, width=300, border_color="red"))
    register_button = ft.ElevatedButton(
        content=ft.Text("Зарегистрироваться", size=16, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        on_click=lambda _: cl.register_click,
        style=ft.ButtonStyle(
            padding=ft.Padding(10, 10, 10, 10),
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Регистрация", size=24, weight=ft.FontWeight.BOLD),
                page.session.get("login_input"),
                page.session.get("password_input"),
                page.session.get("confirm_password_input"),
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


def mainpage_view(page: ft.Page):
    settings = ft.TextButton(content=ft.Text("Настройки", size=20, color=ft.colors.BLUE_ACCENT_700),
                             on_click=lambda _: sw.switch_to_settings(page))
    themes = ft.TextButton(content=ft.Text("Мои темы", size=20, color=ft.colors.BLUE_ACCENT_700),
                           on_click=lambda _: sw.switch_to_mythemes(page))

    profile = ft.Text(page.session.get("login_input").value, size=22)
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
        on_click=lambda _: sw.switch_to_feed(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    newtheme_button = ft.ElevatedButton(
        width=200,
        height=50,
        content=ft.Text("Новая тема", size=24, color=ft.colors.BLUE_ACCENT_700),
        bgcolor=ft.colors.SECONDARY_CONTAINER,
        on_click=lambda _: sw.switch_to_search(page),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    return ft.Column(
        [
            a,
            ft.Row([
                feed_button,
                newtheme_button,
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            ft.Text(""),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True,
    )


def settings_view(page: ft.Page):
    page.session.set("old_pass", ft.TextField(label="Старый пароль", width=300, password=True))
    page.session.set("new_pass", ft.TextField(label="Новый пароль", password=True, width=300))
    exit_button = ft.ElevatedButton(
        content=ft.Text("Выйти из профиля", size=20, color=ft.colors.RED),
        bgcolor=ft.colors.DEEP_ORANGE_100,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.exit_click(page),
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
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    save_button = ft.ElevatedButton(
        content=ft.Text("Сохранить", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.change_pass_click(page),
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
                page.session.get("old_pass"),
                page.session.get("new_pass"),
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


def change_password_error(type_err, page: ft.Page):
    if type_err == 1:
        error_text = ft.Text("Пароль должен содержать не менее 8 символов.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    elif type_err == 2:
        error_text = ft.Text("Введённые значения не должны совпадать.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    else:
        error_text = ft.Text("Неверный пароль.",
                             size=18, weight=ft.FontWeight.NORMAL, color="red", text_align=ft.TextAlign.CENTER)
    page.session.set("old_pass", ft.TextField(label="Старый пароль", width=300, password=True, border_color="red"))
    page.session.set("new_pass", ft.TextField(label="Новый пароль", password=True, width=300, border_color="red"))
    exit_button = ft.ElevatedButton(
        content=ft.Text("Выйти из профиля", size=20, color=ft.colors.RED),
        bgcolor=ft.colors.DEEP_ORANGE_100,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.exit_click(page),
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
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    save_button = ft.ElevatedButton(
        content=ft.Text("Сохранить", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.change_pass_click(page),
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
                page.session.get("old_pass"),
                page.session.get("new_pass"),
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


def feed_view(page: ft.Page):
    topics = page.session.get("user_session").get_tags()
    b = ft.TextButton(content=ft.Row(
        [
            ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
            ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
    ),
        width=200,
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
    for topic in topics:
        topic_row = ft.Row(
            controls=[
                ft.Text(topic["name"], size=18),
                ft.Row(
                    controls=[ft.Text(topic["media"], size=18, color=ft.colors.TERTIARY, weight=ft.FontWeight.BOLD),
                              ft.Text(topic["date"], size=18, color=ft.colors.SECONDARY),
                              ft.ElevatedButton(
                                  content=ft.Text("Смотреть", size=18, color=ft.colors.BLUE_ACCENT_700),
                                  on_click=lambda _: cl.view_click(page),
                                  bgcolor=ft.colors.WHITE, )], alignment=ft.MainAxisAlignment.END, ),
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


def search_view(page: ft.Page):
    search_field = ft.TextField(label="Введите текст", text_size=20, width=1100, height=45, border_color="blue")
    b = ft.TextButton(content=ft.Row(
        [
            ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
            ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
    ),
        width=200,
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    search_button = ft.ElevatedButton(
        content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.search_click(page),
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


def mythemes_view(page: ft.Page):
    topics = page.session.get("user_session").get_tags()
    b = ft.TextButton(content=ft.Row(
        [
            ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
            ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
    ),
        width=200,
        on_click=lambda _: sw.switch_to_mainpage(page),
    )

    topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
    for topic in topics:
        topic_row = ft.Row(
            controls=[
                ft.Text(topic, size=18),
                ft.ElevatedButton(content=ft.Text("Удалить", size=18, color=ft.colors.WHITE),
                                  bgcolor=ft.colors.BLUE_ACCENT_700,
                                  on_click=lambda _: cl.delete_click(topic, page))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.alignment.top_center,
        )
        topics_list.controls.append(topic_row)
    return ft.Container(
        content=ft.Column([b, ft.Text("Мои темы", size=24, weight=ft.FontWeight.BOLD), topics_list, ]),
        alignment=ft.alignment.top_left, expand=True, )


def search_show_view(page: ft.Page):
    topics = page.session.get("user_session").get_tags()
    topics_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.START)
    for topic in topics:
        topic_row = ft.Row(
            controls=[
                ft.Text(topic, size=18),
                ft.Row(
                    controls=[ft.Text(topic["media"], size=18, color=ft.colors.TERTIARY, weight=ft.FontWeight.BOLD),
                              ft.Text(topic["date"], size=18, color=ft.colors.SECONDARY),
                              ft.ElevatedButton(
                                  content=ft.Text("Смотреть", size=18, color=ft.colors.BLUE_ACCENT_700),
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
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    search_button = ft.ElevatedButton(
        content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.search_click(page),
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


def search_show_error(page: ft.Page):
    search_field = ft.TextField(label="Введите текст", text_size=20, width=1100, height=45, border_color="blue")
    b = ft.TextButton(content=ft.Row(
        [
            ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED, color=ft.colors.SECONDARY),
            ft.Text("На главную", size=20, color=ft.colors.SECONDARY),
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
    ),
        width=200,
        on_click=lambda _: sw.switch_to_mainpage(page),
    )
    search_button = ft.ElevatedButton(
        content=ft.Text("Найти", size=22, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=lambda _: cl.search_click(page),
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
                ft.Text("По запросу ничего не найдено.", size=20, weight=ft.FontWeight.NORMAL,
                        color=ft.colors.SECONDARY),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20
        ),
        alignment=ft.alignment.top_left,
        expand=True,
    )
