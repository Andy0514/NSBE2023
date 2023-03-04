import cohere
from cohere.classify import Example
co = cohere.Client('yiOWD4KfXSiayGiim2MRmZRUvGsbdEFOY5QaCQ1Z') # This is your trial API key

inputs = ["This item was broken when it arrived", "This item broke after 3 weeks"]

examples = [
    Example("The order came 5 days early", "positive"), 
    Example("The item exceeded my expectations", "positive"), 
    Example("I ordered more for my friends", "positive"), 
    Example("I would buy this again", "positive"), 
    Example("I would recommend this to others", "positive"), 
    Example("The package was damaged", "negative"), 
    Example("The order is 5 days late", "negative"), 
    Example("The order was incorrect", "negative"), 
    Example("I want to return my item", "negative"), 
    Example("The item\'s material feels low quality", "negative")
]

response = co.classify(
  model='large',
  inputs=inputs,
  examples=examples)
print('The confidence levels of the labels are: {}'.format(response.classifications))