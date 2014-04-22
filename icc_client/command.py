# Internet Chess Server (ICS) Bot Template
# Copyright 2011 Ryan Chiu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

class Command:

    # Commands are stored in a list; each will have its own function
    VALID_COMMAND_LIST = ['add', 'your', 'own', 'command', 'list', 'here', 'plz']

    def __init__(self): pass

    # Tells (strings) sent to the bot will be split. They will then be passed
    # in as "ommand"(split_str[0]), and "args", as a list of the remaining
    # text in the tell.
    #
    # Returns the response to the command. (ex. return player info if "finger"
    # is passed in).
    def parse_tell(self, command, args):
        if hasattr(self, command) and command in self.VALID_COMMAND_LIST:
            return command(self, args)
        else: return "\""+command+"\" is either not a valid command, or \
didn't have the correct number of arguments supplied to it."
    
    ###############################################################################
    #                              COMMAND METHODS                                #
    ###############################################################################

    # IMPORTANT! Make sure to name your methods the same name as the command
    # for all of this to work correctly! For example, if you have a "vars" command,
    # please define a method named "vars(self, args)".

    # [ methods go here :-) ]
