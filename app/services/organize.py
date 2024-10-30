from typing import Optional

from app.utils.send_discord_message import SendDiscordMessage

class Organize:

    def bubble_sort(self, numbers: list[float]) -> Optional[list[float]]:
        length = len(numbers)

        if length <= 1:
            return numbers

        for i in range(length - 1):
            swapped = False

            for j in range(length - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    swapped = True

            if not swapped:
                break

        return numbers