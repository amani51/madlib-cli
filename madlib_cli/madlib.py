import re

a= '''
**************************************
**    Welcome to the MadLib game!   **
**    Feel free to be crazy :p      **
**    
**    Add your crazy words to       **
**    create a funny story by       **
**    answering the question        **
**    and press enter...            **
**************************************
'''
def read_template(path):
    '''
    A function that takes in a path to text file 
    and returns a stripped string of the file's contents. 
    '''
    with open(path) as f:
        return f.read()
    # try:
    #     with open(path) as f:
    #         return f.read()
    # except FileNotFoundError as err:
    #     print("{} is invalid".format(path))
        
    

def parse_template(z):
    '''
    A function that takes in a template string and returns a string with language parts removed and a separate tuple of those language parts.
    '''
    try:
        match=re.findall(r'{.*?}',z)
        for i in range(len(match)):
            match[i]=match[i].replace("{","")
            match[i]=match[i].replace("}","")
            z=z.replace(match[i],"")
        match=tuple(match)
        return z,match
    except Exception as err:
        print("Say hello for a new error >_< => {}".format(err))



def merge(str1,values):
    '''
    function takes two arguments ; one is str with empty curly brackets,
    and the values that will be inside the curly bracket.
    and return the string with values instead of empty curly brackets.

    '''
    try:
        return str1.format(*values)
    except Exception as err:
        print("Say hello for a new error >_< => {}".format(err))   


def parse_template_stripped(file_content):
    '''
    A function that return the string with values instead of empty curly brackets.
    '''
    try:
        return parse_template(read_file)[0]
    except Exception as err:
        print("Say hello for a new error >_< => {}".format(err))


def parse_template_parts(list_of_words):
    '''
    A function that loops through a list of words, and for each iteration asks a user to add a word regarding the specific input word and appends it into a list, and returns the tuple of this list.
    '''
    try:
        x=[]
        for i in range(len(list_of_words)):
            x.append(input (list_of_words[i]+" => "))
        return tuple(x)
    except Exception as err:
        print("Say hello for a new error >_< => {}".format(err))


def write_story(story):
    '''
    A function that writes story into file ,and return the content of this file.
    '''
    try:
        with open('assets/make_me_a_video_game_output.txt', 'w') as f:
            story_content=f.write(story)  
        return story_content
    except Exception as err:
        print("Say hello for a new error >_< => {}".format(err))


if __name__=="__main__":
    print(a)
    # read_file=read_template("assets/make_me_a_video_game_template.txt")
    read_file=read_template("assets/dark_and_stormy_night_template.txt")
    template,words=parse_template(read_file)
    required_words=parse_template_parts(words)
    crazy_story=merge(template,required_words)
    output_game=write_story(crazy_story)
    print("*********************************")
    print("Your crazy story is as follows :p")
    print("*********************************")
    print(read_template("assets/make_me_a_video_game_output.txt"))
