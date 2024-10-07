import flet as ft

def main(page: ft.Page):
    page.title = "Student Management"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
if __name__ == '__main__':
    ft.app(main)