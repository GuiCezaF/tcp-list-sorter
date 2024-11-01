from typing import List
from app.utils.send_discord_message import SendDiscordMessage

class Organize:
    def bubble_sort(self, numbers: List[float]) -> List[float]:
        """
        Ordena uma lista de números utilizando o algoritmo de bubble sort.

        Args:
            numbers (List[float]): Lista de números a ser ordenada.

        Returns:
            List[float]: Lista de números ordenada em ordem crescente.
        """
        
        if not all(isinstance(x, (int, float)) for x in numbers):
            raise ValueError("A lista deve conter apenas valores numéricos.")
        
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
