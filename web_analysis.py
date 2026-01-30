import pandas as pd
#ingest data
df=pd.read_csv("event_attendance.csv")
#print(df.head(5))
#print(df.columns)
#print(df.shape)

#Data quality check

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.duplicated(subset=["event_id","attendee_email"]).sum())

#DEDUPLICATION

df_clean = ( df.sort_values(by="date_time").drop_duplicates(
    subset=["event_id","attendee_email"],keep="last").copy())
#print(df.shape)
#print(df_clean.shape)

#Registration count per event


event_attendees = (df_clean.groupby(["event_id","event_name"])
                   .agg(total_att=("attendee_email","count")))
ascen = event_attendees.sort_values("total_att",ascending=False)
print(ascen)



                   
