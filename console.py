#!/usr/bin/python3
"""HBNBCommand Class"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand subclass Cmd. It uses inherited class
    attribute (prompt) to issue command on each iteration
    through inherited public method cmdloop().

    Arg:
        Cmd (super class): pass down its attributes and methods
        for subclass extends.

    """
    prompt = '(hbnb) '

    __supported_class = ['BaseModel']

    '''=============================================
            Hbnb interpreter commands section
        =========================================='''
    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF exit the program and through key strokes: Ctrl + D'''
        return True

    def do_create(self, line):
        '''
        create a new instance of BaseModel
        '''
        line = self.parseline(line)
        class_name = line[0]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in HBNBCommand.__supported_class:
            print('** class doesn\'t exit **')
        else:
            instance_obj = BaseModel()
            instance_obj.save()
            print(instance_obj.id)

    def do_show(self, line):
        '''Fetch all stored instance obj, select a particular
           by the given id and print its id to console
        '''
        line = self.parseline(line)
        class_name = line[0]
        id = line[1]

        if class_name is None:
           print('** class name missing **')
        elif class_name not in HBNBCommand.__supported_class:
            print('** class doesn\'t exist **')
        elif id == '':
            print('** instance id missing **')
        else:
            data = storage.all()
            new_dict = {}

            '''convert to dict: (Work in Progress but still buggy)'''
            for (key, value) in data.items():
                new_dict[key] = self.to_dict(value)

            for obj in data.values():
                print(data.values())
                if id == obj.id:
                    print(obj)
                    return
            print('** no instance found **')

    '''=============================================
            Overridden base class method section
        =========================================='''
    def emptyline(self):
        '''
        Override emptyline so that Empty line + Enter shouldn't
        execute either of previous cmd(s)
        '''
        return False

    def parseline(self, line):
        '''
        Override super parseline method to parse the agv from
        prompt and pass its result to any calling method.
        '''
        ret = super().parseline(line)
        return ret

    '''================================================
            Overridden docstring section
        ============================================='''
    def help_quit(self):
        print('Quit command to exit the program\n')

    def help_EOF(self):
        print('EOF exit the program\n')

    def help_all(self):
        print('all command fetches and prints all store data\n')

    def help_create(self):
        help_msg = '''
            create command creates a new instance of supported\n
            class name pass as parameter to create command. ex:\n
            create BaseModel\n
            And save the instance to storage file.\n
        '''
        print(help_msg)

    def help_show(self):
        help_msg = '''
            show command prints id of a particular instance obj\n
            of supported class name. It selects a particular obj\n
            to print through arguments: class name and id. ex:\n
            show BaseModel id
        '''
        print(help_msg)

    '''=========================================
            HBNBCommand public method
        ======================================'''
    def to_dict(self, instance_obj):
        return instance_obj.__dict__

if __name__ == '__main__':
    HBNBCommand().cmdloop()
