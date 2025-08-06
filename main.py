#basic simple analysis of a personality dataset between introverts and extroverts
#practice for data analysis using pandas
import pandas as pd 

df=pd.read_csv('personality_dataset.csv')
#drop rows with missing values since there are not many
df.dropna(inplace=True)
df.reset_index(drop=True,inplace=True)

#categorical columns
def extrovert(df):
    if(df['Personality']=='Extrovert' and df['Stage_fear']=='Yes'):
        return True

def introvert(df):
    if(df["Personality"]=="Introvert" and df["Stage_fear"]=="Yes"):
        return True

extrovert_stagefear= df.apply(extrovert,axis=1).count()
introvert_stagefear = df.apply(introvert, axis=1).count()

total_extroverts = df.Personality.value_counts().get('Extrovert', 0)
total_introverts = df.Personality.value_counts().get('Introvert', 0)


print(" Percentage of extroverts with stage fear is: ", round((extrovert_stagefear/total_extroverts)*100,2))
print(" Percentage of introverts with stage fear is: ", round((introvert_stagefear/total_introverts)*100, 2))


introvert_drainedAfterSocializing = (df[df["Personality"]=="Introvert"]["Drained_after_socializing"].value_counts().get('Yes', 0)/ total_introverts)*100
print(f"{introvert_drainedAfterSocializing: .2f} percentage of introverts feel drained after socializing.")
extrovert_drainedAfterSocializing = (df[df["Personality"]=="Extrovert"]["Drained_after_socializing"].value_counts().get('Yes', 0)/total_introverts)*100
print(f'{extrovert_drainedAfterSocializing: .2f} percentage of extroverts feel drained after socializing.')

# Summary statistics for introverts and extroverts
introvert_summary= df[df["Personality"]=="Introvert"].describe().round(2)
print("Summary statistics for introverts:\n", introvert_summary)
extrovert_summary = df[df["Personality"]=="Extrovert"].describe().round(2)
print("Summary statistics for extroverts:\n", extrovert_summary)

# Finding weird cases where extroverts have stage fear (less than 10% of extroverts)
weird=df.loc[(df.Personality=="Extrovert") & (df.Stage_fear=="Yes")]
print("Summary of Extrovert with Stage Fear: \n",weird.describe().round(2))

#unsual case where introverts have more than 10 friends in their circle
weird1= df.loc[(df.Personality=="Introvert") & (df.Friends_circle_size> 10)]
print("Summary of Introvert with more than 10 friends: \n", weird1.describe().round(2))