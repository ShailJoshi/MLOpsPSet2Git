import numpy
import pandas
import pickle

def CleanUpDf():
    
    df = pandas.read_csv('./data/raw/04_cricket_1999to2011.csv')
    # Keep 1st innings data and remove errorneus data
    df_firstInnings = df[(df['Innings']==1) & (df['Error.In.Data']==0)]

    # Keep only the necessary columns
    df_firstInnings = df_firstInnings[['Match','Over','Runs','Total.Runs','Innings.Total.Runs','Total.Out','Innings.Total.Out']]
    numMatches = df_firstInnings.Match.unique().shape[0]
    df_firstInnings = df_firstInnings[df_firstInnings['Match']<100000]
    # Create a column of expected total i.e. the sum of runs per over
    df_fIinningsSum = df_firstInnings[['Match','Runs']].groupby('Match').aggregate(numpy.sum)
    df_fIinningsSum = df_fIinningsSum.rename(columns={'Runs': 'ExpectedTotal'})
    df_scoreCompare = df_firstInnings.merge(df_fIinningsSum, on='Match')

    # Create a column of total Overs bowled in the first innings of the match
    df_fItotalOvers = df_scoreCompare[['Match','Over']].groupby('Match').aggregate(numpy.max).rename(columns={'Over':'TotalOvers'})
    df_temp = df_scoreCompare.merge(df_fItotalOvers,on='Match')

    # Remove innnigs if it neither finished by overs nor by all-out
    df_cleaned = df_temp[(df_temp['TotalOvers']==50) | (df_temp['Innings.Total.Out']==10)]
    
    # Remove innings if the mismatch between Expected Total and Actual Total is beyond a threshold. Indicates that many over's data is missing
    df_cleanedfinal = df_cleaned[df_cleaned['Innings.Total.Runs']<=(df_cleaned['ExpectedTotal']+10)]# & ((df_temp['TotalOvers']==50) | (df_temp['Innings.Total.Out']==10))]
    print(df_cleanedfinal.size)
    dbfile = open('./data/interim/temp4', 'ab')
    pickle.dump(df_cleanedfinal, dbfile)
    dbfile.close()
    
    return
