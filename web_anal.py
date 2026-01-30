#ingest data structure
import pandas as pd
df=pd.read_csv("webinar_rawdata - Sheet1.csv")

#extract the timestamp form record id
df["record_timestamp"]=df["Record ID"].str.split("_").str[1]
df["record_timestamp"]=pd.to_datetime(df["record_timestamp"])


# Sort records to retain the latest interaction per participant per event

d = df.sort_values(by="record_timestamp")
print("Before Cleaning:",d.shape)

#remove the duplicate by keeping the latest record
df_clean = d.drop_duplicates(
    subset=["Email","Event name"],keep="last").copy()
print("After cleaning:",df_clean.shape)

#Validate no duplicates remain
r_duplicate = df_clean.duplicated(subset=["Email","Event name"]).sum()
#print("Remaining Duplicate",r_duplicate)


#checking for null values

print(df_clean.isnull().sum())

print(df_clean.isnull().sum().sum())

#creating analytics

df_clean["attended_flag"]= df_clean["Attendance Status"].apply(
    lambda x:1 if x=="Attended" else 0)

count=df_clean["attended_flag"].value_counts()
print(count)

#attendance Rate
total_registrants = len(df_clean)
total_attended = df_clean["attended_flag"].sum()
attendance_rate = (total_attended/total_registrants)*100
print("Total Registrants:",total_registrants)
print("Total Attended:",total_attended)
print("Attendance Rate:",attendance_rate)


#Filtering the attendees
attended = df_clean[df_clean["attended_flag"]==1]
recommendation = attended[attended["Would you recommend our webinars"].notna()
                          ]
yes_count = recommendation[
    recommendation["Would you recommend our webinars"] == "Yes"
].shape[0]

total_responses = recommendation.shape[0]

recommendation_rate = (yes_count / total_responses) * 100

print("Total Attendee Responses:", total_responses)
print("Yes Recommendations:", yes_count)
print(f"Recommendation Rate: {recommendation_rate:.2f}%")



