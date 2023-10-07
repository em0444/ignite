# class RecommendedResourcesDatabase:
#     def __init__(self):
#         self.resources = {}

# class ToDoList:
#      def recommend_resources(self, study_topic):
#         resources = {
#             "Book recommendation": [
#                 "Book by Gayle Laackmann: Cracking the Coding Interview",
#                 "Book by Alex Xu: System Design Interview Part 1 and 2",
#                 "Book by Eric Giguere, John Mongan, and Noah Kindler: Programming Interviews Exposed",
#                 "Book by Steven S. Skiena: The Algorithm Design Manual",
#                 "Book by Adnan Aziz: Elements of Programming Interviews",
#                 "Book by Jon Bentley: Programming Pearls",
#                 "Book by Noel Markham: Java Programming Interview Exposed",
#                 "Book by Meenakshi & Kamal Rawat: Dynamix Programming for Coding Interviews",
#                 "Book by Adnan Aziz: Algorithms for Interview",
#                 "Book by Joe Celkos: SQL Puzzles & Answers",
#             ],
#         }

#         if study_topic in resources:
#             print(f"\nRecommended Resources for {study_topic}:")
#             for i, resource in enumerate(resources[study_topic], 1):
#                 print(f"{i}. {resource}")
#         else:
#             print("No recommendations available for this topic.")

# def main():
#     todo_list = ToDoList()
    
#     while True:
#         print("\nMenu:")
#         print("1. Information about Intervews")
#         print("2. Book Recommendations")
#         print("3. Interview Questions")
#         print("4. Hackathon Events")
#         print("5. Job Recommendations")
#         print("6. Quit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             print(f"The truth\n")
#             print("""Students preparing for coding interviews should be aware of several truths to help them navigate the process more effectively. 
#                     Remember that coding interviews are just one part of the job application process. While they are important, they are not the only 
#                     factor that determines your worth as a developer. Stay persistent, keep learning, and approach interviews as opportunities to showcase your skills and experience.
#                 """)
#         elif choice == "2":
#             study_topic = input("Enter your study topic: ")
#             todo_list.recommend_resources(study_topic)
#         elif choice == "6":
#             break
#         else:
#             print("Invalid choice. Please try again.")

class RecommendedResourcesDatabase:
    def __init__(self):
        self.resources = {}

    def add_resource(self, topic, resources):
        self.resources[topic] = resources

class ToDoList:
    def __init__(self):
        self.resource_db = RecommendedResourcesDatabase()

    def recommend_resources(self, study_topic):
        if study_topic in self.resource_db.resources:
            print(f"\nRecommended Resources for {study_topic}:")
            for i, resource in enumerate(self.resource_db.resources[study_topic], 1):
                print(f"{i}. {resource}")
        else:
            print("No recommendations available for this topic.")

def main():
    todo_list = ToDoList()
    todo_list.resource_db.add_resource("Book recommendation", [
        "Book by Gayle Laackmann: Cracking the Coding Interview",
        "Book by Alex Xu: System Design Interview Part 1 and 2",
        "Book by Eric Giguere, John Mongan, and Noah Kindler: Programming Interviews Exposed",
        "Book by Steven S. Skiena: The Algorithm Design Manual",
        "Book by Adnan Aziz: Elements of Programming Interviews",
        "Book by Jon Bentley: Programming Pearls",
        "Book by Noel Markham: Java Programming Interview Exposed",
        "Book by Meenakshi & Kamal Rawat: Dynamix Programming for Coding Interviews",
        "Book by Adnan Aziz: Algorithms for Interview",
        "Book by Joe Celkos: SQL Puzzles & Answers",
    ])

    while True:
        print("\nMenu:")
        print("1. Information about Interviews")
        print("2. Book Recommendations")
        print("3. Interview Questions")
        print("4. Hackathon Events")
        print("5. Job Recommendations")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"The truth\n")
            print("""Students preparing for coding interviews should be aware of several truths to help them navigate the process more effectively. 
                    Remember that coding interviews are just one part of the job application process. While they are important, they are not the only 
                    factor that determines your worth as a developer. Stay persistent, keep learning, and approach interviews as opportunities to showcase your skills and experience.
                """)
        elif choice == "2":
            study_topic = input("Enter your study topic: ")
            todo_list.recommend_resources(study_topic)
        # elif choice == "3":
        elif choice == "4":
            todo_list.recommend_resources(study_topic)            
            print("Hackathon Events: ")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
