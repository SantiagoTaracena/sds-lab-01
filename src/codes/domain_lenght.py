from urllib.parse import urlparse

class domain_lenght:
    def __init__(self, df):
        self.df = df
        
    def print_paths(self):
        domain_names = []

        for url in self.df:
            parsed_url = urlparse(url)
            domain_name  = parsed_url.netloc

            # Verifica si hay un pathname antes de agregarlo a la lista
            if domain_name:
                domain_names.append(domain_name)

        print(domain_names)
        # existe = "?" in pathnames
        # print(existe)
        
        domain_lengths = [len(domain) for domain in domain_names]

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(domain_lengths)} caracteres")
        print(f"Máximo: {max(domain_lengths)} caracteres")
        print(f"Promedio: {sum(domain_lengths) / len(domain_lengths):.2f} caracteres")


