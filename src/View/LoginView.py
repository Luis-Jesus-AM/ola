import flet as ft

def LoginView(page: ft.Page, auth_controller):

    user_or_email = ft.TextField(
        label="Usuario o Correo",
        hint_text="Escribe tu usuario o correo",
        prefix_icon=ft.Icons.PERSON,
        width=300,
        border_radius=10
    )

    password = ft.TextField(
        label="Contraseña",
        hint_text="Contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        width=300,
        border_radius=10
    )

    error_text = ft.Text("", color=ft.Colors.RED, size=14)

    def mostrar_snackbar(texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()

    def login_click(e):
        error_text.value = ""

        if not user_or_email.value or not password.value:
            error_text.value = "❌ Debes llenar todos los campos"
            page.update()
            return

        user, msg = auth_controller.login(user_or_email.value, password.value)

        if user:
            page.user_data = user
            mostrar_snackbar("✅ Sesión iniciada correctamente")
            page.go("/dashboard")
        else:
            error_text.value = f"❌ {msg}"
            page.update()

    login_btn = ft.ElevatedButton(
        "Iniciar Sesión",
        bgcolor=ft.Colors.PURPLE,
        color=ft.Colors.WHITE,
        width=300,
        on_click=login_click
    )

    register_btn = ft.TextButton(
        "¿No tienes cuenta? Regístrate",
        on_click=lambda _: page.go("/register")
    )

    password.on_submit = login_click

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Iniciar Sesión", size=30, weight=ft.FontWeight.W_500),
                        user_or_email,
                        password,
                        error_text,
                        login_btn,
                        register_btn
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15
                ),
                padding=30,
                border_radius=15,
                bgcolor=ft.Colors.BLUE_GREY_50,
                shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK12)
            )
        ]
    )