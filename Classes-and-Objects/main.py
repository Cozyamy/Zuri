class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name) 
        self.age = int(age)
        self.track = list(tracks)
        self.score = float(score)
        print("Details of new student")

    def change_name(self, n_name):
        self.name = n_name
        print("name: ", self.name)

    def change_age(self, n_age):
        self.age = n_age
        print("age: ", self.age)

    def add_track(self, n_track):
        self.tracks = n_track
        print("tracks: ", self.tracks)

    def get_score(self):
        print("score: ", self)


Bob = Student("Bob", 26, ["FE","BE"],20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
