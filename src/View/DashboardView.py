import flet as ft
from datetime import datetime

def DashboardView(page, tarea_controller):
    user = getattr(page, "user_data", None)

    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    fecha_limite = ft.DatePicker(
        first_date=datetime(2000, 1, 1),
        last_date=datetime(2030, 12, 31)
    )

    hora_limite = ft.TimePicker()

    page.overlay.append(fecha_limite)
    page.overlay.append(hora_limite)

    def abrir_calendario(e):
        fecha_limite.open = True
        page.update()

    def abrir_reloj(e):
        hora_limite.open = True
        page.update()

    txt_fecha = ft.Text("📅 Sin fecha")
    txt_hora = ft.Text("⏰ Sin hora")

    def actualizar_fecha(e):
        if fecha_limite.value:
            txt_fecha.value = f"📅 {fecha_limite.value.strftime('%d/%m/%Y')}"
        page.update()

    def actualizar_hora(e):
        if hora_limite.value:
            txt_hora.value = f"⏰ {hora_limite.value.strftime('%H:%M')}"
        page.update()

    fecha_limite.on_change = actualizar_fecha
    hora_limite.on_change = actualizar_hora

    def cargar_tareas():
        lista_tareas.controls.clear()

        if user and 'id_usuario' in user:
            tareas = tarea_controller.obtener_lista(user['id_usuario'])

            for t in tareas:
                lista_tareas.controls.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(t['titulo'], weight="bold", size=16),
                            ft.Text(t.get('descripcion', '')),
                            ft.Text(f"📌 {t.get('prioridad')} | 🏷 {t.get('clasificacion')}"),
                            ft.Text(f"📊 {t.get('estado')}"),
                            ft.Row([
                                ft.IconButton(
                                    ft.Icons.DELETE,
                                    icon_color=ft.Colors.RED,
                                    on_click=lambda e, id_t=t['id_tarea']: eliminar_tarea(id_t)
                                )
                            ])
                        ]),
                        padding=15,
                        border_radius=12,
                        bgcolor=ft.Colors.WHITE,
                        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.BLACK12)
                    )
                )
        page.update()

    def eliminar_tarea(id_tarea):
        success, msg = tarea_controller.eliminar_tarea(id_tarea)
        if success:
            cargar_tareas()

    txt_titulo = ft.TextField(label="Título", width=300)
    txt_descripcion = ft.TextField(label="Descripción", width=300, multiline=True)

    prioridad = ft.Dropdown(
        value="media",
        width=140,
        options=[ft.dropdown.Option(x) for x in ["alta", "media", "baja"]]
    )

    clasificacion = ft.Dropdown(
        value="personal",
        width=140,
        options=[ft.dropdown.Option(x) for x in ["personal", "trabajo", "estudio"]]
    )

    estado = ft.Dropdown(
        value="pendiente",
        width=160,
        options=[ft.dropdown.Option(x) for x in ["pendiente", "en_progreso", "completada"]]
    )

    def agregar_tarea(e):
        if not txt_titulo.value:
            return

        tarea_controller.guardar_nueva(
            user['id_usuario'],
            txt_titulo.value,
            txt_descripcion.value,
            prioridad.value,
            clasificacion.value,
            estado.value,
            fecha_limite.value.strftime('%Y-%m-%d') if fecha_limite.value else None,
            hora_limite.value.strftime('%H:%M:%S') if hora_limite.value else None
        )

        txt_titulo.value = ""
        txt_descripcion.value = ""
        cargar_tareas()
        page.update()

    cargar_tareas()

    return ft.View(
        route="/dashboard",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Hola, {user.get('nombre', 'Usuario')} 👋"),
                bgcolor=ft.Colors.BLUE_GREY_100,
                actions=[
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ]
            ),

            ft.Container(
                expand=True,
                bgcolor=ft.Colors.BLUE_GREY_50,
                content=ft.Column([

                    # 🔥 CARD CREAR TAREA
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Nueva tarea", size=20, weight="bold"),

                            txt_titulo,
                            txt_descripcion,

                            ft.Row([prioridad, clasificacion, estado], wrap=True),

                            ft.Row([
                                ft.ElevatedButton("Fecha", on_click=abrir_calendario),
                                ft.ElevatedButton("Hora", on_click=abrir_reloj),
                            ]),

                            ft.Row([txt_fecha, txt_hora]),

                            ft.ElevatedButton(
                                "Guardar",
                                bgcolor=ft.Colors.PURPLE,
                                color=ft.Colors.WHITE,
                                on_click=agregar_tarea
                            )
                        ], spacing=10),
                        padding=20,
                        border_radius=15,
                        bgcolor=ft.Colors.WHITE,
                        shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK12)
                    ),

                    ft.Text("Mis tareas", size=20, weight="bold"),

                    lista_tareas

                ], spacing=20),
                padding=20
            )
        ]
    )