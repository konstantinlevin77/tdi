from colorama import Fore

def done_command(args):
    pass

def undone_command(args):
    pass

def add_command(args):
    pass

def remove_command(args):
    pass

def exit_command(args):
    pass

interpreter_commands = {
    "done":done_command,
    "undone":undone_command,
    "add":add_command,
    "remove":remove_command,
    "exit":exit_command
}

def run_open_interpreter():
    while True:

        raw_command = input(Fore.YELLOW+"Type your command: "+Fore.RESET)
        command,args = raw_command.split()[0],raw_command.split()[1:len(raw_command.split())]

        command_as_function = interpreter_commands.get(command)

        if command_as_function is None:
            print(Fore.CYAN+f"There is no command called {command}")

        else:
            command_as_function(args)
        
        