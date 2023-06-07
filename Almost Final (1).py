from tkinter import *
from tkinter import Tk, Button, font
import numpy as np
from Simulation import m_s_simulation


class Coupled_Oscillating_System:
    """
    Class representing a coupled oscillating system
    """

    def __init__(self, masses, springs):
        """
        Initialize the Coupled_Oscillating_System object.
        """
        try:
            self.masses = masses
            if springs != masses + 1:
                raise ValueError
        except ValueError:
            print("Number of springs must be 1 more than the number of masses")
        else:
            self.springs = springs
            self.mass_matrix = np.zeros(self.masses)
            self.spring_constants = np.zeros(self.springs)
            self.springs_matrix = np.zeros((self.masses, self.masses))

    def construct_mass_matrix(self):
        """
        Construct the mass matrix using user input values.
        """
        mass_entry_values = [float(entry.get()) for entry in mass_entries]
        self.mass_matrix = np.empty(0)
        self.append_to_mass_matrix(mass_entry_values)
        give_sc_entries()

    def construct_sc_matrix(self):
        """
        Construct the spring constants matrix using user input values.
        """
        sc_entry_values = [float(entry.get()) for entry in sc_entries]
        self.spring_constants = np.empty(0)
        self.append_to_sc_matrix(sc_entry_values)
        bold_font = font.Font(weight="bold", size=10)
        btn4 = Button(win, text="ENTER VALUES", font=bold_font, command=sp_matrix_nf_nm, width=14, height=2)
        btn4.grid(row=scale_value + 2 + a, column=0, columnspan=1, pady=(50, 0), padx=(10, 0))

    def construct_sp_matrix(self):
        """
        Construct the springs matrix based on the mass matrix and spring constants.
        """
        for k in range(self.masses):
            self.springs_matrix[k, k] += self.spring_constants[k]

            if k == 0:
                continue

            self.springs_matrix[k - 1, k] -= self.spring_constants[k]
            self.springs_matrix[k, k - 1] -= self.spring_constants[k]

        for l in range(self.masses):
            self.springs_matrix[l, l] += self.spring_constants[l + 1]

        self.springs_matrix = -1 * self.springs_matrix
        i = 0

        for mass in self.mass_matrix:
            self.springs_matrix[i] /= mass
            i += 1

    def append_to_mass_matrix(self, values1):
        """
        Append values to the mass matrix.
        """
        self.mass_matrix = np.append(self.mass_matrix, values1)

    def append_to_sc_matrix(self, values2):
        """
        Append values to the spring constants matrix.
        """
        self.spring_constants = np.append(self.spring_constants, values2)

    def normal_frequencies(self):
        """
        Calculate normal frequencies.
        """
        eigenval, eigenvec = np.linalg.eig(self.springs_matrix)  # Calculate eigenvalues and eigenvectors
        global normal_frequency
        normal_frequency = []  # list of normal frequencies
        """Normal frequencies are the square roots of the eigenvalues"""
        for i in eigenval:
            if i < 0:  # if eigenvalues are negative
                i = f'{abs(i)**(1/2)}i'  # square root taken of absolute value
            else:
                i = i**(1/2)  # otherwise square root taken if the values are positive
            normal_frequency.append(i)  # adds all the individual normal frequencies to the list
        return normal_frequency

    def normal_modes(self):
        """
        Return the eigenvectors (normal modes).
        """
        global eigenvec
        eigenval, eigenvec = np.linalg.eig(self.springs_matrix)
        return eigenvec

    def __repr__(self):
        pass


def get_scale_value():
    """
    Get the number of masses selected by the user.
    """
    global scale_value
    scale_value = scale.get()
    global system
    system = Coupled_Oscillating_System(scale_value, scale_value + 1)
    give_mass_entries()


