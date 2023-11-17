#Greedy Algorithm for set covering problem.
#Create a list of all states.
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])

#Create the list of stateions.
stations = {}
stations["kone"]=set(["id","nv","ut"])
stations["ktwo"]=set(["wa","id","mt"])
stations["kthree"]=set(["or","nv","ca"])
stations["kfour"]=set(["nv","ut"])
stations["kfive"]=set(["ca","az"])

#Final set of stations
final_stations = set()

while states_needed: #While there are still states that we need to cover
    best_station = None #This is the station that covers the remaining most uncovered states
    states_covered = set() #The states which this BEST STATION covers
    for station, states_for_station in stations.items(): #Loop over all the stations
        covered = states_for_station & states_needed #These are the uncovered states that the current station in loop covers
        if len(covered)>len(states_covered): #If current station covers more than the previous stations in the loop
            best_station = station #Make current station the best station
            states_covered = covered #Count the states covered by this station as the current tally of states covered
    states_needed-=states_covered #After the for loop is done, remove the states covered by the best station from states needed
    final_stations.add(best_station) #Add the best station in last run of for loop to the final stations set.

print (final_stations) #Print the list of stations chosen.
