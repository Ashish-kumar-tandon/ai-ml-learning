import pandas as pd

data = {
    "name": ["Aman", "Riya", "Karan", "Sneha", "Rahul", "Priya", "Arjun", "Neha",
             "Vikash", "Anjali", "Rohit", "Pooja", "Aditya", "Simran", "Manish"],

    "age": [22, 25, None, 28, 24, None, 30, 26, 23, 29, None, 27, 31, 24, 28],

    "gender": ["Male", "Female", "Male", None, "Male", "Female", "Male", "Female",
               None, "Female", "Male", "Female", "Male", None, "Male"],

    "salary": [25000, 32000, 28000, None, 30000, 35000, None, 29000,
               27000, None, 40000, 33000, 45000, 31000, None]
}

df = pd.DataFrame(data)

# # 1. First 5 rows
# print("First 5 rows of the DataFrame:")
# print(df.head())

# # 2. Last 5 rows
# print("Last 5 rows of the DataFrame:")
# print(df.tail())

# # 3. Complete information
# print("Complete information of the DataFrame:")
# print(df.info())

# # 4. Statistical summary
# print("Statistical summary of the DataFrame:")
# print(df.describe())

# # 5. Shape of DataFrame (rows, columns)
# print("Shape of the DataFrame (rows, columns):")
# print(df.shape)

# # 6. Column names
# print("Column names:")
# print(df.columns)

# # 7. Data types of each column
# print("Data types of each column:")
# print(df.dtypes)


# # 8. Check missing values in each column
# print("Missing values in each column:")
# print(df.isnull().sum())


# Handling Null Values

# # 1. Using dropna() to remove rows with any missing values
# print("DataFrame after removing rows with any missing values:")
# print(df.dropna())

# 2. Filling missing values with a specific value
# print("DataFrame after filling missing values with specific values:")
# print(df.fillna(0))

# # 3(a). Filling missing values with the mean age
# mean_age = df['age'].mean()
# df['age'] = df['age'].fillna(mean_age)
# print("DataFrame after filling missing values in 'age' column with mean age:")
# print(df)

# # 3(b). Filling missing values with the median salary
# median_salary = df['salary'].median()
# df['salary'] = df['salary'].fillna(median_salary)
# print("DataFrame after filling missing values in 'salary' column with median salary:")
# print(df)

# # 3(c). Filling missing values with the mode
# gender_mode = df['gender'].mode()[0]
# df['gender'] = df['gender'].fillna(gender_mode)
# print("DataFrame after filling missing values in 'gender' column with mode:")
# print(df)

# 9. Check for duplicate rows

# Handling Duplicate Values