def give_mass_entries():
    """
    Create entry fields for mass values.
    """
    global mass_entries
    mass_entries = []
    mass_label = Label(text="Enter the Values of each\n mass(kg)")
    mass_label.grid(row=3, column=0, columnspan=1, pady=2, padx=(10, 0))
    for i in range(scale_value):
        mass_entry = Entry(win)
        mass_entry.grid(row=4+i, column=0, columnspan=1, pady=2, padx=(10, 0))
        mass_entries.append(mass_entry)
    btn2 = Button(win, text="SUBMIT", command=system.construct_mass_matrix)
    btn2.grid(row=scale_value+5, column=0, columnspan=1, pady=(10, 20), padx=(10, 0))


def give_sc_entries():
    """
    Create entry fields for spring constant values.
    """
    global sc_entries
    sc_entries = []
    sc_label = Label(text="Enter the Values of each\nspring constant(N/m)")
    sc_label.grid(row=scale_value+6, column=0, columnspan=1, pady=2, padx=(10, 0))
    global a
    a = scale_value + scale_value + 7
    for j in range(scale_value + 1):
        sc_entry = Entry(win)
        sc_entry.grid(row=a + j, column=0, columnspan=1, pady=2, padx=(10, 0))
        sc_entries.append(sc_entry)
    btn3 = Button(win, text="SUBMIT", command=system.construct_sc_matrix)
    btn3.grid(row=scale_value + 1 + a, column=0, columnspan=1, pady=(10, 20), padx=(10, 0))


def run_simulation():
    """
    Run the simulation.
    """
    m_s_simulation(scale_value)


def sp_matrix_nf_nm():
    """
    Construct the springs matrix, calculate normal frequencies and normal modes.
    """
    system.construct_sp_matrix()
    system.normal_frequencies()
    system.normal_modes()
    for x in range(system.masses):
        display_frequencies = Label(text=f'Frequency {x + 1}:\n{float(normal_frequency[x][:len(normal_frequency[x])-1]):.2f}{normal_frequency[x][len(normal_frequency[x])-1]} Hz')
        display_frequencies.grid(row=1, column=x+12, columnspan=1, padx=10)

    vector = []
    for y in range(system.masses):
        vector_el = []
        for z in range(system.masses):
            eigenvec_2f = f'{eigenvec[z][y]:.2f}'
            eigenvec_2f = str(eigenvec_2f)
            if '-' in eigenvec_2f:
                eigenvec_2f = f'|{eigenvec_2f}|'
            else:
                eigenvec_2f = f'| {eigenvec_2f}|'
            vector_el.append(eigenvec_2f)

        vector.append(vector_el)
        column = '\n'.join(vector[y])
        display_modes = Label(text=f'Mode {y + 1}:\n\n{column}\n')
        display_modes.grid(row=3, column=y + 12, columnspan=1, padx=10)
        btn5 = Button(win, text="RUN SIMULATION", font=("TkDefaultFont", 10, "bold"), command=run_simulation, width=14, height=2)
        btn5.grid(row=5, column=10, columnspan=7)


win = Tk()
win.title("Normal Frequencies of Coupled Mass-Spring Systems")

# win.geometry("200x500")
# Get the screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Set the window size to match the screen size
win.geometry(f"{800}x{screen_height}")

v = DoubleVar()

label = Label(win, text="Choose the number of masses:")
label.grid(row=0, column=0, columnspan=1, pady=10, padx=(10, 20))

scale = Scale(win, variable=v, from_=2, to=5, orient=HORIZONTAL)
scale.grid(row=1, column=0, columnspan=1, pady=3)
scale_value = 0

btn1 = Button(win, text="ENTER", command=get_scale_value)
btn1.grid(row=2, column=0, columnspan=1, pady=(10, 20), padx=(10, 0))
display_modes_head = Label(text=f"Normal Modes:", font=("TkDefaultFont", 9, "bold"))
display_modes_head.grid(row=3, column=10)

display_frequencies_head = Label(text=f"Normal Frequencies:", font=("TkDefaultFont", 9, "bold"))
display_frequencies_head.grid(row=1, column=10)

win.mainloop()
