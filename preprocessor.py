import csv
fileObj = open('responses.csv')

csvObj = csv.DictReader(fileObj)

engagementOptions = ["Like", "Retweet with quote", "Retweet without quote", "Click on author's profile", "View replies", "Write reply", "Ignore/keep scrolling"]
reactionOptions = ["Fear", "Hope", "Sadness", "Joy", "Distress", "Relief", "Frustration", "Empathy", "Dissension", "Agreement", "NONE"]

counter = 1

newObjects = []

for row in csvObj:
    
    uniName = row['Where do you go to school?'].strip().lower()

    # eventually won't need these lines
    del row['Timestamp']
    del row['Are you a college/university student currently working towards completing an undergraduate or graduate degree?']
    del row['Do you consent to having your responses used as part of a sociological experiment conducted by students at Duke University?']
    del row['Read Instructions']
    del row["What's your email address?"]
    
    print('response ', counter)

    for i in range(1, 19):
        newRow = {}
        newRow['Respondent'] = counter
        newRow['Tweet'] = i
        newRow['College'] = uniName
        newRow['Ideology'] = row['How would you describe your political beliefs relative to the rest of the US population?']
        engagementKey = "Tweet " + str(i)
        reactionKey = f"How did you feel about Tweet {str(i)}?"

        engagementValues = row[engagementKey].split(", ")
        reactionValues = row[reactionKey].split(", ")

        for engagement in engagementOptions:
            if engagement in engagementValues:
                newRow[f"Engagement_{engagement}"] = 1
            else:
                newRow[f"Engagement_{engagement}"] = 0
        
        for reaction in reactionOptions:
            if reaction in reactionValues:
                newRow[f"Reaction_{reaction}"] = 1
            else:
                newRow[f"Reaction_{reaction}"] = 0
        
        newObjects.append(newRow)
        
    counter+=1


columns = newObjects[0].keys()
with open('formatted_responses.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, columns)
    dict_writer.writeheader()
    dict_writer.writerows(newObjects)



# THE FOLLOWING WAS USED TO IDENTIFY AND AMELIORATE TYPOS IN SCHOOL NAME, INCLUDING SPELLING ERRORS AND FAILURE TO PUT ENTIRE SCHOOL NAME,
# LIKE RESPONDENTS WHO WROTE DOWN "YALE" INSTEAD OF "YALE UNIVERSITY"
# schoolSet = set([])
# for row in csvObj:
#     uniName = row['Where do you go to school?'].strip().lower()
#     schoolSet.add(uniName)

# arr = sorted(list(schoolSet))
# for i in range(len(arr)):
#     print(arr[i])
