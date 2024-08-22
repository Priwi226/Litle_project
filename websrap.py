#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:04:22 2023

@author: priwi
"""

    #   Import kniznic 
import requests
from bs4 import BeautifulSoup

    #   prechod na stranku 
page = requests.get ("https://isport.blesk.cz/vysledky?selday=2024-03-10")

    #   ziskanie kodu stranky 
# print (page.text)

soup = BeautifulSoup(page.text, 'html.parser')
# print (soup.prettify())

Match_rows = soup.find_all('div', 'list-score-structured-wapper')
#print(Match_rows)
favotir_team = input("Your favorit team?"

    # ziskanie tabukly z datumom

for Daten in Match_rows:
    
    # Datum / cas 
    datum_cas = Daten.find("div", "datetime-container")
    if datum_cas != None:
        datum_cas = Daten.find("div", "datetime-container").text
        datum_cas = ' '.join(datum_cas.split())
        # print ("\nDatum a cas:" + str(datum_cas))
    else:
        continue
        # print("\nDatum zeit ist unbekant")
        
    # Meno domaceho teamu 
    
    Home_team = Daten.find('div', 'team-container team-home')
    if Home_team != None:
        Home_team = Daten.find('div', 'team-container team-home').text
        Home_team = " ".join(Home_team.split())
        # print ("Home_team\n" + Home_team)
    else:
        continue
        # print("Home team unbekant")
    
    # Meno hostujuceho teamu
    away_team = Daten.find("div", "team-container team-away")
    if away_team != None:
        away_team = Daten.find("div", "team-container team-away").text
        away_team = " ".join(away_team.split())
        # print ("Away Team\n" + str(away_team))
    else:
        continue
        # print("Gast team unbekant")
        
    # Score
    score = Daten.find("div", "score")
    if score != None:
        score = Daten.find("div", "score").text
        # print (score[0])
        # print (score[3])
        # print("Skore:\n" + str(score))
    else:
        continue
        # print("Skore ist unbekant")
    
    # losser metode1
    if score[0] > score[2]:
        vinner = Home_team
        loser = away_team
    elif score[0] == score[2]:
        vinner = None
        loser = None
    else:
        vinner = away_team
        loser = Home_team
    
        
    # print ("vyner:\n" + str(vynner))
        
    # Looser metode2
    looser = Daten.find("div", "team-name team-looser")
    if looser != None:
        looser = Daten.find("div", "team-name team-looser").text
    else:
        if looser == None and Home_team == None:
        #    print("Losser unbekant")
            continue
            
    # Priorit team
    if favotir_team == Home_team or favotir_team == away_team:
        if looser != favotir_team and score[0] != score[2]:
            print ("Metode 1 :")
            print (str(datum_cas) + " Wir sind gewonen in duel: " + str(looser))
        else: 
            print ("Metode 1 : Keine ergebnise")
            
    if favotir_team == Home_team or favotir_team == away_team:
        if vinner == favotir_team:
            print ("Metode 2 :")
            print (str(datum_cas) + " Wir sind gewonen in duel. " + str(loser) + " Ist verloren")
        else: 
            print ("Metode 2 : Keine ergebnise")
     
