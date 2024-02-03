from urllib.parse import urlparse

class num_vocals_domain:
    def __init__(self, df):
        self.df = df
        
    def print_num(self):
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
        
        vocal_counts = []

        for domain in domain_names:
            # Cuenta el número de vocales en el nombre de dominio
            vowel_count = sum(1 for char in domain if char.lower() in 'aeiou')
            vocal_counts.append(vowel_count)

        # print("\nNúmero de vocales en cada nombre de dominio:")
        # for i, count in enumerate(vocal_counts):
        #     print(f"Nombre de dominio {i+1}: {count} vocales")

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(vocal_counts)} vocales")
        print(f"Máximo: {max(vocal_counts)} vocales")
        print(f"Promedio: {sum(vocal_counts) / len(vocal_counts):.2f} vocales")

