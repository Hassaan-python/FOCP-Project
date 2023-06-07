import numpy as np


# imports numpy library

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

    def construct_matrix(self):
        """
        Construct the mass and spring matrices with input values
        """
        try:
            # get inputs of mass values to create mass matrix

            for i in range(self.masses):
                self.mass_matrix[i] = float(input(f'enter mass of mass {i + 1}: '))

            # Get input for spring constants
            for j in range(self.springs):
                self.spring_constants[j] = float(input(f"enter spring constant of spring {j + 1}: "))

        except ValueError as v:  # ensure valid inputs
            print("Enter a positive number only", str(v))

        else:
            # Construct the springs matrix
            for k in range(self.masses):
                self.springs_matrix[k, k] += self.spring_constants[k]

                if k == 0:
                    continue

                self.springs_matrix[k - 1, k] -= self.spring_constants[k]
                self.springs_matrix[k, k - 1] -= self.spring_constants[k]

            for l in range(self.masses):
                self.springs_matrix[l, l] += self.spring_constants[l + 1]

            self.springs_matrix = -1 * self.springs_matrix
            i=0

            for mass in self.mass_matrix:
                self.springs_matrix[i] /= mass
                i+=1
            print(self.springs_matrix)

    def normal_frequencies(self):
        """Calculate normal frequencies"""
        eigenval, eigenvec = np.linalg.eig(self.springs_matrix)  # Calculate eigenvalues and eigenvectors
        normal_frequency= [] # list of normal frequencies
        """Normal frequencies are the square roots of the eigenvalues"""
        for i in eigenval:
            if i<0: # if eigenvalues are negative
                i= f'{abs(i)**(1/2)}i' # square root taken of absolute value and 'i' added separately
            else:
                i= i**(1/2) # otherwise square root taken if the values are positive
            normal_frequency.append(i) # adds all the individual normal frequencies to the list
        return normal_frequency

    def normal_modes(self):
        """Return the eigenvectors (normal modes)"""
        eigenval, eigenvec = np.linalg.eig(self.springs_matrix)
        return eigenvec

    def __repr__(self):
        pass
system = Coupled_Oscillating_System(3,4)
system.construct_matrix()
print(system.normal_frequencies())
print(system.normal_modes())









