import psycopg2

# Establish connection to PostgreSQL
mydb = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="admin",
    database="videoanalysis"
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

# Call create_table() function to create the table
#create_table()

# Close the database connection

# x={
#     'Duration': 600,
#     'Total Words': 1500,
#     'Filler Words Per Minute': 120,
#     'average words per minute': 100,
#     'fillers per minute': 20,
#     'average fillers per minute': 15,
#     'eye contact percentage': 75.5,
#     'num_pauses': 10,
#     'total_pause_time': 30.5,
#     'soft voices %': 20,
#     'medium voices %': 50,
#     'high voices %': 30
# }
# print(x)
# insert_data(x)
# mydb.close()