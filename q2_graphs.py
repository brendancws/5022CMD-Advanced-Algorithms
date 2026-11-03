
# ============================================================
# CLASS 1: GRAPH
# ============================================================
# This class represents a directed graph used to manage
# university course prerequisite relationships.
#
# A graph is a data structure made up of:
# 1. Vertices - Represent individual university courses.
# 2. Edges - Represent prerequisite relationships.
#
# This system uses a directed graph because prerequisite
# relationships have a specific direction.
#
# Example:
# CS101 -> CS201
#
# This means CS101 is a prerequisite for CS201.
# Completing CS101 unlocks CS201.
#
# The graph is implemented using an adjacency list.
# An adjacency list stores each vertex together with
# a list of vertices directly connected from it.
# ============================================================

class Graph:

    # Constructor method that initializes the graph.
    # A dictionary is used to represent the adjacency list.
    #
    # Example:
    # {
    #     "CS101": ["CS201", "CS302"],
    #     "CS201": ["CS301"]
    # }
    #
    # The dictionary key represents the source course,
    # while the list contains courses it directly unlocks.
    def __init__(self):

        # Adjacency list used to store the directed graph
        self.adj_list = {}

    # --------------------------------------------------------
    # METHOD 1: ADD VERTEX
    # --------------------------------------------------------
    # Adds a new vertex (course) into the graph.
    #
    # Each vertex represents a university course code.
    #
    # Before inserting, the method checks whether the
    # vertex already exists in the adjacency list.
    #
    # If the vertex does not exist, it is added with an
    # empty list to represent no outgoing edges initially.
    #
    # This prevents duplicate vertices from being created.
    # --------------------------------------------------------

    def addVertex(self, vertex):

        # Add a new vertex if it does not already exist
        if vertex not in self.adj_list:

            # Creates a new dictionary entry for the course.
            # The empty list will store its outgoing neighbors.
            self.adj_list[vertex] = []

    # --------------------------------------------------------
    # METHOD 2: ADD DIRECTED EDGE
    # --------------------------------------------------------
    # Adds a directed edge between two courses.
    #
    # The source represents the prerequisite course.
    # The destination represents the course being unlocked.
    #
    # Example:
    # addEdge("CS101", "CS201")
    #
    # This means students must complete CS101 before
    # taking CS201.
    #
    # Both courses must exist in the graph before
    # a relationship can be created.
    #
    # The method also prevents duplicate edges.
    # --------------------------------------------------------

    def addEdge(self, source, destination):

        # Add a directed edge from source to destination

        # Checks that both source and destination courses
        # already exist as vertices in the graph.
        if source in self.adj_list and destination in self.adj_list:

            # Checks that this relationship does not already exist.
            if destination not in self.adj_list[source]:

                # Adds the destination to the source's adjacency list.
                # This creates a one-way directed relationship.
                self.adj_list[source].append(destination)

    # --------------------------------------------------------
    # METHOD 3: FIND INCOMING ADJACENT VERTICES
    # --------------------------------------------------------
    # Finds all vertices that have directed edges pointing
    # towards a specified target vertex.
    #
    # In this system, incoming vertices represent the
    # direct prerequisite courses of the target course.
    #
    # Example:
    # CS201 -> CS301
    #
    # If the target is CS301, the incoming vertex is CS201.
    # Therefore, CS201 is a direct prerequisite of CS301.
    #
    # The method examines every vertex in the adjacency
    # list to identify which vertices connect to the target.
    #
    # It returns a list of prerequisite course codes.
    #
    # Time Complexity: O(V + E)
    # V = Number of vertices
    # E = Number of edges
    # --------------------------------------------------------

    def listIncomingAdjacentVertex(self, target_vertex):

        # Find all vertices that point towards the target vertex

        # Creates an empty list to store prerequisite courses.
        incoming = []

        # Iterates through every vertex and its outgoing neighbors.
        # items() provides both the course code and its neighbor list.
        for vertex, neighbors in self.adj_list.items():

            # Checks whether the target course appears in
            # the current vertex's outgoing adjacency list.
            if target_vertex in neighbors:

                # If found, the current vertex is a prerequisite.
                # Adds its course code to the incoming list.
                incoming.append(vertex)

        # Returns all direct prerequisites found for the course.
        # An empty list means no incoming connections were found.
        return incoming

    # --------------------------------------------------------
    # METHOD 4: GET OUTGOING VERTICES
    # --------------------------------------------------------
    # Retrieves all vertices directly connected from a
    # specified source vertex.
    #
    # In this system, outgoing vertices represent courses
    # that are directly unlocked by completing a course.
    #
    # Example:
    # CS101 -> CS201
    # CS101 -> CS302
    #
    # Searching for CS101 returns ["CS201", "CS302"].
    #
    # The dictionary's get() method safely retrieves
    # the adjacency list of the specified source vertex.
    #
    # If the vertex does not exist, an empty list is returned.
    # --------------------------------------------------------

    def getOutgoingVertices(self, source_vertex):

        # Return all vertices connected from the source vertex
        return self.adj_list.get(source_vertex, [])


