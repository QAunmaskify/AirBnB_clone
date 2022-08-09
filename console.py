#!/usr/bin/python3
"""HBNBCommand Class"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand extends Cmd. It inherits cmdloop method that
    gives prompt on every single interation.


    Attributes:
        prompt (str): name of command interpreter.

    """
    prompt = '(hbnb) '

    __supported_class = [
        'BaseModel',
        'User',
        'Place',
        'City',
        'Amenity',
        'Review',
        'State'
    ]

    '''=============================================
            Hbnb interpreter commands section
        =========================================='''
    def do_quit(self, line: str) -> bool:
        '''
        Quit command to exit the program.

        Args:
            line: Required for super class 'onecmd' method.

        Returns:
            True for success, False otherwise.

        '''
        return True

    def do_EOF(self, line: str) -> bool:
        '''
        EOF exit the program and through key strokes: Ctrl + D

        Args:
            line: Required for super class 'onecmd' method.

        Returns:
            True for success, False otherwise.

        '''
        return True

    def do_create(self, line: str) -> None:
        '''
        Create command creates a new instance of a class.

        Args:
            line: Input argument to create command.

        Returns:
            None

        '''
        line = self.parseline(line)
        class_name = line[0]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in HBNBCommand.__supported_class:
            print('** class doesn\'t exist **')
        else:
            instance = self.create(class_name)
            instance.save()
            print(instance.id)

    def do_show(self, line: str) -> None:
        '''
        Show command prints to a console a particular instance
        of a class.

        Args:
            line: Input argument to show command


        Returns:
            None
        '''
        line = self.parseline(line)
        class_name = line[0]
        class_id = line[1]

        if class_name is None:
            print('** class name missing **')
        elif class_name not in HBNBCommand.__supported_class:
            print('** class doesn\'t exist **')
        elif class_id == '':
            print('** instance id missing **')
        else:
            try:
                key = '{}.{}'.format(line[0], line[1])
                data = storage.all()[key]
                print(data)
            except KeyError:
                print('** no instance found **')

    def do_destroy(self, line) -> None:
        '''
        deletes an instance based on class name and id

        Args:
            line: destroy BaseModel 1234-1234-1234
        '''
        line = line.split(' ')
        if line[0] == '':
            print('** class name missing **')
        elif line[0] not in HBNBCommand.__supported_class:
            print('** class doesn\'t exist **')
        else:
            try:
                key = '{}.{}'.format(line[0], line[1])
                storage.all()[key]
                storage.destroy(class_name, class_id)
                storage.save()
            except KeyError:
                print('** no instance found **')
            except IndexError:
                print('** instance id missing **')

    def do_all(self, line) -> None:
        '''
        prints all string representation of all instance based or
        or not on the class name
        '''
        line = self.parseline(line)
        class_name = line[0]
        if class_name is not None and class_name\
                not in HBNBCommand.__supported_class:
            print('** class doesn\'t exist **')
        else:
            list_all = storage.all()
            if class_name:
                result = [str(list_all[obj]) for obj in
                          list_all if obj.startswith(class_name)]
            else:
                result = [str(list_all[obj]) for obj in list_all]
            print(result)

    def do_update(self, line) -> None:
        '''
        updates an instance based on class name and id
        by adding or updating attribute

        Args:
            line: update <class name> <id> <attribute name> "<attribute value>"
        '''
        line = line.replace('"', '')
        line = line.split(' ')
        if line[0] == '':
            print('** class name missing **')
        elif line[0] not in HBNBCommand.__supported_class:
            print('** class doesn\'t exist **')
        elif len(line) == 1:
            print('** instance id missing **')
        else:
            try:
                key = '{}.{}'.format(line[0], line[1])
                storage.all()[key]
                storage.update(*line)
                storage.save()
            except KeyError:
                print('** no instance found **')
            except IndexError:
                print('** instance id missing **')
            except TypeError:
                print('** value missing **')

    '''=============================================
            Overridden base class method section
        =========================================='''
    def emptyline(self) -> bool:
        '''
        Override emptyline to deactivate Empty line + Enter shouldn't
        being resolved to previous commands.

        Args:
            No arguments

        Returns:
            False for successful, True for otherwise
        '''
        return False

    def parseline(self, line: tuple) -> tuple:
        '''
        Override parseline method to parse the agv from
        prompt and pass its result to any calling method.

        Args:
            line: variable of length of tuple of string

        Returns:
            tuple of str.
        '''
        ret = super().parseline(line)
        return ret

    def default(self, line):
        """ Called on an input line when the command prefix is not recognised
        """
        args = line.replace(',', '')
        args = re.split(r'\.|\(|\)', args)
        class_name = args[0]
        method = args[1]
        if method == "all":
            self.do_all(line)
        elif method == 'count':
            print(len([k for k in storage.all().keys()
                  if k.startswith(class_name)]))
        elif method == "show":
            self.do_show(class_name + ' ' + args[2])
        elif method == 'destroy':
            self.do_destroy(class_name + ' ' + args[2])
        elif method == 'update':
            update_args = " ".join([class_name, args[2]])
            self.do_update(update_args)

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

    def help_destroy(self):
        print('Deletes an instance based on the class name and id\n')

    def help_update(self):
        print('Updates an instance based on the class name and id \
                by adding or updating attribute\n')

    '''=========================================
            HBNBCommand public method
        ======================================'''
    def to_dict(self, instance_obj):
        return instance_obj.__dict__

    def create(self, class_name):
        instance = None

        if class_name == 'BaseModel':
            instance = BaseModel()
        elif class_name == 'User':
            instance = User()
        elif class_name == 'Place':
            instance = Place()
        elif class_name == 'Amenity':
            instance = Amenity()
        elif class_name == 'City':
            instance = City()
        elif class_name == 'State':
            instance = State()
        elif class_name == 'Review':
            instance = Review()

        return instance


if __name__ == '__main__':
    HBNBCommand().cmdloop()
