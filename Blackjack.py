import random
import time

def playerSpecialCheck():
    cardpos=0
    while cardpos<len(tempCurrentHand):
        if tempCurrentHand[cardpos]=="A":
            cardpos+=1
        else:
            cardpos=0
            for card in tempCurrentHand: 
                if card == "J" or card == "Q" or card == "K":
                    tempCurrentHand[cardpos] = 10
                    cardpos+=1
                else:
                    cardpos+=1
    cardpos=0                
    for card in tempCurrentHand: 
        if card == "A":
            tempCurrentHand[cardpos] = 11
            if sum(tempCurrentHand) > 21:
                tempCurrentHand[cardpos] = 1
        else:
            cardpos+=1

def dealerSpecialCheck():
    cardpos=0
    while cardpos<len(tempDealersHand):
        if tempDealersHand[cardpos]=="A":
            cardpos+=1
        else:
            cardpos=0
            for card in tempDealersHand: 
                if card == "J" or card == "Q" or card == "K":
                    tempDealersHand[cardpos] = 10
                    cardpos+=1
                else:
                    cardpos+=1
    cardpos=0
    for card in tempDealersHand: 
        if card == "A":
            tempDealersHand[cardpos] = 11
            if sum(tempDealersHand) > 21:
                tempDealersHand[cardpos] = 1
        else:
            cardpos+=1

balance=2500

