# Date: 24/10/2018
# Alright dickheads im back to write some more incredible code. I've gone through
# and cleaned out all yesterdays unecessary comments (basically all of them, the
# remaining ones are prefixed with 'IMPORTANT') so I can do it all again.
# BTW: This code won't actually work yet because we need to split it up
# correctly across multiple files... which is hard because I'm trying to do this 
# as a journal type weird thing

class Person(object):

  """This is the base class for all people objects"""

  name = "Person"
  gender = "unknown"  
  interests = []

  traits = Traits("ENTJ-A", {"body" : [{"waist" : ['Leg', 'Leg']}]})


  def __init__(self, name, gender, traits, interests):

    self.name = name
    self.gender = gender
    self.interests = interests
    self.traits = traits

  def introduce(self):
    # IMPORTANT: Perhaps use the traits object to get a recommended greeting
    print(f"Hi!, My name is {self.name}")

  # Lol, I realised that I didn't finish implementing this yesterday so lets do that
  def get_date_of_birth(self):
    return "11/09/01" # We don't actually have this information so 9/11 works fine


  import random as rand
  class Traits(object):

    """This is an object for recording details of a person"""

    # IMPORTANT: Max of five greetings per category
    greetings = {
      "Positive" : [
        "Hi! My name is [name]",
        "Hello kind sir! I'm [name]",
      ],
      "Negative" : [
        "Fuck off you dirty filth",
        "Roses are red violets are blue, God made me pretty, what happened to you?",
        "Just found out you had an illness, I hope its nothing too trivial",
        "Some people were dropped on their heads as a child.. you must have been thrown at a wall",
      ]
    }

    def __init__(self, mbti, body):

      self.mbti = mbti
      self.body = body

    # I realised that this logic could be  better. Check yesterday's to see the change
    # from then to now
    def get_greeting(self, sentiment = "Positive"):
      index = rand.randint(0,5)

      return greetings[sentiment][index]

# Ok so before continuing let me explain what exactly the Dumb-person people factory is.
# Put in simplest terms, It's a dumb waste of time. The idea is to create a program thing
# that is capable of generating people. The end goal is for this project to be over complicated.
# I want genrated people to be randomly generated and have their own personalilties. Some will have
# 'dumb' hardcoded brains and others will have a neural network. They will have avatars genrated based
# on their traits and be able to talk nonsense.. possibly from my previously constructed random
# sentence generator. As for the 'overcomplicated' bit, we are going to be using a dumb project architecture
# reserved for big time software engineers who want to make it look like they know what they're doing.
# We split our code across multiple modules and bloat it wherever possible. This will include using 'factory'
# classes instead of just writing useful constructors.
  class skeleton_factory(object):

    """Because writing JSON structures is hard"""

    species_types = {
        "Human" : {
            "Torso" : {
                "Waist" : ['Leg', 'Leg'],
                "Neck" : 'Head',
                "Shoulders" : ['Arm', 'Arm'],
            }
        },
        "Dog" : {
            "Torso" : {
                "Neck" : {
                    "Head" : ['Ear', 'Ear'],
                },
                "Limbs" : ['Leg', 'Leg', 'Leg', 'Leg', 'Penis']
            }
        }
    }

    # This function will return a JSON skeleton based off some predefined types
    def get_skeleton(species = "human"):

      # I think we should make a class solely for getting permission to build stuff
      # but it always returns true. After all, it is what the 'professionals' do.
      if species in species_types:
        return species_types[species]

    # Allows the user to define their own species types that can be used system wide
    def add_custom_template(name, template):

      # Some sneaky error handling in case a species with that name already exists.
      if name not in species_types:
          species_types[name] = template
          return true
      else:
          # ValueError because I could not be fucked to define my own exception type
          raise ValueError("A template is is already defined for: " + name)
          return false

    # I should probably also add a JSON formatter because that means we can use the
    # templates more dynamically, but tbh, I can't be fucked to do that right now
    # Lol, its 123 lines and currently does nothing. Yet i could add like 3 more and it
    # would suddenly do stuff
