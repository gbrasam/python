from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def make_graph(df: pd.DataFrame) -> None:

    year = df.columns[1:]
    print(year)

    rows, cols = df.shape
    for i in range(rows):
        row = df.iloc[i]
        country = row["country"]
        period = year[1800:2051]
        population = row[1:]
        print(population.head())
        plt.plot(period, population, label=country)

    plt.legend()

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(period[::40])
    plt.show()


def main():
    """
    loads population dataset, filters
    and cleans data for Spain vs France,
    and displays the comparison from 1800 to 2050
    """

    try:
        df = load("../population_total.csv")
        if df is None:
            return 0

        subset = df[df["country"].isin(["Spain", "France"])]
        if subset.empty:
            raise ValueError("'Spain' or 'France' not found in the dataset")
        
        # print(subset.values[1])
        make_graph(subset)

        return 1

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Error: {error}")

    return 0


if __name__ == "__main__":
    main()
