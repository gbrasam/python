import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    load a CSV dataset from the given path
    prints the dataset dimensions and returns the loaded DataFrame
    returns None if the file cannot be loaded
    """

    try:
        if not path:
            raise ValueError("empty path")

        if not path.lower().endswith(".csv"):
            raise ValueError("invalid file format")

        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")

        return df

    except ValueError as error:
        print(f"Error: {error}")

    except (FileNotFoundError,
            PermissionError,
            IsADirectoryError) as error:
        print(f"File error: {error}")

    except pd.errors.ParserError as error:
        print(f"CSV error: {error}")

    except Exception as error:
        print(f"Error: {error}")

    return None
