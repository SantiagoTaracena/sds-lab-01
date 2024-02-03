from urllib.parse import urlparse

class num_point_domain:
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
        
        point_counts  = []

        for domain in domain_names:
            # Cuenta el número de vocales en el nombre de dominio
            point_count = domain.count('.')
            point_counts.append(point_count)

        # print("\nNúmero de puntos en cada nombre de dominio:")
        # for i, count in enumerate(point_counts):
        #     print(f"Nombre de dominio {i+1}: {count} puntos")

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(point_counts )} puntos")
        print(f"Máximo: {max(point_counts )} puntos")
        print(f"Promedio: {sum(point_counts ) / len(point_counts ):.2f} puntos")

