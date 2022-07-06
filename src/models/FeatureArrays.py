
import numpy
import pickle

def FeatureArrays():

    dbfile = open('./data/interim/temp4', 'rb')
    df_cleanedfinal = pickle.load(dbfile)
    dbfile.close()
# Create a column of runs yet to be scored in the innings
    df_cleanedfinal['TotalminusScored'] = df_cleanedfinal['Innings.Total.Runs']-df_cleanedfinal['Total.Runs']

    # Create a column of overs remaining to bat
    df_cleanedfinal['OversLeft'] = 50-df_cleanedfinal['Over']

    # Extract overs-left, wickets and runs yet to be scored data
    OversLeftArr = df_cleanedfinal['OversLeft'].to_numpy()
    WicketsArr = df_cleanedfinal['Total.Out'].to_numpy()
    MoreRunsScored = df_cleanedfinal['TotalminusScored'].to_numpy()

    # Extract overs-left, wickets and runs yet to be scored data
    OversLeftArr = df_cleanedfinal['OversLeft'].to_numpy()
    WicketsArr = df_cleanedfinal['Total.Out'].to_numpy()
    MoreRunsScored = df_cleanedfinal['TotalminusScored'].to_numpy()

    # Extract data when overs left are 50 (and wickets are 0 obviously)
    df_temp = df_cleanedfinal[(df_cleanedfinal['Over']==1)]
    df_temp['zero'] = 0
    df_temp['fifty'] = 50
    OversLeftArr2 = df_temp['fifty'].to_numpy()
    WicketsArr2 = df_temp['zero'].to_numpy()
    MoreRunsScored2 = df_temp['Innings.Total.Runs'].to_numpy()

    # Combine all the data. For each over(row) the overs left, wickets and runs to score are stored in ordered arrays
    OversLeftArr = numpy.concatenate((OversLeftArr,OversLeftArr2))
    WicketsArr = numpy.concatenate((WicketsArr,WicketsArr2))
    MoreRunsScored = numpy.concatenate((MoreRunsScored,MoreRunsScored2))

    # Form input and output data
    InputData = [OversLeftArr,WicketsArr]
    OutputData = MoreRunsScored.astype(float)

    dbfile = open('./data/interim/temp5', 'ab')
    pickle.dump(InputData, dbfile)
    dbfile.close()

    dbfile = open('./data/interim/temp6', 'ab')
    pickle.dump(OutputData, dbfile)
    dbfile.close()
    

    return