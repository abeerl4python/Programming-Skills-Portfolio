import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, code, name, mark1, mark2, mark3, exam_mark):
        self.code = code
        self.name = name
        self.coursework_marks = [mark1, mark2, mark3]
        self.exam_mark = exam_mark
        self.total_coursework = sum(self.coursework_marks)
        self.overall_total = self.total_coursework + exam_mark
        self.overall_percentage = (self.overall_total / 160) * 100
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.overall_percentage >= 70:
            return 'A'
        elif self.overall_percentage >= 60:
            return 'B'
        elif self.overall_percentage >= 50:
            return 'C'
        elif self.overall_percentage >= 40:
            return 'D'
        else:
            return 'F'

def load_students():
    data = [
        "1345,John Curry,8,15,7,45",
        "2345,Sam Sturtivant,14,15,14,77",
        "9876,Lee Scott,17,11,16,99",
        "3724,Matt Thompson,19,11,15,81",
        "1212,Ron Herrema,14,17,18,66",
        "8439,Jake Hobbs,10,11,10,43",
        "2344,Jo Hyde,6,15,10,55",
        "9384,Gareth Southgate,5,6,8,33",
        "8327,Alan Shearer,20,20,20,100",
        "2983,Les Ferdinand,15,17,18,92"
    ]
    
    students = []
    for entry in data:
        fields = entry.split(',')
        students.append(Student(
            int(fields[0]),  
            fields[1],       
            int(fields[2]),  
            int(fields[3]),  
            int(fields[4]),  
            int(fields[5])   
        ))
    return students

class StudentManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.students = load_students()
        
        # Create Layout
        self.create_layout()

    def create_layout(self):
        # Title
        tk.Label(self.root, text="Student Manager", font=("Arial", 16)).grid(row=0, column=1, pady=10)

        # Buttons
        tk.Button(self.root, text="View All Student Records", command=self.view_all_students, width=25).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(self.root, text="Show Highest Score", command=self.show_highest_score, width=25).grid(row=1, column=1, padx=20, pady=10)
        tk.Button(self.root, text="Show Lowest Score", command=self.show_lowest_score, width=25).grid(row=1, column=2, padx=20, pady=10)
        
        tk.Button(self.root, text="Sort Student Records", command=self.sort_students_menu, width=25).grid(row=2, column=0, padx=20, pady=10)
        tk.Button(self.root, text="Add Student Record", command=self.add_student, width=25).grid(row=2, column=1, padx=20, pady=10)
        tk.Button(self.root, text="Delete Student Record", command=self.delete_student_menu, width=25).grid(row=2, column=2, padx=20, pady=10)
        tk.Button(self.root, text="Update Student Record", command=self.update_student_menu, width=25).grid(row=3, column=1, padx=20, pady=10)

        # Label for viewing individual student
        tk.Label(self.root, text="View Individual Student Record", font=("Arial", 12)).grid(row=4, column=1, pady=10)

        # Dropdown menu for selecting individual student
        self.student_var = tk.StringVar(self.root)
        self.student_var.set(self.students[0].name)  

        student_menu = tk.OptionMenu(self.root, self.student_var, *[student.name for student in self.students])
        student_menu.grid(row=5, column=1, pady=5)

        # View record button
        tk.Button(self.root, text="View Record", command=self.view_individual_student, width=20).grid(row=6, column=1, pady=5)

        # Text box for displaying results
        self.text_box = tk.Text(self.root, height=15, width=80)
        self.text_box.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    def display_student_info(self, student):
        result = (f"Name: {student.name}\n"
                  f"Number: {student.code}\n"
                  f"Coursework Total: {student.total_coursework}\n"
                  f"Exam Mark: {student.exam_mark}\n"
                  f"Overall Percentage: {student.overall_percentage:.2f}%\n"
                  f"Grade: {student.grade}\n")
        self.text_box.insert(tk.END, result + "\n")

    def view_all_students(self):
        self.text_box.delete(1.0, tk.END)  # Clear the text box
        total_percentage = 0
        for student in self.students:
            self.display_student_info(student)
            total_percentage += student.overall_percentage
        
        avg_percentage = total_percentage / len(self.students)
        self.text_box.insert(tk.END, f"\nTotal Students: {len(self.students)}, Average Percentage: {avg_percentage:.2f}%\n")

    def view_individual_student(self):
        self.text_box.delete(1.0, tk.END)  
        selected_student_name = self.student_var.get()
        student = next(s for s in self.students if s.name == selected_student_name)
        self.display_student_info(student)

    def show_highest_score(self):
        self.text_box.delete(1.0, tk.END)  
        highest = max(self.students, key=lambda s: s.overall_total)
        self.display_student_info(highest)

    def show_lowest_score(self):
        self.text_box.delete(1.0, tk.END)  
        lowest = min(self.students, key=lambda s: s.overall_total)
        self.display_student_info(lowest)

    def sort_students_menu(self):
        sort_order = tk.simpledialog.askstring("Sort Order", "Enter 'asc' for ascending or 'desc' for descending:")
        if sort_order in ['asc', 'desc']:
            reverse = (sort_order == 'desc')
            self.students.sort(key=lambda s: s.overall_total, reverse=reverse)
            self.view_all_students()
        else:
            messagebox.showerror("Error", "Invalid input. Please enter 'asc' or 'desc'.")

    def add_student(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Student Record")

        tk.Label(add_window, text="Code:").grid(row=0, column=0)
        code_entry = tk.Entry(add_window)
        code_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Mark 1:").grid(row=2, column=0)
        mark1_entry = tk.Entry(add_window)
        mark1_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Mark 2:").grid(row=3, column=0)
        mark2_entry = tk.Entry(add_window)
        mark2_entry.grid(row=3, column=1)

        tk.Label(add_window, text="Mark 3:").grid(row=4, column=0)
        mark3_entry = tk.Entry(add_window)
        mark3_entry.grid(row=4, column=1)

        tk.Label(add_window, text="Exam Mark:").grid(row=5, column=0)
        exam_entry = tk.Entry(add_window)
        exam_entry.grid(row=5, column=1)

        def save_student():
            try:
                code = int(code_entry.get())
                name = name_entry.get()
                mark1 = int(mark1_entry.get())
                mark2 = int(mark2_entry.get())
                mark3 = int(mark3_entry.get())
                exam_mark = int(exam_entry.get())
                new_student = Student(code, name, mark1, mark2, mark3, exam_mark)
                self.students.append(new_student)
                self.save_students_to_file()
                messagebox.showinfo("Success", "Student added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid input.")

        tk.Button(add_window, text="Add Student", command=save_student).grid(row=6, column=0, columnspan=2)

    def delete_student_menu(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Student Record")

        tk.Label(delete_window, text="Enter Student Code or Name:").grid(row=0, column=0)
        delete_entry = tk.Entry(delete_window)
        delete_entry.grid(row=0, column=1)

        def delete_student():
            search_term = delete_entry.get()
            to_delete = []
            for student in self.students:
                if str(student.code) == search_term or student.name.lower() == search_term.lower():
                    to_delete.append(student)
            if to_delete:
                for student in to_delete:
                    self.students.remove(student)
                self.save_students_to_file()
                messagebox.showinfo("Success", "Student record deleted successfully!")
                delete_window.destroy()
            else:
                messagebox.showerror("Error", "No student found with that code or name.")

        tk.Button(delete_window, text="Delete Student", command=delete_student).grid(row=1, column=0, columnspan=2)

    def update_student_menu(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Student Record")

        tk.Label(update_window, text="Enter Student Code or Name:").grid(row=0, column=0)
        update_entry = tk.Entry(update_window)
        update_entry.grid(row=0, column=1)

        def update_student():
            search_term = update_entry.get()
            student_to_update = None
            for student in self.students:
                if str(student.code) == search_term or student.name.lower() == search_term.lower():
                    student_to_update = student
                    break
            
            if student_to_update:
                self.show_update_options(student_to_update)
                update_window.destroy()
            else:
                messagebox.showerror("Error", "No student found with that code or name.")

        tk.Button(update_window, text="Find Student", command=update_student).grid(row=1, column=0, columnspan=2)

    def show_update_options(self, student):
        update_option_window = tk.Toplevel(self.root)
        update_option_window.title("Update Options")

        tk.Label(update_option_window, text="Select the item to update:").grid(row=0, column=0, columnspan=2)

        def update_code():
            new_code = tk.simpledialog.askinteger("Update Code", "Enter new code:")
            if new_code is not None:
                student.code = new_code
                self.save_students_to_file()
                messagebox.showinfo("Success", "Student code updated successfully!")

        def update_name():
            new_name = tk.simpledialog.askstring("Update Name", "Enter new name:")
            if new_name:
                student.name = new_name
                self.save_students_to_file()
                messagebox.showinfo("Success", "Student name updated successfully!")

        def update_marks():
            new_marks = []
            for i in range(1, 4):
                mark = tk.simpledialog.askinteger("Update Mark", f"Enter new mark {i}:")
                if mark is not None:
                    new_marks.append(mark)
            if len(new_marks) == 3:
                student.coursework_marks = new_marks
                student.total_coursework = sum(new_marks)
                student.overall_total = student.total_coursework + student.exam_mark
                student.overall_percentage = (student.overall_total / 160) * 100
                student.grade = student.calculate_grade()
                self.save_students_to_file()
                messagebox.showinfo("Success", "Student marks updated successfully!")

        def update_exam():
            new_exam_mark = tk.simpledialog.askinteger("Update Exam Mark", "Enter new exam mark:")
            if new_exam_mark is not None:
                student.exam_mark = new_exam_mark
                student.overall_total = student.total_coursework + new_exam_mark
                student.overall_percentage = (student.overall_total / 160) * 100
                student.grade = student.calculate_grade()
                self.save_students_to_file()
                messagebox.showinfo("Success", "Student exam mark updated successfully!")

        tk.Button(update_option_window, text="Update Code", command=update_code).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(update_option_window, text="Update Name", command=update_name).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(update_option_window, text="Update Marks", command=update_marks).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(update_option_window, text="Update Exam Mark", command=update_exam).grid(row=2, column=1, padx=10, pady=5)

    def save_students_to_file(self):
        with open("students.txt", "w") as file:
            for student in self.students:
                file.write(f"{student.code},{student.name},{','.join(map(str, student.coursework_marks))},{student.exam_mark}\n")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()