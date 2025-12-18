from adventure.utils import read_events_from_file
import random

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console = Console()


def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."


def left_path(event):
    return "You walk left. " + event


def right_path(event):
    return "You walk right. " + event


def show_intro():
    title = Text("Adventure", style="bold magenta")
    body = Text("You wake up in a dark forest.\nYou can go left or right.", style="white")
    console.print(Panel(body, title=title, border_style="magenta"))


def show_result(result: str):
    console.print(Panel.fit(result, border_style="cyan"))


if __name__ == "__main__":
    events = read_events_from_file("events.txt")

    show_intro()

    while True:
        choice = Prompt.ask(
            "[bold]Which direction do you choose?[/bold] [dim](left/right/exit)[/dim]",
            choices=["left", "right", "exit"],
            default="left",
        ).strip().lower()

        if choice == 'exit':
            console.print("[red]You decide to leave the forest. Goodbye![/red]")
            break #forgot to add a break
            
        show_result(step(choice, events))
