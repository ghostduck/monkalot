"""Commands: "!oralpleasure on/off"."""

from bot.commands.command import Command
from bot.utilities.permission import Permission


class Oralpleasure(Command):
    """Turn oral pleasure on and off."""

    perm = Permission.User

    def __init__(self, bot):
        """Initialize variables."""
        self.active = False
        self.responses = {}

    def match(self, bot, user, msg):
        """Match if the bot is tagged."""
        cmd = msg.lower()
        return (cmd.startswith('!oralpleasure on') or cmd.startswith('!oralpleasure off'))

    def run(self, bot, user, msg):
        """Define answers based on pieces in the message."""
        self.responses = bot.responses["Oralpleasure"]
        cmd = msg.lower()

        if cmd.startswith('!oralpleasure on'):
            if self.active:
                bot.write(self.responses["op_already_on"]["msg"])
            else:
                self.active = True
                bot.write(self.responses["op_activate"]["msg"])
        elif cmd.startswith('!oralpleasure off'):
            if self.active:
                self.active = False
                bot.write(self.responses["op_deactivate"]["msg"])
            else:
                bot.write(self.responses["op_already_off"]["msg"])

    def close(self, bot):
        """Turn off on shotdown or reload."""
        self.active = False