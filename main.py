import flet as ft
from database import search_student, add_student  # Import the MySQL functions

# Main Flet app
def main(page: ft.Page):
    page.title = "Student Management"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Function to handle route changes
    def route_change(route):
        page.views.clear()
        if page.route == "/student":
            page.views.append(student_info_view())
        elif page.route == "/exam":
            page.views.append(exam_marks_view())
        elif page.route == "/fee":
            page.views.append(fee_details_view())
        elif page.route == "/dept":
            page.views.append(department_info_view())
        else:
            page.views.append(home_view())
        page.update()

    # Home view (default)
    def home_view():
        return ft.View(
            "/",
            controls=[
                navbar,
                ft.Text("Welcome to the Student Management System", size=24)
            ]
        )

    # Student Info view
    def student_info_view():
        return ft.View(
            "/student",
            controls=[
                navbar,
                ft.Row([rollno_field, phone_field, search_button], alignment=ft.MainAxisAlignment.CENTER),
                student_details,
                copy_button,
                add_student_button
            ]
        )

    # Exam Marks view (dummy for now)
    def exam_marks_view():
        return ft.View(
            "/exam",
            controls=[
                navbar,
                ft.Text("Exam Marks View", size=24)
            ]
        )

    # Fee Details view (dummy for now)
    def fee_details_view():
        return ft.View(
            "/fee",
            controls=[
                navbar,
                ft.Text("Fee Details View", size=24)
            ]
        )

    # Department Info view (dummy for now)
    def department_info_view():
        return ft.View(
            "/dept",
            controls=[
                navbar,
                ft.Text("Department Info View", size=24)
            ]
        )

    # Function to handle search
    def search_student_details(e):
        rollno = rollno_field.value
        phone = phone_field.value
        student = search_student(rollno=rollno, phone=phone)
        if student:
            details = f"Rollno: {student['rollno']}\nName: {student['name']}\nPhone: {student['phone']}"
            student_details.value = details
            copy_button.visible = True
        else:
            student_details.value = "No student found"
            copy_button.visible = False
        page.update()

    # Function to copy student details to clipboard
    def copy_to_clipboard(e):
        page.set_clipboard(student_details.value)
        page.snack_bar = ft.SnackBar(ft.Text("Copied to clipboard"))
        page.snack_bar.open = True
        page.update()

    # Function to handle opening the form for adding a student
    def open_add_student_form(e):
        add_student_dialog.open = True
        page.update()

    # Function to handle student form submission
    def submit_student_form(e):
        data = {
            "rollno": rollno_input.value,
            "name": name_input.value,
            "age": int(age_input.value),
            "gender": gender_radio_group.value,
            "phone": phone_input.value,
            "fathername": fathername_input.value,
            "mothername": mothername_input.value,
            "address": address_input.value,
            "deptid": int(deptid_input.value)
        }
        add_student(data)
        page.snack_bar = ft.SnackBar(ft.Text("Student added successfully!"))
        page.snack_bar.open = True
        add_student_dialog.open = False
        page.update()

    # Search bar
    rollno_field = ft.TextField(label="Search by Rollno")
    phone_field = ft.TextField(label="Search by Phone Number")
    search_button = ft.TextButton("Search", on_click=search_student_details, style=ft.ButtonStyle(color="white", bgcolor='blue'))

    student_details = ft.Text(value="", size=18)
    copy_button = ft.TextButton("Copy to Clipboard", on_click=copy_to_clipboard, visible=False)

    # Add student button
    add_student_button = ft.TextButton("Add Student", on_click=open_add_student_form)

    # Dialog box for adding student details
    rollno_input = ft.TextField(label="Rollno", expand=True)
    name_input = ft.TextField(label="Name", expand=True)
    age_input = ft.TextField(label="Age", expand=True)
    phone_input = ft.TextField(label="Phone Number", expand=True)
    fathername_input = ft.TextField(label="Father's Name", expand=True)
    mothername_input = ft.TextField(label="Mother's Name", expand=True)
    address_input = ft.TextField(label="Address", expand=True)
    deptid_input = ft.TextField(label="Department ID", expand=True)
    gender_radio_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Male", label="Male"),
            ft.Radio(value="Female", label="Female")
        ])
    )

    submit_button = ft.TextButton("Submit", on_click=submit_student_form)

    # Dialog for adding a student
    add_student_dialog = ft.AlertDialog(
        title=ft.Text("Add New Student"),
        content=ft.Column([
            rollno_input,
            name_input,
            age_input,
            gender_radio_group,
            phone_input,
            fathername_input,
            mothername_input,
            address_input,
            deptid_input,
            submit_button
        ]),
        open=False
    )

    # Navbar for navigation
    navbar = ft.Row(
        controls=[
            ft.TextButton("Home", data="/", icon=ft.icons.HOME, on_click=lambda e: page.go("/"), style=ft.ButtonStyle(color="white", bgcolor='blue')),
            ft.TextButton("Student Info", data="/student", on_click=lambda e: page.go("/student"), style=ft.ButtonStyle(color="white", bgcolor='blue')),
            ft.TextButton("Exam Marks", data="/exam", on_click=lambda e: page.go("/exam"), style=ft.ButtonStyle(color="white", bgcolor='blue')),
            ft.TextButton("Fee Details", data="/fee", on_click=lambda e: page.go("/fee"), style=ft.ButtonStyle(color="white", bgcolor='blue')),
            ft.TextButton("Department Info", data="/dept", on_click=lambda e: page.go("/dept"), style=ft.ButtonStyle(color="white", bgcolor='blue'))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Add route_change and initial navigation
    page.on_route_change = route_change
    page.go(page.route)  # Start at the initial route

    # Append the dialog to page overlay
    page.overlay.append(add_student_dialog)

if __name__ == '__main__':
    ft.app(target=main)
