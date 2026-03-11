from colorama import init

from cmd_chat.client.config import COLORS
from cmd_chat.client.core.abs.abs_renderer import ClientRenderer

init()


class DefaultClientRenderer(ClientRenderer):
    def print_message(self, message: str) -> str:
        """generating string with message in required format"""
        # split only on the first ':' to keep message contents intact
        parts = message.split(":", 1)
        if parts[0] == self.username:
            return COLORS["my_username_color"] + parts[0] + ": " + parts[1] + COLORS["text_color"]
        return parts[0] + ": " + parts[1] + COLORS["text_color"]

    def clear_console(self):
        # ANSI escape sequence to clear screen and move cursor to top left
        print("\033[H\033[2J", end="", flush=True)

    def print_ip(self, ip: str) -> str:
        return "IP: " + COLORS["ip_color"] + ip + COLORS["text_color"]

    def print_username(self, username: str) -> str:
        # Username label + colored username
        return "USERNAME: " + COLORS["username_color"] + username + COLORS["text_color"]

    def print_chat(self, response) -> None:
        for i, msg in enumerate(response["messages"]):
            actual_message = self._decrypt(msg)
            if i == 0:
                for user in response["users_in_chat"]:
                    print(self.print_ip(user.split(",")[0]))
                    print(self.print_username(user.split(",")[1]))
                print("Write 'q' to quit from chat")
                print(f"\n{self.print_message(actual_message)}")
            else:
                print(f"{self.print_message(actual_message)}")
