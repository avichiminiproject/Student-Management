import flet as ft

def main(page: ft.Page):
    page.title = "Student Management"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

if __name__ == '__main__':
    ft.app(main)