import openai
class StoryGenerator():
    """
    Base class for te story generator
    Args:
        *args (list): list of arguments
        **kwargs (dict): dict of keyword arguments
    Attributes:
        self
    """

    def __init__(self, *args, **kwargs):
        print("initializing Generator")
        models = openai.Model.list()
        print("available models: " + models)

    def generate_story(self):
        """
        Function.
        """
        print("Testing to see if the story generator works.")