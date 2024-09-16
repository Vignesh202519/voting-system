nominee1=input("Enter the name of 1st nominee:")
nominee2=input("Enter the name of 2nd nominee:")

nm1_votes=0
nm2_votes=0

voter_id=[1,2,3,4,5,6,7,8,9,10]

no_of_voters=len(voter_id)
while True:
    if voter_id == []:
        print("The voting session is over!!!")
        if nm1_votes>nm2_votes:
            percent=nm1_votes/no_of_voters*100
            print(nominee1,"has won the election with",percent,"% of votes") 
            break

        elif nm2_votes>nm1_votes:
            percent=nm2_votes/no_of_voters*100
            print(nominee2,"has won the election with",percent,"% of votes")
            break

        else:
            print("Both have equal number of votes!!! Government will decide who will rule ") 
            break     
    
    
    
    
    voter=int(input("Enter the voter_id:"))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter)
        print("......................................")
        print("To give the vote to",nominee1,"press 1")
        print("To give the vote to",nominee2,"press 2")
        print("......................................")
        vote=int(input("Enter your precious vote:"))
        if vote==1:
            nm1_votes+=1
            print(nominee1,"Thanks for giving your important vote to them!!")
        elif vote==2:
            nm2_votes+=1
            print(nominee2,"Thanks for giving your important vote to them!!")
        elif vote>2:
            print("Check your pressed key!!")
        else:
            print("You are not a voter OR You have already voted!!")            
