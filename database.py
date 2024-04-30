import mysql.connector

mydb = mysql.connector.connect(
    host=" 192.168.0.113",
    user="root",
    password="Siddhartha@1728",
    database='videoanalysis'
)

def insert_data(databasedata):
    insert_query = """
            INSERT INTO performance_metricsdata2 (
                Country_Code, Mobile_Number, Duration, Total_Words, Filler_Words_Per_Minute,
                Average_Words_Per_Minute, Fillers_Per_Minute,
                Average_Fillers_Per_Minute, Eye_Contact_Percentage,
                Num_Pauses, Total_Pause_Time, Soft_Voices_Percentage,
                Medium_Voices_Percentage, High_Voices_Percentage
            ) VALUES (
                %(Country_Code)s, %(Mobile_Number)s, %(Duration)s, %(Total_Words)s, %(Filler_Words_Per_Minute)s,
                %(Average_Words_Per_Minute)s, %(Fillers_Per_Minute)s,
                %(Average_Fillers_Per_Minute)s, %(Eye_Contact_Percentage)s,
                %(Num_Pauses)s, %(Total_Pause_Time)s, %(Soft_Voices_Percentage)s,
                %(Medium_Voices_Percentage)s, %(High_Voices_Percentage)s
            )
    """
    cursor = mydb.cursor()
    cursor.execute(insert_query, databasedata)
    mydb.commit()
    print("Data inserted successfully in db!")

def create_table():
    cursor = mydb.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS performance_metricsdata2 (
            Country_Code INT,
            Mobile_Number VARCHAR(15),
            Duration INT,
            Total_Words INT,
            Filler_Words_Per_Minute INT,
            Average_Words_Per_Minute INT,
            Fillers_Per_Minute INT,
            Average_Fillers_Per_Minute INT,
            Eye_Contact_Percentage FLOAT,
            Num_Pauses INT,
            Total_Pause_Time FLOAT,
            Soft_Voices_Percentage FLOAT,
            Medium_Voices_Percentage FLOAT,
            High_Voices_Percentage FLOAT,
            PRIMARY KEY (Country_Code, Mobile_Number)
        )
    """
    cursor.execute(create_table_query)
    mydb.commit()
    print("Table created successfully!")

# # Call create_table() function to create the table
#create_table()
# databasedata={
#     "Country_Code": 91,
#     'Mobile_Number':7207053174,
#     "Duration": 523,
#     "Total_Words": 387,
#     'Filler_Words_Per_Minute': 82,
#     'Average_Words_Per_Minute': 36,
#     'Fillers_Per_Minute': 32,
#     'Average_Fillers_Per_Minute': 5,
#     'Eye_Contact_Percentage': 96.6,
#     'Num_Pauses': 29,
#     'Total_Pause_Time': 99.56,
#     'Soft_Voices_Percentage': 13.47,
#     'Medium_Voices_Percentage': 47.32,
#     'High_Voices_Percentage': 57.32,
# }


# print(databasedata)

# insert_data(databasedata)
