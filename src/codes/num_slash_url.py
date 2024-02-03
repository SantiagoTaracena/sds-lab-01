class num_slash_url:
    def __init__(self, df):
        self.df = df
        # print(self.df)

    def print_num(self):
        slash_counts = [url.count('/') for url in self.df]

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(slash_counts)} barras")
        print(f"Máximo: {max(slash_counts)} barras")
        print(f"Promedio: {sum(slash_counts) / len(slash_counts):.2f} barras")

