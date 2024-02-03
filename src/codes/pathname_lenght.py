from urllib.parse import urlparse

class pathname_lenght:
    def __init__(self, df):
        self.df = df
        
    def print_paths(self):
        pathnames = []

        for url in self.df:
            parsed_url = urlparse(url)
            pathname = parsed_url.path

            # Verifica si hay un pathname antes de agregarlo a la lista
            if pathname and pathname != "/":
                pathnames.append(pathname)

        print(pathnames)
        # existe = "?" in pathnames
        # print(existe)
        
        path_lengths = [len(path) for path in pathnames]

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(path_lengths)} caracteres")
        print(f"Máximo: {max(path_lengths)} caracteres")
        print(f"Promedio: {sum(path_lengths) / len(path_lengths):.2f} caracteres")



