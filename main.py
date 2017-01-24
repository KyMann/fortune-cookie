#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
def getRandomFortune():
    #select from a list of fortunes
    fortunes = [
    "I see much code in your future",
    "Consider eating more fortune cookies",
    "You have tamed the mighty Python, now you must free it onto the Great Spider's Web!",
    "You would be great as a TI",
    "A feather in the hand is better than a bird in the air",
    "A friend asks only for your time not your money.",
    "A new perspective will come with the new year",
    ]
    #randomley select a fortune
    index = random.randint(0, len(fortunes)-1)
    return(fortunes[index])

class MainHandler(webapp2.RequestHandler):
    '''home page
    '''
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        
        fortune = "<strong>" +getRandomFortune() +"</strong>"
        fortune_sentence = "Your fortune is: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"
        
        lucky_number = "<strong>" + str(random.randint(1,100)) +"</strong>"
        number_sentence ='Your lucky number: ' + (lucky_number) 
        number_paragraph = "<p>" + number_sentence + "</p>"
        
        cookie_again_button = "<a href='.'><button>Another Cookie Plz!</button></a>"
        
        content = header + fortune_paragraph +number_paragraph +cookie_again_button
        self.response.write(content)

class LoginHandler(webapp2.RequestHandler): #why bother deleting a good example?
    '''login page
    '''
    def get(self):
        self.response.write("Thanks for trying to log in!")
        
app = webapp2.WSGIApplication([ #app is an instance of this premade class that takes in routes as arguments
    ('/', MainHandler),
    ('/login', LoginHandler) #it's not hurting anything by staying!
], debug=True)
 