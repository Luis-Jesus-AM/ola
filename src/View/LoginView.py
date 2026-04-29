# src/View/LoginView.py
import flet as ft

USUARIOS = {
    "admin": {"correo": "admin@gmail.com", "password": "1234"}
}

class LoginView:
    def __init__(self, page: ft.Page):
        self.page = page

        # Campos de usuario y contraseña
        self.user_or_email = ft.TextField(
            label="Usuario o Correo",
            hint_text="Escribe tu usuario o correo",
            prefix_icon=ft.Icons.PERSON,
            width=300
        )
        self.password = ft.TextField(
            label="Contraseña",
            hint_text="Contraseña",
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK,
            width=300
        )

        # Texto de error
        self.error_text = ft.Text("", color=ft.Colors.RED, size=14)

        # Contenedor principal
        self.contenido = ft.Container()

        # Mostrar el login al inicio
        self.mostrar_login()

    # Validación de credenciales
    def validar_credenciales(self, usuario_o_correo, password):
        for usuario, datos in USUARIOS.items():
            if (usuario_o_correo == usuario or usuario_o_correo == datos["correo"]) and password == datos["password"]:
                return True, datos["correo"]
        return False, None

    # Mostrar la página de inicio
    def pagina_inicio(self):
        return ft.Column(
            [
                ft.Text("Bienvenido al Sistema", size=28, weight=ft.FontWeight.BOLD),
                ft.Text("Has iniciado sesión correctamente")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    # Página de explorar
    def pagina_explorar(self):
        return ft.Column(
            [ft.Icon(ft.Icons.EXPLORE, size=60), ft.Text("Explorar contenido", size=25)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    # Página de perfil
    def pagina_perfil(self, correo_usuario):
        return ft.Column(
            [ft.Icon(ft.Icons.PERSON, size=60),
             ft.Text("Perfil del usuario", size=25),
             ft.Text(correo_usuario)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    # Cerrar sesión
    def cerrar_sesion(self):
        self.page.appbar = None
        self.page.clean()
        self.mostrar_login()
        self.page.update()

    # Cambiar entre páginas
    def cambiar_pagina(self, index, correo_usuario):
        if index == 0:
            self.contenido.content = self.pagina_inicio()
        elif index == 1:
            self.contenido.content = self.pagina_explorar()
        elif index == 2:
            self.contenido.content = self.pagina_perfil(correo_usuario)
        elif index == 3:
            self.cerrar_sesion()
            return
        self.page.update()

    # Función para iniciar sesión
    def iniciar_sesion(self, e):
        self.error_text.value = ""

        if not self.user_or_email.value or not self.password.value:
            self.error_text.value = "❌ Debes llenar todos los campos"
            self.page.update()
            return

        valido, correo_usuario = self.validar_credenciales(self.user_or_email.value, self.password.value)
        if valido:
            self.page.clean()
            self.contenido.content = self.pagina_inicio()
            self.page.add(
                ft.Column([self.contenido],
                          alignment=ft.MainAxisAlignment.CENTER,
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )

            self.page.appbar = ft.AppBar(
                title=ft.Text("Welcome to Jurassic Park", color=ft.Colors.BLACK),
                bgcolor=ft.Colors.BLUE_GREY_100,
                leading=ft.IconButton(ft.Icons.LOGOUT, on_click=lambda _: self.cerrar_sesion()),
                actions=[
                    ft.IconButton(ft.Icons.HOME, on_click=lambda _: self.cambiar_pagina(0, correo_usuario)),
                    ft.IconButton(ft.Icons.EXPLORE, on_click=lambda _: self.cambiar_pagina(1, correo_usuario)),
                    ft.IconButton(ft.Icons.PERSON, on_click=lambda _: self.cambiar_pagina(2, correo_usuario)),
                ],
            )
            self.page.update()
        else:
            self.error_text.value = "❌ Usuario o correo o contraseña incorrectos"
            self.page.update()

    # Mostrar formulario de login
    def mostrar_login(self):
        self.user_or_email.value = ""
        self.password.value = ""
        self.error_text.value = ""
        self.page.add(
            ft.Column(
                controls=[
                    ft.Text("Iniciar Sesión", size=30, weight=ft.FontWeight.W_500),
                    self.user_or_email,
                    self.password,
                    self.error_text,
                    ft.ElevatedButton("Iniciar Sesión", bgcolor=ft.Colors.PURPLE,
                                    color=ft.Colors.WHITE, width=300, on_click=self.iniciar_sesion),
                    ft.ElevatedButton("Registrarse", bgcolor=ft.Colors.PURPLE,
                                    color=ft.Colors.WHITE, width=300),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )