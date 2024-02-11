"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Librería necesaria para la obtención de la entropía del texto.
import math
from urllib.parse import urlparse

# Diccionario con las frecuencias oficiales.
official_frequency_analysis: dict[str, float] = {
    "a": 0.1253,
    "b": 0.0142,
    "c": 0.0468,
    "d": 0.0586,
    "e": 0.1368,
    "f": 0.0069,
    "g": 0.0101,
    "h": 0.0070,
    "i": 0.0625,
    "j": 0.0044,
    "k": 0.0002,
    "l": 0.0497,
    "m": 0.0315,
    "n": 0.0671,
    "ñ": 0.0031,
    "o": 0.0868,
    "p": 0.0251,
    "q": 0.0088,
    "r": 0.0687,
    "s": 0.0798,
    "t": 0.0463,
    "u": 0.0393,
    "v": 0.0090,
    "w": 0.0001,
    "x": 0.0022,
    "y": 0.0090,
    "z": 0.0052,
}

# Función que obtiene la entropía de un texto.
def text_entropy(text: str) -> float:

    # Limpieza y conversión del texto a minúsculas.
    text: str = text.lower()

    # Probabilidades de cada letra del texto.
    local_probabilities: list[float] = [(text.count(char) / len(text)) for char in set(text)]
    global_probabilities: list[float] = [(official_frequency_analysis.get(char, 0.0001)) for char in set(text)]

    # Obtención de la entropía total del texto.
    text_entropy_value: float = sum([(probability * math.log2(probability / q_probability)) for probability, q_probability in zip(local_probabilities, global_probabilities)])

    # Retorno de la entropía total del texto.
    return text_entropy_value

def get_domain_entropy(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return text_entropy(domain)
