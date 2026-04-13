import flet as ft 
from controllers.UserController import AutoController 
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from viewa.dashboard import DashboardView 

def main(page: ft.Page):
    #INSTALAMOS LOS CONTROLADORES UNA SOLA VES 
    auth_crtl = AutoController()
    task_crtl = TareaController()
    
    def route_change(route):
        page.view.clear()
        if page.view == "/":
            page.view.append(LoginView(page, auth_crtl))
        elif page.route == "/dashboard":
            page.view.append(DashboardView(page, task_crtl))
        #agregas aqui el registro_viewde la misma forma 
        page.update()
        
    page.on_route_change = route_change 
    page.go("/")
    
if __name__ == "__main__":
    ft.run(main)