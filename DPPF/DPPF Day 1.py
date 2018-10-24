# This is some random shit I wrote whilst I was highly tired
# I have no idea if it is even valid python, let alone whether or
# not it does anything. Programming is my zen at the moment. Just
# open a simple text editor with a nice color scheme and just write
# shit. Welcome to the dumb-person people factory (DPPF 1.0)


# Lets start by defining a person
class Person(object):

  """This is the base class for all people objects"""

  name = "Person"
  gender = "unknown"  # Check if this is a Politically correct default
                      # maybe use 'non-binary' instead...?
  interests = []

  # The default guy only has a torso and two legs coz im lazy
  traits = Traits("ENTJ-A", {"body" : [{"waist" : ['Leg', 'Leg']}]})

  # This is the init function. It is used to set up a new instance
  # of this object eg; my_person = Person("Nic", "Male..?", ["Cricket", "AFL"])
  # its black magic really. No one understands this shit. Fuck guido van rossum
  def __init__(self, name, gender, traits, interests):
    self.name = name
    self.gender = gender
    self.interests = interests
    self.traits = traits

  def introduce(self):
    # Perhaps use the traits object to get a recommended greeting
    print(f"Hi!, My name is {self.name}")

  # Why? Because why the fuck not. It may be helpful to have this function
  # at some point in the future
  def get_date_of_birth(self):


  # You may have noticed the use of a 'Traits' object in the previous class
  # This is the object we will define next. It should contain information
  # regarding personalilty and physical characteristics
  # BTW: We inherit from object because it looks cool
  import random as rand
  class Traits(object):

    """This is an object for recording details of a person"""

    # IMPORTANT: Max of five greetings per category
    greetings = {
      "Positive" : [
        "Hi! My name is [name]",
        "Hello kind sir! I'm [name]",
      ]
      "Negative" : [
        "Fuck off you dirty filth",
        "Roses are red violets are blue, God made me pretty, what happened to you?",
        "Just found out you had an illness, I hope its nothing too trivial",
      ]
    }

    # TODO: Maybe we could implement our own personality test. Types
    #  could be 'Happy', 'Smart', 'Inspiring' and 'Jew'

    def __init__(self, mbti, body):
      # BTW: 'mbti' means 'Myers-Briggs Type Identifier'. It is a standard
      # personalilty test used to assess someones characteristics. It categorises
      # you in one of 16 main personality types. For more info: www.16personalities.com
      self.mbti = mbti
      self.body = body

    def get_greeting(self, sentiment = "default"):
      if sentiment is "default":
        sentiment = "Positive"

      return greetings[sentiment][rand.randint(0,5)]


  # Next up. The skeleton builder. The traits class has a body feild. The body 
  # will be described in JSON format. To build these bodies concviniently we 
  # will make a static factory class
  class skeleton_factory(object):

    """
    I think ima leave it here for tonight guys. This idea is wild as fuck though. Im liking it.
    This could get pretty wild and there is a lot of room for addded functionalilty.
    """
