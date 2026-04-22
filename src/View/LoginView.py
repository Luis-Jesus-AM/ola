import flet as ft

USER_CORRECTO = "admin"
CORREO_CORRECTO = "admin@gmail.com"
PASSWORD_CORRECTO = "1234"

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    user = ft.TextField(
        label="User",
        hint_text="Usuario",
        prefix_icon=ft.Icons.PERSON,
        width=300
    )

    correo = ft.TextField(
        label="Correo",
        hint_text="Correo electronico",
        prefix_icon=ft.Icons.ALTERNATE_EMAIL,
        width=300
    )

    password = ft.TextField(
        label="Contraseña",
        hint_text="Contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        width=300
    )

    contenido = ft.Container()

    pagina_inicio = ft.Column(
        [
            ft.Text("Bienvenido al Sistema", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Has iniciado sesión correctamente")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina_explorar = ft.Column(
        [
            ft.Icon(ft.Icons.EXPLORE, size=60),
            ft.Text("Explorar contenido", size=25)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina_perfil = ft.Column(
        [
            ft.Icon(ft.Icons.PERSON, size=60),
            ft.Text("Perfil del usuario", size=25),
            ft.Text("admin@gmail.com")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    def cambiar_pagina(e):
        if e.control.selected_index == 0:
            contenido.content = pagina_inicio
        elif e.control.selected_index == 1:
            contenido.content = pagina_explorar
        elif e.control.selected_index == 2:
            contenido.content = pagina_perfil
        page.update()

    def iniciar_sesion(e):

        if user.value == "" or correo.value == "" or password.value == "":
            page.snack_bar = ft.SnackBar(
                ft.Text("Datos incorrectos ❌ Debes llenar todos los campos")
            )
            page.snack_bar.open = True
            page.update()
            return

        if (
            user.value == USER_CORRECTO
            and correo.value == CORREO_CORRECTO
            and password.value == PASSWORD_CORRECTO
        ):

            page.snack_bar = ft.SnackBar(ft.Text("Felicidades, has iniciado sesión 🎉"))
            page.snack_bar.open = True

            page.clean()

            contenido.content = pagina_inicio

            page.add(
                ft.Column(
                    [
                        contenido
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )

            page.navigation_bar = ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(
                        icon=ft.Icons.HOME,
                        label="Inicio"
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.EXPLORE,
                        label="Explorar"
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.PERSON,
                        label="Perfil"
                    ),
                ],
                on_change=cambiar_pagina
            )

            page.update()

        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Usuario o contraseña incorrectos ❌")
            )
            page.snack_bar.open = True
            page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Iniciar Sesion",
                    size=30,
                    weight=ft.FontWeight.W_500
                ),
                user,
                correo,
                password,

                ft.ElevatedButton(
                    "Iniciar Sesion",
                    bgcolor=ft.Colors.PURPLE,
                    color=ft.Colors.WHITE,
                    width=300,
                    on_click=iniciar_sesion
                ),

                ft.ElevatedButton(
                    "Registrarse",
                    bgcolor=ft.Colors.PURPLE,
                    color=ft.Colors.WHITE,
                    width=300
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)