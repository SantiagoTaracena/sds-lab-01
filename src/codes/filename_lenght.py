from urllib.parse import urlparse
import os

class filename_lenght:
    def __init__(self, df):
        self.df = df
        
    def print_paths(self):
        file_names = []

        for url in self.df:
            parsed_url = urlparse(url)
            path   = parsed_url.path
            file_name = os.path.basename(path)


            # Verifica si hay un pathname antes de agregarlo a la lista
            if file_name and "." in file_name:
                file_names.append(file_name)

        print(file_names)
        # existe = "?" in pathnames
        # print(existe)
        
        file_lengths = [len(file) for file in file_names]

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(file_lengths)} caracteres")
        print(f"Máximo: {max(file_lengths)} caracteres")
        print(f"Promedio: {sum(file_lengths) / len(file_lengths):.2f} caracteres")


