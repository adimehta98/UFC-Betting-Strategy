import pandas as pd
import numpy as np
data= pd.read_csv("./ufc-master.csv")
data.head()

#### Always bet on the favourites:
capital = 5000
stake_per_bet = 100

win_counter = 0
gain_counter = 0
loss_counter = 0

def getPayout(odd,stake): 
        if odd<0:
            payout = -stake*100/odd
        else:
            payout = odd*stake/100
        return(payout)
    
init_capital = capital
for row in data.iterrows():
    if row[1]['R_odds']<0: ### Bet on Red - favourites
        if row[1]['Winner']=="Red": ### Bet on red, red wins
            win_counter = win_counter + 1
            prof = getPayout(row[1]['R_odds'],stake_per_bet)
            gain_counter = gain_counter + prof
            capital = capital+ prof
        else:   ### Bet on red, red loses
            loss_counter = loss_counter + stake_per_bet                
            capital = capital - stake_per_bet
    else: ### Bet on Blue
        if row[1]['Winner']=="Blue": ### Bet on Blue, Blue wins
            win_counter = win_counter + 1
            prof = getPayout(row[1]['B_odds'],stake_per_bet)
            gain_counter = gain_counter + prof
            capital = capital+ prof
        else: ###Bet on Blue, Blue loses
            loss_counter = loss_counter + stake_per_bet  
            capital = capital - stake_per_bet

print(f'Won {win_counter} out of {len(data)} bets made- Win Percentage: {round(100*win_counter/len(data),2)}%')
print(f'Average Win Size: {round(gain_counter/win_counter,2)}')
print(f'Average Loss Size: {round((loss_counter/(len(data)-win_counter)),2)}')
print(f'Total Profit earned: {round(capital-init_capital,2)}')
