import pandas as pd

# for formatting purposes
def print_selection(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

# function to load out dataframe
def load_data(filepath):
    df = pd.read_csv(filepath)
    print('Successfully loaded data from: ' + filepath)
    return df

# function to show basic info about the dataframe
def show_basic_info(df):
    print_selection("DATAFRAME INFO")
    print(df.info())

# function to show missing values in the dataframe
def missing_values(df):
    missing = df.isnull().sum()
    return missing

def show_data_review(df):
    print_selection("DATA VALUES REVIEW")   

    total_missing = missing_values(df).sum()

    if total_missing == 0:
        print("No missing values found in the dataset.")
    else:
        print('A. MISSING VALUES PER COLUMN:')
        print(missing_values(df))
        print('\nB. TOTAL MISSING VALUES: ' + str(missing_values(df).sum()))

def analyze_features(df):
    print_selection("LABEL DISTRIBUTION")
    
    label_counts = df['label'].value_counts()

# analyze text features
def analyze_text_features(df):
    print_selection("TEXT FEATURE STATISTICS")

    text_length = df['text'].str.len()
    word_count = df['text'].str.split().apply(len)

    print('Average character length: ' + str(text_length.mean()))
    print('Average word count: ' + str(word_count.mean()))
    print('Shortest word count: ' + str(word_count.min()))
    print('Longest word count: ' + str(word_count.max()))

# continue tomorrow: analyze_numerical features

# main function for testing
def main():
    df = load_data("data/cyberbullying_dataset_1000.csv")
    show_basic_info(df)
    show_data_review(df)
    analyze_features(df)
    analyze_text_features(df)

if __name__ == "__main__":
    main()