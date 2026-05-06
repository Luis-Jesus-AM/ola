import flet as ft

def UserView(page, auth_controller):
    page.title = "Perfil"
    user = getattr(page, "user_data", None)
    
    nombre = ft.Text(f"Nombre: {user['nombre'] if user else 'Usuario'}", size=20)
    apellido = ft.Text(f"Apellido: {user['apellido'] if user else 'Usuario'}", size=20)
    email = ft.Text(f"Email: {user['email'] if user else 'Usuario'}", size=20)
    fecha_registro = ft.Text(f"Fecha de creacion de la cuenta: {user['fecha_registro'] if user else 'Usuario'}", size=20)
    ultimo_acceso = ft.Text(f"Último acceso: {user['ultimo_acceso'] if user else 'Usuario'}", size=20)

    return ft.View(
        route="/perfil",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Perfil de Usuario", size=30),
                actions=[
                    ft.IconButton(ft.Icons.BOOK, on_click=lambda _: page.go("/dashboard")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Container(
                ft.Column([
                    ft.Divider(thickness=8, color=ft.Colors.BLUE),
                    ft.Row([nombre]),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([apellido]),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([email]),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Divider(thickness=8, color=ft.Colors.BLUE),
                    ft.Row([fecha_registro]),
                    ft.Divider(thickness=8, color=ft.Colors.BLUE),
                    ft.Row([ultimo_acceso]),
                ], expand=True),
                padding=20, expand=True,
            ),
        ]
    )