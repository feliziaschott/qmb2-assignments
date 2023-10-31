import random
def CoinFlips(no_flips):
    flipResults=[]
    isHead=bool()
    #no_flips=2
    
    for i in range(no_flips):
        
        if(random.random()<0.5):
            isHeads=True
            
        else:
            isHeads=False
        flipResults.append(isHeads)
    return(flipResults)
        
no_flips=10
flipResults=CoinFlips(no_flips)
print(flipResults)

#global definitions are overwritten by local (inside function) ones 
