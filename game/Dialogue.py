
import pygame
import re
import sys , string

#Dictionnary of the the character stats
#labels is a dictionnary of the # marks in the dialogue
#functions is a dictionnary of the functions encountered in the piece of text found
#sex is the gender of the player it changes he/she into the right sex 
dict = {'cha': 1, 'int': 5}
labels = {}
functions = {}
sex = "he"
class dialogue_system:

    #populating_dictionnary is first used to make a dictionnary of the # marks 
    #The format is mark:line it is at
    def populating_dictionnary(self):
        file = open("Sample Dialogue.txt")
        for num, line in enumerate(file,1) :
            if line [0] == '#':
                words = line.split()
                labels[words[1]] = num
                
                      

    def speech(self, start=0):
        file = open("Sample Dialogue.txt")
        file = list(file)
        check = 0
        check1 = 0
        check2 = 0
        num_choices = 1
        choices = {}
        for line in file[start:]:
           
            #if # is found then it is a block of text
            if line[0]== '#': 
                check +=1
            #if two are found then it is the end of the block so break
            if check == 2: 
                break
            
            #if ! is found then a function is used, create a "functions" will store the function as index and the function and its arguments as keys ex: function:function(args)
            #if jump is found no need to store it as it is a dialogue based function to jump from one block of text to another but it will break out to allow for the jump
            if line [0] == '!':
                word = line.split()
                word[1] = word[1].replace(":", "")
                if word[1] == 'jump':
                    spec= dict[word[2]]
                    word[4] = word[4].replace(",", "")
                    comparison = int(word[4])
                    if spec < comparison:
                        jump= labels[word[5]]
                        check2 = 1
                        break
                                     
                else :
                    if len(word)>2:
                        args = line.split(':')
                        args[1] = args[1].replace(" ", "")
                        args[1] = args[1].replace("\n", "")
                        functions[word[1]]  = word[1] + '(' + args[1] + ')'                
                    else :
                        functions[word[1]]  = word[1] + '()'
                        
            #if % is found it means it corresponds to dialogue by the character or the narrator. (Once dialogue is displayed to make it go on press "enter")
            #depending on the sex of the player he/she will be replaced with the right one.
            #the input() line can be taken out and replaced by the commented out line below it. Input() corresponds to an "Enter" press in the command line while the other corresponds to any key press in pygame.
            #the print lines need to be replaced by the equivalent for pygame 
            if line [0] == '%':
                sentence = line.split()
                text = line.split('"')
                if sex == "she":
                    text[1] = text[1].replace("he/she", "she")
                else:
                    text[1] = text[1].replace("he/she", "he")
                name = line.split()
                name = name[1]
                name = name.replace("(", "")
                name = name.replace(")", "")
                if len(sentence[1]) < 3:
                    print("Narrator\n" +  text[1])
                    input()
                    #while (pygame.event.wait().type != KEYDOWN): pass


                else:
                    print (name + "\n" + text[1])
                    input()
                    #while (pygame.event.wait().type != KEYDOWN): pass

            #Variable used to see a choice block was entered
            if line[0] == '*':
                check1 += 1 
            #Parses for the different choices and prints them out. Except for the ones that require a specific level of stat that isn't met.
            #Print statements also need to be printed as their pygame equivalent 
            #The way the choice selection works is by entering the number that corresponds to the choice wanted (starts at 1)
            if line[0] == '+':
                sentence = line.split()
                text = line.split('"')
                if len(sentence[1]) != 2: 
                    spec=sentence[1].replace("(", "")
                    magn=sentence[3].replace(")", "")
                    
                    comparison = dict[spec]
                    if comparison > int(magn):
                        #Assign normal color
                        print(text[1])
                        dest = line.split('>')
                        length = len(dest) -1
                        dest[length] = dest[length].replace('\n', "")
                        dest[length] = dest[length].replace(' ', "")

                        choices[num_choices] = dest[length]
                        num_choices += 1
                        
                        
                    else:
                        #Assign grey or dont show 
                        print("NOT OK")
                else:
                    #Assign normal color
                    print(text[1])
                    
                    dest = line.split('>')
                    dest[1] = dest[1].replace('\n', "")
                    dest[1] = dest[1].replace(' ', "")
                    choices[num_choices] = dest[1]
                    num_choices += 1
        #breaks in the code lead here. The first one is for choices the second one is in case of jump functions encountered.
        #Uncommenting the block below should make the pygame input work allowing up to 6 choices. If done so the next 4 lines can be deleted as they are for command line (from usr_input to print("done"))           
        if check1 == 1:       
            #while (pygame.event.wait().type != (KEYDOWN and (event.key == K_1 or event.key == K_2 or event.key == K_3 or event.key == K_4 or event.key == K_5 or event.key == K_6))): pass
            #if event.key == K_1:
            #    usr_input = 1
            #if event.key == K_2:
            #    usr_input = 2
            #if event.key == K_3:
            #    usr_input = 3
            #if event.key == K_4:
            #    usr_input = 4
            #if event.key == K_5:
            #    usr_input = 5
            #if event.key == K_6:
            #    usr_input = 6
            
            usr_input = int(input("choose"))            
            while  (int(usr_input) not in choices):
                usr_input = int(input("keep choosing"))
            print("done")
            
            jump_to = choices[usr_input]
            #gives the line to jump to
            jump = labels[jump_to]
            self.speech(jump-1)
        
        if check2 == 1:
            self.speech(jump-1)
                
        
        
        
