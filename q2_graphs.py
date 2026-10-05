class Graph:
    def __init__(self):
        self.adj_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def addEdge(self, source, destination):
        if source in self.adj_list and destination in self.adj_list:
            if destination not in self.adj_list[source]:
                self.adj_list[source].append(destination)

    def listIncomingAdjacentVertex(self, target_vertex):
        incoming = []
        for vertex, neighbors in self.adj_list.items():
            if target_vertex in neighbors:
                incoming.append(vertex)
        return incoming

    def getOutgoingVertices(self, source_vertex):
        return self.adj_list.get(source_vertex, [])


class Course:
    def __init__(self, course_code, course_name, credit_hours, level):
        self.courseCode = course_code
        self.courseName = course_name
        self.creditHours = credit_hours
        self.level = level  # "Core" or "Elective"

    def display_profile(self):
        if self.level.lower() == 'elective':
            print(f"[{self.courseCode}] {self.courseName} (Elective) - Further details are hidden.")
        else:
            print(f"[{self.courseCode}] {self.courseName} | Credits: {self.creditHours} | Level: {self.level}")


def main():
    univ_graph = Graph()

    courses = {
        "CS101": Course("CS101", "Introduction to Programming", 4, "Core"),
        "CS201": Course("CS201", "Data Structures", 4, "Core"),
        "CS301": Course("CS301", "Advanced Algorithms", 3, "Core"),
        "CS302": Course("CS302", "Database Systems", 3, "Core"),
        "CS401": Course("CS401", "Artificial Intelligence", 3, "Elective"),
        "CS405": Course("CS405", "Web Development", 3, "Elective")
    }

    for code in courses.keys():
        univ_graph.addVertex(code)

    univ_graph.addEdge("CS101", "CS201")
    univ_graph.addEdge("CS101", "CS302")
    univ_graph.addEdge("CS201", "CS301")
    univ_graph.addEdge("CS301", "CS401")
    univ_graph.addEdge("CS302", "CS405")

    while True:
        print("\n==== University Course Prerequisite System ====")
        print("1. View All Courses")
        print("2. View Course Details")
        print("3. View Prerequisites of a Course (Incoming Edges)")
        print("4. View Courses Unlocked by a Course (Outgoing Edges)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            print("\n--- All Available Courses ---")
            for code, course_obj in courses.items():
                print(f"{code} - {course_obj.courseName}")

        elif choice == '2':
            while True:
                target = input("Enter Course Code: ").strip().upper()
                if target in courses:
                    print("\n--- Course Details ---")
                    courses[target].display_profile()
                    break
                else:
                    print("Course not found in the system. Please try again.")

        elif choice == '3':
            while True:
                target = input("Enter Course Code to check prerequisites: ").strip().upper()
                if target in courses:
                    prereqs = univ_graph.listIncomingAdjacentVertex(target)
                    print(f"\n--- Prerequisites for {courses[target].courseName} ({target}) ---")
                    if not prereqs:
                        print("None. You can take this course immediately.")
                    else:
                        for req in prereqs:
                            print(f"- {req} ({courses[req].courseName})")
                    break
                else:
                    print("Course not found. Please try again.")

        elif choice == '4':
            while True:
                target = input("Enter Course Code to see what it unlocks: ").strip().upper()
                if target in courses:
                    unlocked = univ_graph.getOutgoingVertices(target)
                    print(f"\n--- Courses unlocked by {courses[target].courseName} ({target}) ---")
                    if not unlocked:
                        print("None. This course does not serve as a prerequisite for any further courses.")
                    else:
                        for unl in unlocked:
                            print(f"- {unl} ({courses[unl].courseName})")
                    break
                else:
                    print("Course not found. Please try again.")

        elif choice == '5':
            print("Exiting University System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()