# create a class (wow!)
class me:
    # constructor function can reference self like a weirdo who talks about themselves in 3rd person
    def __init__(self, in1="John", in2="25", in3="Blue Collar Worker"):
        self.name = in1
        self.age = in2
        self.job = in3
        self.past_jobs = []
    # classes can have functions
    def intro(self):
        return f"Hi my name is {self.name}. I am {self.age}. I do {self.job}. English good. :D"
    # adding new info
    def add_job(self, new_job):
        self.past_jobs.append(new_job)
# make an object with blank parameters (we filled in definition)
blank_object = me()
print(blank_object.intro())
# make an object with actual info
me_object = me("A", 18, "teacher")
print(me_object.name, me_object.age, me_object.job)
# adding new info through methods
me_object.add_job("Referee")
print(me_object.past_jobs)

# inheritance - creating new class with all of old class properties
class me2(me):
    def __init__(self, a="John", b="25", c="hepl", d="sure"):
        # inherit first 3 attributes from parent
        super().__init__(a, b, c)
        # new attribute (wow so cool)
        self.children = d
    def new_intro(self):
        return f"Hi my name is {self.name}. I am {self.age}. I do {self.job}. I would like {self.children} kids."
# establish child
child = me2("Josh", "3", "Build Tanks", "Lots")
# playing with new method in child
print(child.new_intro())