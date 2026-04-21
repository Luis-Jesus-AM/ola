import flet as ft

def LoginView(page: ft.Page, auth_controller):
    email_input = ft.TextField(
        label="Correo electrónico",
        width=350,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10
    )

    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snackbar = ft.Snackbar(ft.Text("Por favor, completa todos los campos"))
            page.snackbar.open = True
            page.update()
            return
        
        user, msg = auth_controller.login(email_input.value, pass_input.value)

        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snackbar = ft.Snackbar(ft.Text(msg))
            page.snackbar.open = True
            page.update()

    login_button = ft.ElevatedButton(
        "entrar",
        on_click=login_click,
        width=350,
        bgcolor="blue",
        color="white"
    )

    pass_input.on_submit = login_click

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar = ft.Appbar(
            title=ft.Text("SIGE - Login"),
            bgcolor="bluegrey900",
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al sistema",size=24, weigth="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    ft.TextButton(
                        "crea una cuenta nueva",
                        on_click=lambda _: page.go("/register")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )

