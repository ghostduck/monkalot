"""Commands: "!block on/off"."""
from bot.commands.command import Command
from bot.utilities.permission import Permission


class PyramidBlock(Command):
    """Send a random SMOrc message."""

    perm = Permission.Moderator
    responses = {}

    def __init__(self, bot):
        """Initialize variables."""
        self.responses = {}

    def match(self, bot, user, msg, tag_info):
        """Match if command is !block on or !block off."""
        return msg == "!block on" or msg == "!block off"

    def run(self, bot, user, msg, tag_info):
        """Set block."""
        self.responses = bot.responses["PyramidBlock"]
        if msg == "!block on":
            if not bot.pyramidBlock:
                bot.pyramidBlock = True
                bot.write(self.responses["block_activate"]["msg"])
            else:
                bot.write(self.responses["block_already_on"]["msg"])
        elif msg == "!block off":
            if bot.pyramidBlock:
                bot.pyramidBlock = False
                bot.write(self.responses["block_deactivate"]["msg"])
            else:
                bot.write(self.responses["block_already_off"]["msg"])
