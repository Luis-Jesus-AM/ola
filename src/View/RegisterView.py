import flet as ft
import re
from Moldels.SchemasMoldel import UsuarioSchema  

def RegiView(page: ft.Page, auth_controller):

    nombre = ft.TextField(
        label="Nombre(s)",
        prefix_icon=ft.Icons.PERSON,
        width=300,
        border_radius=10
    )
    
    apellido = ft.TextField(
        label="Apellidos",
        prefix_icon=ft.Icons.PERSON,
        width=300,
        border_radius=10
    )
    
    email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        width=300,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300,
        border_radius=10
    )
    
    confirm_password = ft.TextField(
        label="Confirmar contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300,
        border_radius=10
    )
    
    mensaje = ft.Text("", color=ft.Colors.RED, size=14)

    def mostrar_snackbar(texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()

    def registrar_click(e):
        mensaje.value = ""

        if not nombre.value or not email.value or not password.value or not confirm_password.value:
            mensaje.value = "❌ Todos los campos son obligatorios"
            page.update()
            return
        
        if password.value != confirm_password.value:
            mensaje.value = "❌ Las contraseñas no coinciden"
            page.update()
            return
        
        if len(password.value) < 6:
            mensaje.value = "❌ Mínimo 6 caracteres"
            page.update()
            return
        
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email.value):
            mensaje.value = "❌ Correo inválido"
            page.update()
            return
        
        usuario_data = UsuarioSchema(
            nombre=nombre.value,
            apellido=apellido.value,
            email=email.value,
            password=password.value
        )
        
        exito, msg = auth_controller.registrar(usuario_data)
        
        if exito:
            mostrar_snackbar("✅ Registro exitoso, inicia sesión")
            page.go("/")
        else:
            mensaje.value = f"❌ {msg or 'Error al registrar'}"
            page.update()

    btn_registrar = ft.ElevatedButton(
        "Registrarse",
        bgcolor=ft.Colors.PURPLE,
        color=ft.Colors.WHITE,
        width=300,
        on_click=registrar_click
    )
    
    btn_login = ft.TextButton(
        "¿Ya tienes cuenta? Inicia sesión",
        on_click=lambda _: page.go("/")
    )

    return ft.View(
        route="/register",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Crear Cuenta", size=28, weight=ft.FontWeight.W_500),
                        nombre,
                        apellido,
                        email,
                        password,
                        confirm_password,
                        mensaje,
                        btn_registrar,
                        btn_login
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