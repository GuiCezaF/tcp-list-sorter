import random
import pytest
from app.services.organize import Organize

class TestOrganize:
    """Teste para verificar o comportamento do método de ordenação da classe Organize."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Configuração inicial para instanciar Organize antes de cada teste."""
        
        self.organize = Organize()
    
    def _gerar_array_numeros(self, max_numeros=10, minimo=1, maximo=100):
        """Gera uma lista de números inteiros e decimais aleatórios."""
        quantidade = random.randint(1, max_numeros)
        array = [
            random.choice([random.randint(minimo, maximo), round(random.uniform(minimo, maximo), 2)])
            for _ in range(quantidade)
        ]
        return array
    
    @pytest.mark.parametrize("max_numeros", [5, 10, 15])
    def test_bubble_sort_varios_tamanhos(self, max_numeros):
        """Testa o método bubble_sort com arrays de tamanhos variados."""
        
        numbers = self._gerar_array_numeros(max_numeros)
        ordered = self.organize.bubble_sort(numbers)
        assert ordered == sorted(numbers), f"Falha na ordenação com array: {numbers}"

    def test_bubble_sort_array_vazio(self):
        """Testa se o método bubble_sort retorna uma lista vazia quando recebe uma lista vazia."""
        
        assert self.organize.bubble_sort([]) == []
    
    def test_bubble_sort_lista_ja_ordenada(self):
        """Testa se o método bubble_sort retorna uma lista já ordenada corretamente."""
        
        numbers = [1, 2, 3, 4, 5]
        assert self.organize.bubble_sort(numbers) == numbers
    
    def test_bubble_sort_valores_duplicados(self):
        """Testa se o método bubble_sort ordena corretamente uma lista com valores duplicados."""
        
        numbers = [4, 2, 3, 2, 1, 4]
        assert self.organize.bubble_sort(numbers) == sorted(numbers)
