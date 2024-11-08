import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman tree

def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

    return codes

# Frecuencias de los caracteres
char_freq = {
    'A': 5,
    'B': 12,
    'C': 35,
    'D': 3,
    'E': 8,
    'F': 14,
    'G': 21,
    'H': 1,
    'I': 39,
}

# Construir el árbol de Huffman
huffman_tree_root = build_huffman_tree(char_freq)

# Generar códigos de Huffman
huffman_codes = generate_codes(huffman_tree_root)

# Mostrar resultados
for char, code in huffman_codes.items():
    print(f"Carácter: {char}, Código: {code}")