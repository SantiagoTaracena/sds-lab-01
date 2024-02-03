class url_lenght:
    def __init__(self, df):
        self.df = df
        # print(self.df)

    def print_urls(self):
        url_lengths = [len(url) for url in self.df]

        print("\nEstadísticas generales:")
        print(f"Mínimo: {min(url_lengths)} caracteres")
        print(f"Máximo: {max(url_lengths)} caracteres")
        print(f"Promedio: {sum(url_lengths) / len(url_lengths):.2f} caracteres")
