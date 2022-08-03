#!/usr/bin/python3
"""
Command line interpreter
"""
from models.base_model import BaseModel
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command line interpreter
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """ Creates and saves a new instance of BaseModel"""
        if args == " " or args == "":
            return
        print(type(args))
        arg_list = args.split()
        print("The argument is of length {}".format(len(arg_list)))
        if len(arg_list) != 1:
            print("** class name is missing **")
            return
        try:
            model = BaseModel()
            print(model.id)
        except:
            print("** class name doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

