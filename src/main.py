import flet as ft
from Controllers.UserControllers import AuthController 
from Controllers.TareaController import TareaController
from View.LoginView import LoginView
from View.DashboardView import DashboardView  

def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            
            page.views.a0ppend(LoginView(page, auth_ctrl))
            
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacía")])
            )

        page.update()
        
    def view_pop(e):
        if len(page.view)> 1 : 
            page.views.pop()
            top_view = page.view[-1]
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    if page.route == "/":
        route_change(None)
    else:page.go("/")

def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()