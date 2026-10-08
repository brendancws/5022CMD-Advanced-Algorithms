class Graph:
    def __init__(self):
        # Adjacency list used to store the directed graph
        self.adj_list = {}

    def addVertex(self, vertex):
        # Add a new vertex if it does not already exist
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def addEdge(self, source, destination):
        # Add a directed edge from source to destination
        if source in self.adj_list and destination in self.adj_list:
            if destination not in self.adj_list[source]:
                self.adj_list[source].append(destination)

    def listIncomingAdjacentVertex(self, target_vertex):
        # Find all vertices that point towards the target vertex
        incoming = []

        for vertex, neighbors in self.adj_list.items():
            if target_vertex in neighbors:
                incoming.append(vertex)

        return incoming

    def getOutgoingVertices(self, source_vertex):
        # Return all vertices connected from the source vertex
        return self.adj_list.get(source_vertex, [])


class Course:
    def __init__(self, course_code, course_name, credit_hours, level):
        self.courseCode = course_code
        self.courseName = course_name
        self.creditHours = credit_hours
        self.level = level

    def display_details(self):
        # Display all information about the course
        print(f"Course Code: {self.courseCode}")
        print(f"Course Name: {self.courseName}")
        print(f"Credit Hours: {self.creditHours}")
        print(f"Level: {self.level}")


def get_valid_course_code(courses, prompt):
    # Keep asking until the user enters a valid course code
    while True:
        target = input(prompt).strip().upper()

        if target in courses:
            return target

        print("Course not found. Please try again.")


def main():
    # Create graph object
    univ_graph = Graph()

    # Create Course objects
    courses = {
        "CS101": Course(
            "CS101",
            "Introduction to Programming",
            4,
            "Core"
        ),

        "CS201": Course(
            "CS201",
            "Data Structures",
            4,
            "Core"
        ),

        "CS301": Course(
            "CS301",
            "Advanced Algorithms",
            3,
            "Core"
        ),

        "CS302": Course(
            "CS302",
            "Database Systems",
            3,
            "Core"
        ),

        "CS401": Course(
            "CS401",
            "Artificial Intelligence",
            3,
            "Elective"
        ),

        "CS405": Course(
            "CS405",
            "Web Development",
            3,
            "Elective"
        )
    }

    # Add all course codes as vertices
    for code in courses:
        univ_graph.addVertex(code)

    # Add prerequisite relationships
    # Direction: prerequisite -> course unlocked
    univ_graph.addEdge("CS101", "CS201")
    univ_graph.addEdge("CS101", "CS302")
    univ_graph.addEdge("CS201", "CS301")
    univ_graph.addEdge("CS301", "CS401")
    univ_graph.addEdge("CS302", "CS405")

    while True:
        print("\n==== University Course Prerequisite System ====")
        print("1. View All Courses")
        print("2. View Course Details")
        print("3. View Prerequisites of a Course")
        print("4. View Courses Unlocked by a Course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        # -------------------------------------------------
        # OPTION 1: VIEW ALL COURSES
        # -------------------------------------------------
        if choice == "1":
            print("\n--- All Available Courses ---")

            for code, course_obj in courses.items():
                print(f"{code} - {course_obj.courseName}")

        # -------------------------------------------------
        # OPTION 2: VIEW COURSE DETAILS
        # -------------------------------------------------
        elif choice == "2":
            target = get_valid_course_code(
                courses,
                "Enter Course Code: "
            )

            print("\n--- Course Details ---")
            courses[target].display_details()

        # -------------------------------------------------
        # OPTION 3: VIEW PREREQUISITES
        # -------------------------------------------------
        elif choice == "3":
            target = get_valid_course_code(
                courses,
                "Enter Course Code to check prerequisites: "
            )

            prereqs = univ_graph.listIncomingAdjacentVertex(target)

            print(
                f"\n--- Prerequisites for "
                f"{courses[target].courseName} ({target}) ---"
            )

            if not prereqs:
                print("None. This course has no prerequisites.")

            else:
                for req in prereqs:
                    print(
                        f"- {req} "
                        f"({courses[req].courseName})"
                    )

        # -------------------------------------------------
        # OPTION 4: VIEW COURSES UNLOCKED
        # -------------------------------------------------
        elif choice == "4":
            target = get_valid_course_code(
                courses,
                "Enter Course Code to see what it unlocks: "
            )

            unlocked = univ_graph.getOutgoingVertices(target)

            print(
                f"\n--- Courses Unlocked by "
                f"{courses[target].courseName} ({target}) ---"
            )

            if not unlocked:
                print(
                    "None. This course does not unlock "
                    "any further courses."
                )

            else:
                for course_code in unlocked:
                    print(
                        f"- {course_code} "
                        f"({courses[course_code].courseName})"
                    )

        # -------------------------------------------------
        # OPTION 5: EXIT
        # -------------------------------------------------
        elif choice == "5":
            print("Exiting University Course Prerequisite System. Goodbye!")
            break

        # -------------------------------------------------
        # INVALID MENU OPTION
        # -------------------------------------------------
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()