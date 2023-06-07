from vpython import*

# Define the length of the system
length = 10.

# Function to simulate a mass-spring system
def m_s_simulation(x):
    # Check if the value of x is valid
    if x == 2:
        # Create a 3D scene
        scene2 = canvas(title='Coupled Mass-Spring System(2 Masses)', width=400, height=200, center=vector(length,0,0), background=color.white) 
        # Initialize masses
        ball=sphere(pos=vector(2,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball2=sphere(pos=vector(2 + length*2,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)

        # Initialize walls
        wall_right=box(pos=vector(3*length,0,0), size= vector(0.2, 5, 5), color = color.green)
        wall_left=box(pos=vector(-length,0,0), size= vector(0.2, 5, 5), color = color.green)

        # Create invisible sections
        section1=box(pos=vector(length,0,0), size= vector(0.2, 5, 5), opacity = 0)
        section2=box(pos=vector(length/2,0,0), size= vector(0.2, 5, 5), opacity = 0)
        section3=box(pos=vector(1.5*length,0,0), size= vector(0.2, 5, 5), opacity = 0)

        # Initialize springs
        spring_right=helix(pos=wall_right.pos,axis=ball2.pos - wall_right.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red)
        mid_spring=helix(pos=vector(2*length+2,0,0),axis=ball.pos - ball2.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red,velocity=vector(0,0,0))
        spring_left=helix(pos=wall_left.pos,axis=ball.pos-wall_left.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red)

        # Function to calculate the acceleration of a mass
        def acc(left, self, right):  
            # Calculate the displacement vector between the masses
            dr_left = self.pos - left.pos
            dr_right = self.pos - right.pos
            # Calculate the spring force using Hooke's law
            force_right = -1*(mag(dr_right) - length)*norm(dr_right)
            force_left = -1*(mag(dr_left) - length)*norm(dr_left)
            # Calculate and return the net acceleration of the mass
            return (force_right+force_left)/ball.mass

        # Simulation parameters
        t=0
        dt=0.01
        # Main simulation loop
        while (t<1000):
            rate(500)
            # Update the velocity and position of the masses
            ball.velocity=ball.velocity+acc(wall_left, ball, section1)*dt
            ball.pos=ball.pos+ball.velocity*dt

            ball2.velocity=ball2.velocity+acc(section1, ball2, wall_right)*dt
            ball2.pos=ball2.pos+ball2.velocity*dt
            # Update the springs' positions and axes
            spring_right.axis=ball2.pos - wall_right.pos
            spring_left.axis=ball.pos - wall_left.pos
            #   mid_spring.axis=ball.pos - ball2.pos
            mid_spring.velocity=mid_spring.velocity+acc(section2, mid_spring, section3)*dt
            mid_spring.pos=mid_spring.pos+mid_spring.velocity*dt
            # Increment the time
            t=t+dt

    if x == 3:
        # Create a 3D scene
        scene2 = canvas(title='Coupled Mass-Spring System(3 Masses)', width=600, height=200, center=vector(length,0,0), background=color.white) 
        # Initialize masses
        ball=sphere(pos=vector(2,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball2=sphere(pos=vector(2 + 2*length,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball3=sphere(pos=vector(2 + 4*length,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)

        # Initialize walls
        wall_right=box(pos=vector(5*length,0,0), size= vector(0.2, 5, 5), color = color.green)
        wall_left=box(pos=vector(-length,0,0), size= vector(0.2, 5, 5), color = color.green)

        # Create invisible sections
        section1=box(pos=vector(length,0,0), size= vector(0.2, 5, 5), opacity = 0)
        section2=box(pos=vector(3*length,0,0), size= vector(0.2, 5, 5), opacity = 0)
        section3=box(pos=vector(length/2,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section4=box(pos=vector(1.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section5=box(pos=vector(2.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section6=box(pos=vector(3.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)


        # Initialize springs
        spring_right=helix(pos=wall_right.pos,axis=ball3.pos - wall_right.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red, velocity=vector(0,0,0))
        mid_spring1=helix(pos=vector(2*length+2,0,0),axis=ball.pos - ball2.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red, velocity=vector(0,0,0))
        mid_spring2=helix(pos=vector(4*length+2,0,0),axis=ball2.pos - ball3.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red, velocity=vector(0,0,0))
        spring_left=helix(pos=wall_left.pos,axis=ball.pos-wall_left.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red, velocity=vector(0,0,0))
        
        # Function to calculate the acceleration of a mass
        def acc(left, self, right):  
            # Calculate the displacement vector between the masses
            dr_left = self.pos - left.pos
            dr_right = self.pos - right.pos
            # Calculate the spring force using Hooke's law
            force_right = -1*(mag(dr_right) - length)*norm(dr_right)
            force_left = -1*(mag(dr_left) - length)*norm(dr_left)
            # Calculate and return the net acceleration of the mass
            return (force_right+force_left)/ball.mass

        # Simulation parameters
        t=0
        dt=0.01
        # Main simulation loop
        while (t<1000):
            rate(500)

            # Update the velocity and position of the masses
            ball.velocity=ball.velocity+acc(wall_left, ball, section1)*dt
            ball.pos=ball.pos+ball.velocity*dt

            ball2.velocity=ball2.velocity+acc(section1, ball2, section2)*dt
            ball2.pos=ball2.pos+ball2.velocity*dt

            ball3.velocity=ball3.velocity+acc(section2, ball3, wall_right)*dt
            ball3.pos=ball3.pos+ball3.velocity*dt

            # Update the springs' positions and axes
            spring_right.axis=ball3.pos - wall_right.pos
            spring_left.axis=ball.pos - wall_left.pos

            mid_spring1.velocity=mid_spring1.velocity+acc(section3, mid_spring1, section4)*dt
            mid_spring1.pos=mid_spring1.pos+mid_spring1.velocity*dt

            mid_spring2.velocity=mid_spring2.velocity+acc(section5, mid_spring2, section6)*dt
            mid_spring2.pos=mid_spring2.pos+mid_spring2.velocity*dt
            # Increment the time
            t=t+dt    

    if x == 4:
        # Create a 3D scene
        scene2 = canvas(title='Coupled Mass-Spring System(4 Masses)', width=800, height=200, center=vector(3*length,0,0), background=color.white) 
        # Initialize masses
        ball=sphere(pos=vector(2,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball2=sphere(pos=vector(2 + length*2,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball3=sphere(pos=vector(2 + length*4,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball4=sphere(pos=vector(2 + length*6,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)

        # Initialize walls
        wall_right=box(pos=vector(7*length,0,0), size= vector(0.2, 5, 5), color = color.green)
        wall_left=box(pos=vector(-length,0,0), size= vector(0.2, 5, 5), color = color.green)

        # Create invisible sections
        section1=box(pos=vector(length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section2=box(pos=vector(length/2,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section3=box(pos=vector(1.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section4=box(pos=vector(3*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section5=box(pos=vector(2.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section6=box(pos=vector(3.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section7=box(pos=vector(5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section8=box(pos=vector(4.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section9=box(pos=vector(5.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)

        # Initialize springs
        spring_right=helix(pos=wall_right.pos,axis=ball4.pos - wall_right.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red)
        mid_spring1=helix(pos=vector(2*length+2,0,0),axis=ball.pos - ball2.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red,velocity=vector(0,0,0))
        mid_spring2=helix(pos=vector(4*length+2,0,0),axis=ball2.pos - ball3.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red,velocity=vector(0,0,0))
        mid_spring3=helix(pos=vector(6*length+2,0,0),axis=ball3.pos - ball4.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red,velocity=vector(0,0,0))
        spring_left=helix(pos=wall_left.pos,axis=ball.pos-wall_left.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red)

        # Function to calculate the acceleration of a mass
        def acc(left, self, right):  
            # Calculate the displacement vector between the masses
            dr_left = self.pos - left.pos
            dr_right = self.pos - right.pos
            # Calculate the spring force using Hooke's law
            force_right = -1*(mag(dr_right) - length)*norm(dr_right)
            force_left = -1*(mag(dr_left) - length)*norm(dr_left)
            # Calculate and return the net acceleration of the mass
            return (force_right+force_left)/ball.mass
        
        # Simulation parameters
        t=0
        dt=0.01
        # Main simulation loop
        while (t<1000):
            rate(500)
            # Update the velocity and position of the masses
            ball.velocity=ball.velocity+acc(wall_left, ball, section1)*dt
            ball.pos=ball.pos+ball.velocity*dt

            ball2.velocity=ball2.velocity+acc(section1, ball2, section4)*dt
            ball2.pos=ball2.pos+ball2.velocity*dt

            ball3.velocity=ball3.velocity+acc(section4, ball3, section7)*dt
            ball3.pos=ball3.pos+ball3.velocity*dt

            ball4.velocity=ball4.velocity+acc(section7, ball4, wall_right)*dt
            ball4.pos=ball4.pos+ball4.velocity*dt

            # Update the springs' positions and axes
            mid_spring1.velocity=mid_spring1.velocity+acc(section2, mid_spring1, section3)*dt
            mid_spring1.pos=mid_spring1.pos+mid_spring1.velocity*dt

            mid_spring2.velocity=mid_spring2.velocity+acc(section5, mid_spring2, section6)*dt
            mid_spring2.pos=mid_spring2.pos+mid_spring2.velocity*dt

            mid_spring3.velocity=mid_spring3.velocity+acc(section8, mid_spring3, section9)*dt
            mid_spring3.pos=mid_spring3.pos+mid_spring3.velocity*dt
            # Increment the time
            t=t+dt

    if x == 5:
        # Create a 3D scene
        scene2 = canvas(title='Coupled Mass-Spring System(5 Masses)', width=1000, height=200, center=vector(4*length,0,0), background=color.white) 
        # Initialize masses
        ball=sphere(pos=vector(2,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball2=sphere(pos=vector(2 + length*2,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball3=sphere(pos=vector(2 + length*4,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball4=sphere(pos=vector(2 + length*6,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)
        ball5=sphere(pos=vector(2 + length*8,0,0),velocity=vector(0,0,0),radius=2.5,mass=1, color=color.blue)

        # Initialize walls
        wall_right=box(pos=vector(9*length,0,0), size= vector(0.2, 5, 5), color = color.green)
        wall_left=box(pos=vector(-length,0,0), size= vector(0.2, 5, 5), color = color.green)

        # Create invisible sections
        section1=box(pos=vector(length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section2=box(pos=vector(length/2,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section3=box(pos=vector(1.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section4=box(pos=vector(3*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section5=box(pos=vector(2.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section6=box(pos=vector(3.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section7=box(pos=vector(5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section8=box(pos=vector(4.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section9=box(pos=vector(5.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section10=box(pos=vector(7*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section11=box(pos=vector(6.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)
        section12=box(pos=vector(7.5*length,0,0), size= vector(0.2, 5, 5), opacity= 0)

        # Initialize springs
        spring_right=helix(pos=wall_right.pos,axis=ball5.pos - wall_right.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red)
        mid_spring1=helix(pos=vector(2*length+2,0,0),axis=ball.pos - ball2.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red,velocity=vector(0,0,0))
        mid_spring2=helix(pos=vector(4*length+2,0,0),axis=ball2.pos - ball3.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red,velocity=vector(0,0,0))
        mid_spring3=helix(pos=vector(6*length+2,0,0),axis=ball3.pos - ball4.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red,velocity=vector(0,0,0))
        mid_spring4=helix(pos=vector(8*length+2,0,0),axis=ball4.pos - ball5.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red,velocity=vector(0,0,0))
        spring_left=helix(pos=wall_left.pos,axis=ball.pos-wall_left.pos,constant=1,coils = 10,thickness=0.2,radius=1, color = color.red)

        # Function to calculate the acceleration of a mass
        def acc(left, self, right):  
            # Calculate the displacement vector between the masses
            dr_left = self.pos - left.pos
            dr_right = self.pos - right.pos
            # Calculate the spring force using Hooke's law
            force_right = -1*(mag(dr_right) - length)*norm(dr_right)
            force_left = -1*(mag(dr_left) - length)*norm(dr_left)
            # Calculate and return the net acceleration of the mass
            return (force_right+force_left)/ball.mass
        
        # Simulation parameters
        t=0
        dt=0.01
        # Main simulation loop
        while (t<1000):
            rate(500)
            # Update the velocity and position of the masses
            ball.velocity=ball.velocity+acc(wall_left, ball, section1)*dt
            ball.pos=ball.pos+ball.velocity*dt

            ball2.velocity=ball2.velocity+acc(section1, ball2, section4)*dt
            ball2.pos=ball2.pos+ball2.velocity*dt

            ball3.velocity=ball3.velocity+acc(section4, ball3, section7)*dt
            ball3.pos=ball3.pos+ball3.velocity*dt

            ball4.velocity=ball4.velocity+acc(section7, ball4, section10)*dt
            ball4.pos=ball4.pos+ball4.velocity*dt

            ball5.velocity=ball5.velocity+acc(section10, ball5, wall_right)*dt
            ball5.pos=ball5.pos+ball5.velocity*dt

            # Update the springs' positions and axes
            mid_spring1.velocity=mid_spring1.velocity+acc(section2, mid_spring1, section3)*dt
            mid_spring1.pos=mid_spring1.pos+mid_spring1.velocity*dt

            mid_spring2.velocity=mid_spring2.velocity+acc(section5, mid_spring2, section6)*dt
            mid_spring2.pos=mid_spring2.pos+mid_spring2.velocity*dt

            mid_spring3.velocity=mid_spring3.velocity+acc(section8, mid_spring3, section9)*dt
            mid_spring3.pos=mid_spring3.pos+mid_spring3.velocity*dt

            mid_spring4.velocity=mid_spring4.velocity+acc(section11, mid_spring4, section12)*dt
            mid_spring4.pos=mid_spring4.pos+mid_spring4.velocity*dt
            # Increment the time
            t=t+dt