# ============================================================
# CLASS 2: COURSE
# ============================================================
# This class represents an individual university course.
#
# Each Course object contains four attributes:
#
# 1. Course Code - Unique identifier for the course.
# 2. Course Name - Full name of the course.
# 3. Credit Hours - Academic credit value of the course.
# 4. Level - Course category (Core or Elective).
#
# The class separates course information from the graph.
#
# The Graph class manages prerequisite relationships,
# while the Course class stores course details.
#
# This demonstrates object-oriented programming by
# organizing related data and methods within a class.
# ============================================================

class Course:

    # Constructor method used to create a new course object.
    # The provided parameters are stored as object attributes.
    def __init__(self, course_code, course_name, credit_hours, level):

        # Stores the unique course code.
        self.courseCode = course_code

        # Stores the full name of the course.
        self.courseName = course_name

        # Stores the number of academic credit hours.
        self.creditHours = credit_hours

        # Stores whether the course is Core or Elective.
        self.level = level

    # --------------------------------------------------------
    # METHOD: DISPLAY COURSE DETAILS
    # --------------------------------------------------------
    # Displays all information belonging to a Course object.
    #
    # The method allows users to view the selected course's
    # code, name, credit hours, and category.
    #
    # Using a separate display method avoids repeatedly
    # writing the same print statements in the main program.
    # --------------------------------------------------------

    def display_details(self):

        # Display all information about the course

        # Displays the unique course identifier.
        print(f"Course Code: {self.courseCode}")

        # Displays the full course name.
        print(f"Course Name: {self.courseName}")

        # Displays the academic credit value.
        print(f"Credit Hours: {self.creditHours}")

        # Displays the course category.
        print(f"Level: {self.level}")


# ============================================================
# FUNCTION 3: VALIDATE COURSE CODE
# ============================================================
# This function checks whether the course code entered
# by the user exists in the course dictionary.
#
# Parameters:
# courses - Dictionary containing available university courses.
# prompt - Message displayed when asking for a course code.
#
# The function repeatedly requests input until the
# user enters an existing course code.
#
# strip() removes unnecessary spaces from the input.
# upper() converts lowercase letters to uppercase.
#
# Example:
# Input: cs101
# Converted: CS101
#
# If the course exists, the function returns its code.
# Otherwise, an error message is displayed and the
# user is asked to enter another course code.
#
# This prevents the program from accessing invalid
# course codes when displaying course information.
# ============================================================

def get_valid_course_code(courses, prompt):

    # Keep asking until the user enters a valid course code
    while True:

        # Reads the course code entered by the user.
        # Removes extra spaces and converts it to uppercase.
        target = input(prompt).strip().upper()

        # Checks whether the entered code exists
        # as a key in the courses dictionary.
        if target in courses:

            # Returns the valid course code to the main program.
            return target

        # Displays an error when the course code does not exist.
        # The while loop will continue requesting input.
        print("Course not found. Please try again.")


