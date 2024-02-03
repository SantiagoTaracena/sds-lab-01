class num_dash_url:
    def __init__(self, df):
        self.df = df
        # print(self.df)

    def print_num(self):
        dash_counts = [url.count('-') for url in self.df]

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(dash_counts)} dash")
        print(f"Máximo: {max(dash_counts)} dash")
        print(f"Promedio: {sum(dash_counts) / len(dash_counts):.2f} dash")

