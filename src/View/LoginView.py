import flet as ft

USUARIOS = {
    "admin": {"correo": "admin@gmail.com", "password": "1234"}
}

def validar_credenciales(usuario_o_correo, password):
    for usuario, datos in USUARIOS.items():
        if (
            (usuario_o_correo == usuario or usuario_o_correo == datos["correo"])
            and password == datos["password"]
        ):
            return True, datos["correo"]
    return False, None

def main(page: ft.Page):
    page.title = "Inicio de sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    user_or_email = ft.TextField(
        label="Usuario o Correo",
        hint_text="Escribe tu usuario o correo",
        prefix_icon=ft.Icons.PERSON,
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

    # Texto de error dentro del formulario
    error_text = ft.Text("", color=ft.Colors.RED, size=14)

    contenido = ft.Container()

    def pagina_inicio():
        return ft.Column(
            [ft.Text("Bienvenido al Sistema", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Has iniciado sesión correctamente")],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def pagina_explorar():
        return ft.Column(
            [ft.Icon(ft.Icons.EXPLORE, size=60), ft.Text("Explorar contenido", size=25)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def pagina_perfil(correo_usuario):
        return ft.Column(
            [ft.Icon(ft.Icons.PERSON, size=60), ft.Text("Perfil del usuario", size=25), ft.Text(correo_usuario)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def cerrar_sesion():
        page.appbar = None
        page.clean()
        mostrar_login()
        page.update()

    def cambiar_pagina(index, correo_usuario):
        if index == 0:
            contenido.content = pagina_inicio()
        elif index == 1:
            contenido.content = pagina_explorar()
        elif index == 2:
            contenido.content = pagina_perfil(correo_usuario)
        elif index == 3:
            cerrar_sesion()
            return
        page.update()

    def iniciar_sesion(e):
        # Resetear mensaje de error
        error_text.value = ""

        if not user_or_email.value or not password.value:
            error_text.value = "❌ Debes llenar todos los campos"
            page.update()
            return

        valido, correo_usuario = validar_credenciales(user_or_email.value, password.value)
        if valido:
            page.clean()
            contenido.content = pagina_inicio()
            page.add(
                ft.Column([contenido],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )

            page.appbar = ft.AppBar(
                title=ft.Text("Welcome to Jurassic Park", color=ft.Colors.BLACK),
                bgcolor=ft.Colors.BLUE_GREY_100,
                leading=ft.IconButton(ft.Icons.LOGOUT, on_click=lambda _: cerrar_sesion()),
                actions=[
                    ft.IconButton(ft.Icons.HOME, on_click=lambda _: cambiar_pagina(0, correo_usuario)),
                    ft.IconButton(ft.Icons.EXPLORE, on_click=lambda _: cambiar_pagina(1, correo_usuario)),
                    ft.IconButton(ft.Icons.PERSON, on_click=lambda _: cambiar_pagina(2, correo_usuario)),
                ],
            )
            page.update()
        else:
            error_text.value = "❌ Usuario o correo o contraseña incorrectos"
            page.update()

    def mostrar_login():
        user_or_email.value = ""
        password.value = ""
        error_text.value = ""
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Iniciar Sesión", size=30, weight=ft.FontWeight.W_500),
                    user_or_email,
                    password,
                    error_text,  # Aquí aparece el mensaje de error
                    ft.ElevatedButton("Iniciar Sesión", bgcolor=ft.Colors.PURPLE, color=ft.Colors.WHITE, width=300, on_click=iniciar_sesion),
                    ft.ElevatedButton("Registrarse", bgcolor=ft.Colors.PURPLE, color=ft.Colors.WHITE, width=300),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    mostrar_login()

ft.app(target=main)
