import flet as ft

# Navigation options
nav_items = [
    {"label": "Student Info", "route": "/student"},
    {"label": "Exam Marks", "route": "/exam"},
    {"label": "Fee Details", "route": "/fee"},
    {"label": "Department Info", "route": "/dept"}
]

def main(page: ft.Page):
    page.title = "Student Management"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Function to update page content based on the route
    def update_page(route):
        page_content.controls.clear()  # Clear current content
        if route == "/student":
            page_content.controls.append(ft.Text("Student Info", size=30))
        elif route == "/exam":
            page_content.controls.append(ft.Text("Exam Marks", size=30))
        elif route == "/fee":
            page_content.controls.append(ft.Text("Fee Details", size=30))
        elif route == "/dept":
            page_content.controls.append(ft.Text("Department Info", size=30))
        else:
            page_content.controls.append(ft.Text("Welcome to Student Management System", size=30))
        page.update()

    # Function to handle navigation button click
    def nav_item_clicked(e):
        page.go(e.control.data)  # Navigate to the route

    # Create navbar with a "Home" button and background color
    navbar = ft.Row(
        controls=[
            ft.TextButton("Home", data="/", icon=ft.icons.HOME, on_click=nav_item_clicked, style=ft.ButtonStyle(color="white",bgcolor="blue")),  # Home button with white icon and text
            *[
                ft.TextButton(nav["label"], data=nav["route"], on_click=nav_item_clicked, style=ft.ButtonStyle(color="white",bgcolor="blue"))
                for nav in nav_items  # Other nav buttons styled with white text
            ]
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
    )

    # Container to hold the navbar with a skyblue background
    navbar_container = ft.Container(
        content=navbar,
        bgcolor="grey",  # Skyblue background for the navbar  # Padding to make the navbar look better
        height=50,
    )

    # A container for page content
    page_content = ft.Column()

    # Add navbar at the top of the page and the content below it
    page.add(
        ft.Column(
            controls=[
                navbar_container,  # Navbar container with skyblue background
                page_content  # Dynamic content section below navbar
            ],
            expand=True  # Allow the content section to expand and fill the page
        )
    )

    # Handle route change
    page.on_route_change = lambda e: update_page(page.route)

    # Default route
    update_page(page.route)

if __name__ == '__main__':
    ft.app(target=main)