while balance>0:
    kartlar=[2,3,4,5,6,7,8,9,10,"A","J","Q","K"]*8

    if input("\nBlackjack'e Hoş Geldiniz. Oynamak ister misiniz (E/H): ").lower()=="e":
        bet=float(input(f"Bahis miktarını yazın (Bakiyeniz: {balance}): "))
        if balance-bet<0:
            print("Lütfen bakiyenize göre bahis giriniz!")
            continue             
        
        dealersHand=[]
        currentHand=[]
        
        currentHand.append(random.choice(kartlar))
        kartlar.remove(currentHand[0])
        
        dealersHand.append(random.choice(kartlar))
        kartlar.remove(dealersHand[0])
        
        currentHand.append(random.choice(kartlar))
        kartlar.remove(currentHand[-1])
        
        dealersHand.append(random.choice(kartlar))
        kartlar.remove(dealersHand[-1])
        
        print("\nKartlar dağıtılıyor...")
        time.sleep(1)
        
        tempCurrentHand=[]
        tempDealersHand=[]
        tempCurrentHand+=currentHand
        tempDealersHand+=dealersHand
        
        if tempCurrentHand[0]=="A" and tempCurrentHand[-1]=="A":
            tempCurrentHand[0]= 11 
            tempCurrentHand[-1]= 1
        if tempDealersHand[0]=="A" and tempDealersHand[-1]=="A":
            tempDealersHand[0]= 11 
            tempDealersHand[-1]= 1
        
        playerSpecialCheck()
        dealerSpecialCheck()
        
        print(f"\nElinizdeki kartlar : {currentHand} ({sum(tempCurrentHand)})\nYerdeki kart \t: {dealersHand[0]} _ ({tempDealersHand[0]})")
        if sum(tempDealersHand)>21 and 11 in tempDealersHand:
            tempDealersHand[tempDealersHand.index(11)]=1
        
        if sum(tempCurrentHand)==21 and dealersHand[0]=="A":
            if input("\nSigorta ister misiniz? (E/H)").lower()=="e":
                if sum(tempDealersHand)!=21:
                    print(f"\nElinizdeki kartlar : {currentHand} ({sum(tempCurrentHand)}) \nYerdeki kartlar : {dealersHand} ({(sum(tempDealersHand))})\n")
                    print("Blackjack! Kazandınız!")
                    balance+=bet*2.5
                    break
                else:
                    print(f"\nElinizdeki kartlar : {currentHand} ({sum(tempCurrentHand)}) \nYerdeki kartlar : {dealersHand} ({(sum(tempDealersHand))})\n")
                    print("Sigorta ile kazandınız.")
                    balance+=bet*2
                    break
            else:
                if sum(tempDealersHand)!=21:
                    print(f"\nElinizdeki kartlar : {currentHand} ({sum(tempCurrentHand)}) \nYerdeki kartlar : {dealersHand} ({(sum(tempDealersHand))})\n")
                    print("Blackjack! Kazandınız!")
                    balance+=bet*2.5
                    break
                else:
                    print(f"\nElinizdeki kartlar : {currentHand} ({sum(tempCurrentHand)}) \nYerdeki kartlar : {dealersHand} ({(sum(tempDealersHand))})\n")
                    print("Berabere kaldınız.")
                    break

        elif sum(tempCurrentHand)==21 and (tempDealersHand[0]==10 and dealersHand[1]=="A"):
            time.sleep(0.75)
            print("Berabere kaldınız!")
            break
        
        elif sum(tempCurrentHand)==21 and tempDealersHand!=21:
            print(f"\nElinizdeki kartlar : {currentHand} ({sum(tempCurrentHand)}) \nYerdeki kartlar : {dealersHand} ({(sum(tempDealersHand))})\n")
            print("Blackjack! Kazandınız!")
            balance+=bet*2.5    
            continue

        while input("\nKart çekmek ister misiniz? (E/H)").lower() == "e":   

            currentHand.append(random.choice(kartlar))
            kartlar.remove(currentHand[-1])
            tempCurrentHand.append(currentHand[-1])
            
            print("\nKartınız veriliyor...") 
            time.sleep(0.5)
            
            playerSpecialCheck()
            
            if sum(tempCurrentHand)>21 and 11 in tempCurrentHand:
                tempCurrentHand[tempCurrentHand.index(11)]=1
            
            print(f"\nElinizdeki kartlar : {currentHand} ({sum(tempCurrentHand)}) \nYerdeki kart \t: {dealersHand[0]} _ ({tempDealersHand[0]})")
            time.sleep(1)
            if sum(tempCurrentHand)>21:
                break
            if sum(tempCurrentHand)==21:
                break
        
        if sum(tempCurrentHand)>21:
            print("\nMaalesef çok çektiniz ve kaybettiniz.")
            print(f"Yerdeki kartlar: {dealersHand} ({(sum(tempDealersHand))})")
            balance-=bet
            continue
        
        playerSpecialCheck()
        dealerSpecialCheck()
        
        while sum(tempDealersHand)<17:
            
            print(f"\nElinizdeki kartlar : {currentHand} ({(sum(tempCurrentHand))}) \nYerdeki kart \t: {dealersHand} ({sum(tempDealersHand)})\nYer yeni kart çekiyor...\n")
            time.sleep(1)
            dealersHand.append(random.choice(kartlar))
            tempDealersHand.append(dealersHand[-1])
            kartlar.remove(dealersHand[-1])

            dealerSpecialCheck()
            
            if sum(tempDealersHand)>21 and 11 in tempDealersHand:
                tempDealersHand[tempDealersHand.index(11)]=1

        if sum(tempCurrentHand)>21:
            print(f"\nElinizdeki Kartlar: {currentHand} ({(sum(tempCurrentHand))})\nYerdeki Kartlar: {dealersHand} ({(sum(tempDealersHand))})\nMaalesef fazla çektiniz ve kaybettiniz!")
            balance-=bet
        elif sum(tempCurrentHand)!=21 and (tempDealersHand[0]==10 and dealersHand[1]=="A"):
            print(f"\nElinizdeki Kartlar: {currentHand} ({(sum(tempCurrentHand))})\nYerdeki Kartlar: {dealersHand} ({(sum(tempDealersHand))})\nYer blackjack oldu ve kaybettiniz!")
            balance-=bet
        elif sum(tempCurrentHand)!=21 and (dealersHand[0]=="A" and tempDealersHand[1]==10):
            print(f"\nElinizdeki Kartlar: {currentHand} ({(sum(tempCurrentHand))})\nYerdeki Kartlar: {dealersHand} ({(sum(tempDealersHand))})\nYer blackjack oldu ve kaybettiniz!")
            balance-=bet    
        elif sum(tempDealersHand)>21 and sum(tempCurrentHand)<=21:
            print(f"\nElinizdeki Kartlar: {currentHand} ({(sum(tempCurrentHand))})\nYerdeki Kartlar: {dealersHand} ({(sum(tempDealersHand))})\nTebrikler kasa patladı ve kazandınız!")
            balance+=bet
        elif sum(tempCurrentHand)> sum(tempDealersHand):
            print(f"\nElinizdeki Kartlar: {currentHand} ({(sum(tempCurrentHand))})\nYerdeki Kartlar: {dealersHand} ({(sum(tempDealersHand))})\nTebrikler Kasayı yendiniz!")
            balance+=bet
        elif sum(tempDealersHand)> sum(tempCurrentHand):
            print(f"\nElinizdeki Kartlar: {currentHand} ({(sum(tempCurrentHand))})\nYerdeki Kartlar: {dealersHand} ({(sum(tempDealersHand))})\nMaalesef kasayı geçemediniz ve kaybettiniz!")
            balance-=bet
        elif sum(tempCurrentHand)==sum(tempCurrentHand):
            print(f"\nElinizdeki Kartlar: {currentHand} ({(sum(tempCurrentHand))})\nYerdeki Kartlar: {dealersHand} ({(sum(tempDealersHand))})\nBerabere kaldınız.")
    else:
        print("Çıkış yapılıyor...")
        break

if balance<=0:
    print("Bakiyeniz bitti. Yenilemek için tekrardan başlatın.")
    time.sleep(5)
    quit