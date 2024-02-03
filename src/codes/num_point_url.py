class num_point_url:
    def __init__(self, df):
        self.df = df
        # print(self.df)

    def print_num(self):
        point_counts = [url.count('.') for url in self.df]

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(point_counts)} puntos")
        print(f"Máximo: {max(point_counts)} puntos")
        print(f"Promedio: {sum(point_counts) / len(point_counts):.2f} puntos")