# ============================================================
# FUNCTION 4: MAIN PROGRAM
# ============================================================
# This function controls the University Course
# Prerequisite System.
#
# Main responsibilities:
# 1. Create the directed graph.
# 2. Store university course information.
# 3. Add course codes as graph vertices.
# 4. Add prerequisite relationships as directed edges.
# 5. Display the menu for user interaction.
# 6. Allow users to view available courses.
# 7. Display details of a selected course.
# 8. Find direct prerequisites of a course.
# 9. Find courses directly unlocked by a course.
# 10. Allow the user to exit the program.
#
# A while loop keeps the program running until the
# user chooses the exit option.
# ============================================================

def main():

    # --------------------------------------------------------
    # STEP 1: INITIALIZE GRAPH
    # --------------------------------------------------------
    # Creates an instance of the Graph class.
    #
    # The graph will represent all university courses
    # and their directed prerequisite relationships.
    # --------------------------------------------------------

    # Create graph object
    univ_graph = Graph()

    # --------------------------------------------------------
    # STEP 2: CREATE UNIVERSITY COURSES
    # --------------------------------------------------------
    # A dictionary is used to store Course objects.
    #
    # Each dictionary key is a unique course code.
    # Each dictionary value is a Course object containing
    # the course name, credit hours, and category.
    #
    # This allows quick retrieval of course details
    # by using the course code as the dictionary key.
    #
    # Six sample university courses are created:
    #
    # CS101 - Introduction to Programming
    # CS201 - Data Structures
    # CS301 - Advanced Algorithms
    # CS302 - Database Systems
    # CS401 - Artificial Intelligence
    # CS405 - Web Development
    # --------------------------------------------------------

    # Create Course objects
    courses = {

        # Foundation programming course with 4 credit hours.
        "CS101": Course(
            "CS101",
            "Introduction to Programming",
            4,
            "Core"
        ),

        # Core course focusing on data structures.
        "CS201": Course(
            "CS201",
            "Data Structures",
            4,
            "Core"
        ),

        # Core course focusing on advanced algorithms.
        "CS301": Course(
            "CS301",
            "Advanced Algorithms",
            3,
            "Core"
        ),

        # Core course covering database systems.
        "CS302": Course(
            "CS302",
            "Database Systems",
            3,
            "Core"
        ),

        # Elective course covering artificial intelligence.
        "CS401": Course(
            "CS401",
            "Artificial Intelligence",
            3,
            "Elective"
        ),

        # Elective course focusing on web development.
        "CS405": Course(
            "CS405",
            "Web Development",
            3,
            "Elective"
        )
    }

    # --------------------------------------------------------
    # STEP 3: ADD COURSES AS GRAPH VERTICES
    # --------------------------------------------------------
    # Every course code in the dictionary is added
    # to the graph as an individual vertex.
    #
    # Each vertex initially has an empty adjacency list.
    #
    # Example:
    # "CS101": []
    # "CS201": []
    #
    # Prerequisite relationships will be added next.
    # --------------------------------------------------------

    # Add all course codes as vertices
    for code in courses:

        # Creates one graph vertex for each course code.
        univ_graph.addVertex(code)

    # --------------------------------------------------------
    # STEP 4: ADD PREREQUISITE RELATIONSHIPS
    # --------------------------------------------------------
    # Directed edges are created to represent the
    # prerequisite relationships between courses.
    #
    # Direction: prerequisite -> course unlocked
    #
    # Example:
    # CS101 -> CS201
    #
    # This means CS101 must be completed before CS201.
    #
    # These relationships form a directed graph.
    # Each edge only points in one direction.
    # --------------------------------------------------------

    # Add prerequisite relationships

    # CS101 is a prerequisite for CS201.
    univ_graph.addEdge("CS101", "CS201")

    # CS101 is also a prerequisite for CS302.
    univ_graph.addEdge("CS101", "CS302")

    # CS201 is a prerequisite for CS301.
    univ_graph.addEdge("CS201", "CS301")

    # CS301 is a prerequisite for CS401.
    univ_graph.addEdge("CS301", "CS401")

    # CS302 is a prerequisite for CS405.
    univ_graph.addEdge("CS302", "CS405")

    # --------------------------------------------------------
    # GRAPH STRUCTURE AFTER INSERTION
    # --------------------------------------------------------
    # The resulting adjacency list represents:
    #
    # CS101 -> [CS201, CS302]
    # CS201 -> [CS301]
    # CS301 -> [CS401]
    # CS302 -> [CS405]
    # CS401 -> []
    # CS405 -> []
    #
    # Courses with empty adjacency lists do not
    # directly unlock any additional courses.
    #
    # Notice that CS101 indirectly leads to CS401
    # through CS201 and CS301.
    #
    # However, the program's methods retrieve only
    # direct incoming or outgoing relationships.
    # --------------------------------------------------------

    # --------------------------------------------------------
    # STEP 5: MAIN MENU LOOP
    # --------------------------------------------------------
    # The while True loop continuously displays the menu
    # until the user selects option 5 to exit.
    #
    # This allows multiple operations to be performed
    # without restarting the entire program.
    # --------------------------------------------------------

    while True:

        # Displays the available system functions.
        print("\n==== University Course Prerequisite System ====")
        print("1. View All Courses")
        print("2. View Course Details")
        print("3. View Prerequisites of a Course")
        print("4. View Courses Unlocked by a Course")
        print("5. Exit")

        # Reads the user's menu selection.
        # strip() removes unnecessary spaces.
        choice = input("Enter your choice (1-5): ").strip()

        # -------------------------------------------------
        # OPTION 1: VIEW ALL COURSES
        # -------------------------------------------------
        # Displays every available university course.
        #
        # The program loops through the course dictionary
        # and prints the code and name of each course.
        #
        # items() allows access to both the dictionary key
        # and the Course object associated with that key.
        #
        # Example output:
        # CS101 - Introduction to Programming
        # CS201 - Data Structures
        # -------------------------------------------------

        if choice == "1":

            # Displays the heading for the course list.
            print("\n--- All Available Courses ---")

            # Loops through all course codes and objects.
            for code, course_obj in courses.items():

                # Prints the course code and full course name.
                print(f"{code} - {course_obj.courseName}")

        # -------------------------------------------------
        # OPTION 2: VIEW COURSE DETAILS
        # -------------------------------------------------
        # Allows the user to view detailed information
        # about a particular university course.
        #
        # The user must enter a valid course code.
        #
        # The validation function checks whether the course
        # exists before the information is displayed.
        #
        # Once validated, the program retrieves the
        # appropriate Course object from the dictionary.
        #
        # The display_details() method prints the
        # course information.
        # -------------------------------------------------

        elif choice == "2":

            # Requests a valid course code from the user.
            target = get_valid_course_code(
                courses,
                "Enter Course Code: "
            )

            # Displays the course details heading.
            print("\n--- Course Details ---")

            # Retrieves the selected course object
            # and calls its display_details() method.
            courses[target].display_details()

        # -------------------------------------------------
        # OPTION 3: VIEW PREREQUISITES
        # -------------------------------------------------
        # Allows the user to identify the direct prerequisite
        # courses required for a selected course.
        #
        # This option uses incoming adjacent vertices.
        #
        # An incoming edge points from a prerequisite
        # course towards the selected target course.
        #
        # Example:
        # CS201 -> CS301
        #
        # Searching for CS301 identifies CS201
        # as its direct prerequisite.
        #
        # If no incoming edges exist, the program
        # displays a message indicating that the
        # selected course has no prerequisites.
        #
        # Note: This option shows direct prerequisites
        # only, not every indirect prerequisite.
        # -------------------------------------------------

        elif choice == "3":

            # Requests and validates the course code.
            target = get_valid_course_code(
                courses,
                "Enter Course Code to check prerequisites: "
            )

            # Calls the graph method to retrieve vertices
            # with directed edges pointing to the target.
            prereqs = univ_graph.listIncomingAdjacentVertex(target)

            # Displays the selected course name and code.
            print(
                f"\n--- Prerequisites for "
                f"{courses[target].courseName} ({target}) ---"
            )

            # Checks whether the prerequisite list is empty.
            if not prereqs:

                # Displays this message when no incoming
                # prerequisite edges were found.
                print("None. This course has no prerequisites.")

            else:

                # Loops through each direct prerequisite.
                for req in prereqs:

                    # Displays the prerequisite course code
                    # together with its full course name.
                    print(
                        f"- {req} "
                        f"({courses[req].courseName})"
                    )

        # -------------------------------------------------
        # OPTION 4: VIEW COURSES UNLOCKED
        # -------------------------------------------------
        # Allows the user to view courses that are
        # directly unlocked by a selected course.
        #
        # This option uses outgoing adjacent vertices.
        #
        # An outgoing edge points from the selected
        # course towards another course that requires it.
        #
        # Example:
        # CS101 -> CS201
        # CS101 -> CS302
        #
        # Searching for CS101 returns CS201 and CS302.
        #
        # These represent courses directly unlocked
        # after completing CS101.
        #
        # If no outgoing edges exist, the system
        # displays a message indicating that no
        # further courses are directly unlocked.
        #
        # This option does not display courses unlocked
        # indirectly through multiple prerequisite edges.
        # -------------------------------------------------

        elif choice == "4":

            # Requests a valid course code from the user.
            target = get_valid_course_code(
                courses,
                "Enter Course Code to see what it unlocks: "
            )

            # Retrieves all outgoing adjacent vertices
            # connected to the selected course.
            unlocked = univ_graph.getOutgoingVertices(target)

            # Displays the course name and code
            # for which unlocked courses are being shown.
            print(
                f"\n--- Courses Unlocked by "
                f"{courses[target].courseName} ({target}) ---"
            )

            # Checks whether the list of unlocked courses is empty.
            if not unlocked:

                # Displays a message when the course
                # has no outgoing prerequisite relationships.
                print(
                    "None. This course does not unlock "
                    "any further courses."
                )

            else:

                # Iterates through every directly unlocked course.
                for course_code in unlocked:

                    # Displays the unlocked course code and name.
                    print(
                        f"- {course_code} "
                        f"({courses[course_code].courseName})"
                    )

        # -------------------------------------------------
        # OPTION 5: EXIT
        # -------------------------------------------------
        # Allows the user to terminate the system.
        #
        # The break statement stops the while True loop.
        # Once the loop finishes, the main() function
        # also finishes, ending the program.
        # -------------------------------------------------

        elif choice == "5":

            # Displays a farewell message to the user.
            print("Exiting University Course Prerequisite System. Goodbye!")

            # Exits the main menu loop.
            break

        # -------------------------------------------------
        # INVALID MENU OPTION
        # -------------------------------------------------
        # Handles user input that does not match
        # any of the available menu options.
        #
        # For example, entering 6 or an alphabet character
        # will display an error message.
        #
        # The while loop continues and shows the menu again.
        # -------------------------------------------------

        else:

            # Informs the user that the selected option is invalid.
            print("Invalid choice. Please select a number from 1 to 5.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
# This condition checks whether the Python file
# is being executed directly.
#
# __name__ is a special Python variable.
#
# When the file runs directly, its value is "__main__".
#
# The main() function is then executed to start
# the University Course Prerequisite System.
#
# This also prevents the main function from running
# automatically if the file is imported into another program.
# ============================================================

if __name__ == "__main__":
    main()
