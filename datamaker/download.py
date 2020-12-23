import pandas as pd
import numpy as np
import statistics
from scipy import stats
import math

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup, Comment
import csv
import re
import sys, getopt



# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objs as go

# import plotly.offline as pyo
# from plotly import subplots




def get_basic_data():

    url = 'https://fbref.com/en/squads/206d90db/2020-2021/s10731/Barcelona-Stats-La-Liga'

    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    table = soup.table


    trs = table.find('tbody')

    minutes = trs.find_all(attrs={"data-stat": "minutes"})

    min_list = []
    for minute in minutes:
        min_list.append(minute.text)


    names = trs.find_all(attrs={'data-stat': 'player'})

    name_list = []
    for name in names:
        name_list.append(name.a.text)


    ages = trs.find_all(attrs={'data-stat':'age'})

    age_list = []
    for age in ages:
        age_list.append(age.text[:2])


    xgs = trs.find_all(attrs={'data-stat':'xg'})

    xg_list =[]
    for xg in xgs:
        xg_list.append(xg.text)


    xas = trs.find_all(attrs={'data-stat':'xa'})
    xa_list = []
    for xa in xas:
        xa_list.append(xa.text)


    npxgs = trs.find_all(attrs={'data-stat':'npxg'})
    npxg_list = []
    for npxg in npxgs:
        npxg_list.append(npxg.text)



    npxg_xas= trs.find_all(attrs={'data-stat':'npxg_xa_per90'})
    npxg_xa_list = []
    for npxg_xa in npxg_xas:
        npxg_xa_list.append(npxg_xa.text)


    with open('../assets/barca_time10.csv', 'w') as csv_file:
        fieldnames = ['team', 'name', 'age', 'mplay',  'xG', 'xA', 'npxG', 'npxG + xA']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for name, age, minute, xg, xa, npxg, npxg_xa in zip(name_list, age_list, min_list, xg_list, xa_list, npxg_list, npxg_xa_list):
            writer.writerow({'team':'Barcelona','name': name, 'age':age,  'mplay': minute, 'xG':xg, 'xA':xa, 'npxG':npxg, 'npxG + xA':npxg_xa})      


            
def get_shoot_data():
    


    url ='https://fbref.com/en/squads/206d90db/2020-2021/s10731/Barcelona-Stats-La-Liga'
    res = requests.get(url)
    ## The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile('<!--|-->')
    soup = BeautifulSoup(comm.sub("", html.text),'lxml')
    tbody = soup.findAll("tbody")
    tbody_shoot = tbody[4]

    goals = tbody_shoot.find_all(attrs={'data-stat':'goals'})
    goal_list = []
    for goal in goals:
        goal_list.append(goal.text)


    xgs = tbody_shoot.find_all(attrs={'data-stat':'xg'})
    xg_list = []
    for xg in xgs:
        xg_list.append(xg.text)

    shoots_total = tbody_shoot.find_all(attrs={'data-stat':'shots_total'})
    shoot_total_list = []
    for shoot in shoots_total:
        shoot_total_list.append(shoot.text)


    shoot90s = tbody_shoot.find_all(attrs={'data-stat':'shots_total_per90'})
    shoot90_list = []
    for shoot90 in shoot90s:
        shoot90_list.append(shoot90.text)


    sots = tbody_shoot.find_all(attrs={'data-stat':'shots_on_target'})
    sot_list = []
    for sot in sots:
        sot_list.append(sot.text)


    sot90s = tbody_shoot.find_all(attrs={'data-stat':'shots_on_target_per90'})
    sot90_list = []
    for sot in sot90s:
        sot90_list.append(sot.text)

    players = tbody_shoot.find_all(attrs={'data-stat':'player'})
    player_list = []
    for player in players:
        player_list.append(player.text)


    with open('../assets/barca/barca_shoot.csv', 'w') as csv_file:
        fieldnames = ['Player', 'Gls', 'xG', 'TotalS', 'TotalS/90', 'SonTar', 'SonT/90']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for player, gl, xg, ts, ts90, sot, sot90 in zip(player_list, goal_list, xg_list, shoot_total_list ,shoot90_list, sot_list, sot90_list):
            writer.writerow({'Player':player, 'Gls':gl, 'xG':xg, 'TotalS':ts, 'TotalS/90':ts90, 'SonTar':sot, 'SonT/90':sot90})      
            

            
            
def get_pass_data():
    
    from bs4 import BeautifulSoup
            
    url = 'https://fbref.com/en/squads/206d90db/2020-2021/s10731/Barcelona-Stats-La-Liga'
    res = requests.get(url)
    ## The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile('<!--|-->')
    soup = BeautifulSoup(comm.sub("",comm.text),'lxml')
    
    tbody = soup.findAll("tbody")
    tbody_pass = tbody[5]
    
    players = tbody_ptype.find_all(attrs={'data-stat':'player'})
    player_list = []
    for pass_player in players:
        player_list.append(pass_player.text)
    print(player_list)

    pass_attempts = tbody_pass.find_all(attrs={'data-stat':'passes'})
    attempt_list = []
    for pass_attempt in pass_attempts:
        attempt_list.append(pass_attempt.text)

    pass_comps = tbody_pass.find_all(attrs={'data-stat':'passes_completed'})
    comp_list = []
    for pass_comp in pass_comps:
        comp_list.append(pass_comp.text)


    pass_pct = tbody_pass.find_all(attrs={'data-stat':'passes_pct'})
    pct_list = []
    for pct in pass_pct:
        pct_list.append(pct.text)

    pass_distances = tbody_pass.find_all(attrs={'data-stat':'passes_total_distance'})
    distance_list = []
    for pass_distance in pass_distances:
        distance_list.append(pass_distance.text)


    pass_progress = tbody_pass.find_all(attrs={'data-stat':'passes_progressive_distance'})
    progres_list = []
    for pass_progres in pass_progress:
        progres_list.append(pass_progres.text)

    pass_longs = tbody_pass.find_all(attrs={'data-stat':'passes_long'})
    long_list = []
    for pass_long in pass_longs:
        long_list.append(pass_long.text)


    pass_comp_longs = tbody_pass.find_all(attrs={'data-stat':'passes_completed_long'})
    comp_long_list = []
    for pass_comp_long in pass_comp_longs:
        comp_long_list.append(pass_comp_long.text)

    long_comp_pcts = tbody_pass.find_all(attrs={'data-stat':'passes_pct_long'})
    long_comp_pct_list = []
    for long_comp_pct in long_comp_pcts:
        long_comp_pct_list.append(long_comp_pct.text)


    ass_mediums = tbody_pass.find_all(attrs={'data-stat':'passes_medium'})
    medium_list = []
    for pass_medium in pass_mediums:
        medium_list.append(pass_medium.text)


    pass_comp_mediums = tbody_pass.find_all(attrs={'data-stat':'passes_completed_medium'})
    comp_medium_list = []
    for pass_comp_medium in pass_comp_mediums:
        comp_medium_list.append(pass_comp_medium.text)


    medium_comp_pcts = tbody_pass.find_all(attrs={'data-stat':'passes_pct_medium'})
    medium_comp_pct_list = []
    for medium_comp_pct in medium_comp_pcts:
        medium_comp_pct_list.append(medium_comp_pct.text)

    pass_shorts = tbody_pass.find_all(attrs={'data-stat':'passes_short'})
    short_list = []
    for pass_short in pass_shorts:
        short_list.append(pass_short.text)


    pass_comp_shorts = tbody_pass.find_all(attrs={'data-stat':'passes_completed_short'})
    comp_short_list = []
    for pass_comp_short in pass_comp_shorts:
        comp_short_list.append(pass_comp_short.text)


    short_comp_pcts = tbody_pass.find_all(attrs={'data-stat':'passes_pct_short'})
    short_comp_pct_list = []
    for short_comp_pct in short_comp_pcts:
        short_comp_pct_list.append(short_comp_pct.text)

    keypasses = tbody_pass.find_all(attrs={'data-stat':'assisted_shots'})
    keypass_list = []
    for keypass in keypasses:
        keypass_list.append(keypass.text)


    ass_final_thirds = tbody_pass.find_all(attrs={'data-stat':'passes_into_final_third'})
    final_third_list = []
    for pass_final_third in pass_final_thirds:
        final_third_list.append(pass_final_third.text)


    pass_into_penaltys = tbody_pass.find_all(attrs={'data-stat':'passes_into_penalty_area'})
    into_penalty_list = []
    for pass_into_penalty in pass_into_penaltys:
        into_penalty_list.append(pass_into_penalty.text)



    cross_into_penaltys = tbody_pass.find_all(attrs={'data-stat':'crosses_into_penalty_area'})
    cross_list = []
    for cross_into_penalty in cross_into_penaltys:
        cross_list.append(cross_into_penalty.text)

    progressive_passes = tbody_pass.find_all(attrs={'data-stat':'progressive_passes'})
    progressive_pass_list = []
    for progressive_pass in progressive_passes:
        progressive_pass_list.append(progressive_pass.text)


    with open('../assets/barca/barca_pass.csv', 'w') as csv_file:

        fieldnames = ['player','Attempt', 'Completed', 'Sucpct', 'Totaldist', 'Progdist', 'LongPass', 'LongComp', 'LongPct', 'MediPass', 'MediComp', 'MediPct', 'ShortPass', 'ShortComp', 'ShortPct', 'Keypass', 'Finalthird', 'Penalty', 'CrossPena','Progcount']

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for player, attempt, comp, pct, distance, progres, long, complong, pctlong, medium, compmedium, pctmedium,short, compshort, pctshort, keypass, final, penalty, cross, pxxxx in zip(player_list, attempt_list, comp_list, pct_list, distance_list, progres_list, long_list, comp_long_list, long_comp_pct_list, medium_list, comp_medium_list, medium_comp_pct_list, short_list, comp_short_list, short_comp_pct_list, keypass_list,final_third_list, into_penalty_list, cross_list, progressive_pass_list):
            writer.writerow({'Attempt':attempt,'Completed': comp, 'Sucpct':pct, 'Totaldist':distance, 'Progdist':progres, 'LongPass':long, 'LongComp':complong,'LongPct':pctlong, 'MediPass':medium, 'MediComp':compmedium, 'MediPct':pctmedium, 'ShortPass':short, 'ShortComp':compshort, 'ShortPct':pctshort, 'Keypass':keypass, 'Finalthird':final, 'Penalty':penalty, 'CrossPena':cross,'Progcount':pxxxx})      


    
        
def get_pass_type():
        
    url = 'https://fbref.com/en/squads/206d90db/2020-2021/s10731/Barcelona-Stats-La-Liga'
    res = requests.get(url)
    ## The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile('<!--|-->')
    soup = BeautifulSoup(comm.sub("",html.text),'lxml')
    tbody = soup.findAll("tbody")
    tbody_ptype = tbody[6]

    players = tbody_ptype.find_all(attrs={'data-stat':'player'})
    player_list = []
    for pass_player in players:
        player_list.append(pass_player.text)
    print(player_list)

    pass_presses = tbody_ptype.find_all(attrs={'data-stat':'passes_pressure'})
    press_list = []
    for pass_press in pass_presses:
        press_list.append(pass_press.text)
    print(press_list)

    pass_switches = tbody_ptype.find_all(attrs={'data-stat':'passes_switches'})
    switch_list = []
    for pass_switch in pass_switches:
        switch_list.append(pass_switch.text)
    print(switch_list)

    pass_intercepts = tbody_ptype.find_all(attrs={'data-stat':'passes_intercepted'})
    intercept_list = []
    for pass_intercept in pass_intercepts:
        intercept_list.append(pass_intercept.text)
    print(intercept_list)

    pass_blockes = tbody_ptype.find_all(attrs={'data-stat':'passes_blocked'})
    block_list = []
    for pass_block in pass_blockes:
        block_list.append(pass_block.text)
    print(block_list)

    with open('../assets/barca/barca_ptype.csv', 'w') as csv_file:
        fieldnames = ['player', 'press', 'switch', 'intercepted', 'blocked']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for player, press, switch, intercept, block in zip(player_list, press_list,switch_list, intercept_list, block_list):
            writer.writerow({'player':player,'press':press, 'switch':switch, 'intercepted':intercept, 'blocked':block})


            
# def get_gk_data(pk='1e26e376', name='Sergio-Romero'):
    
#     url = f'https://fbref.com/en/players/{pk}/{name}'

#     html = requests.get(url)
#     soup = BeautifulSoup(html.content, 'html.parser')
#     table = soup.select('table')
#     tbody_list = []
#     for _table in table:
#         tbody_list.append(_table.tbody)

#     seasons = tbody_list[0](attrs={'data-stat':'season'})
#     season_list = []
#     for season in seasons:
#         season_list.append(season.text)

#     games =  tbody_list[0](attrs={'data-stat':'games_gk'})
#     game_list = []
#     for game in games:
#         game_list.append(game.text)

#     starts = tbody_list[0](attrs={'data-stat':'games_starts_gk'})
#     start_list = []
#     for start in starts:
#         start_list.append(start.text)

#     minutes = tbody_list[0](attrs={'data-stat':'minutes_gk'})
#     minute_list = []
#     for minute in minutes:
#         minute_list.append(minute.text)

#     againsts = tbody_list[0](attrs={'data-stat':'goals_against_gk'})
#     against_list = []
#     for against in againsts:
#         against_list.append(against.text)

#     against90s = tbody_list[0](attrs={'data-stat':'goals_against_per90_gk'})
#     against90_list = []
#     for against90 in against90s:
#         against90_list.append(against90.text)

#     shots_on_tgts = tbody_list[0](attrs={'data-stat':'shots_on_target_against'})
#     shots_on_tgt_list = []
#     for shots_on_tgt in shots_on_tgts:
#         shots_on_tgt_list.append(shots_on_tgt.text)

#     saves = tbody_list[0](attrs={'data-stat':'saves'})
#     save_list = []
#     for save in saves:
#         save_list.append(save.text)

#     save_pcts = tbody_list[0](attrs={'data-stat':'save_pct'})
#     save_pct_list = []
#     for save_pct in save_pcts:
#         save_pct_list.append(save_pct.text)

#     clean_sheets = tbody_list[0](attrs={'data-stat':'clean_sheets'})
#     clean_sheet_list = []
#     for clean_sheet in clean_sheets:
#         clean_sheet_list.append(clean_sheet.text)

#     clean_sheets_pcts = tbody_list[0](attrs={'data-stat':'clean_sheets_pct'})
#     clean_sheet_pct_list = []
#     for clean_sheet_pct in clean_sheets_pcts:
#         clean_sheet_pct_list.append(clean_sheet_pct.text)


#     psxg = tbody_list[1](attrs={'data-stat': 'psxg_gk'})
#     psxg_list = []
#     for _psxg in psxg:
#         psxg_list.append(_psxg)
#     psxg_list


#     psnp = tbody_list[1](attrs={'data-stat': 'psnpxg_per_shot_on_target_against'})
#     psnp_list = []
#     for _psnp in psnp:
#         psnp_list.append(_psnp)
#     psnp_list


#     net = tbody_list[1](attrs={'data-stat': 'psxg_net_gk'})
#     net_list = []
#     for _net in net:
#         net_list.append(_net)
#     net_list


#     psxg90 = tbody_list[1](attrs={'data-stat': 'psxg_net_per90_gk'})
#     psxg90_list = []
#     for _psxg90 in psxg90:
#         psxg90_list.append(_psxg90)
#     psxg90_list


#     launch = tbody_list[1](attrs={'data-stat': 'passes_pct_launched_gk'})
#     launch_list = []
#     for _launch in launch:
#         launch_list.append(_launch)
#     launch_list


#     plaunch = tbody_list[1](attrs={'data-stat': 'pct_passes_launched_gk'})
#     plaunch_list = []
#     for _plaunch in plaunch:
#         plaunch_list.append(_plaunch)
#     plaunch_list


#     lave = tbody_list[1](attrs={'data-stat': 'passes_length_avg_gk'})
#     lave_list = []
#     for _lave in lave:
#         lave_list.append(_lave)
#     lave_list


#     gkave = tbody_list[1](attrs={'data-stat': 'goal_kick_length_avg'})
#     gkave_list = []
#     for _gkave in gkave:
#         gkave_list.append(_gkave)
#     gkave_list


#     plave = tbody_list[1](attrs={'data-stat': 'passes_length_avg_gk'})
#     plave_list = []
#     for _plave in plave:
#         plave_list.append(_plave)
#     plave_list


#     cross = tbody_list[1](attrs={'data-stat': 'crosses_gk'})
#     cross_list = []
#     for _cross in cross:
#         cross_list.append(_cross)
#     cross_list


#     cstop = tbody_list[1](attrs={'data-stat': 'crosses_stopped_pct_gk'})
#     cstop_list = []
#     for _cstop in cstop:
#         cstop_list.append(_cstop)
#     cstop_list


#     outside = tbody_list[1](
#         attrs={'data-stat': 'def_actions_outside_pen_area_per90_gk'})
#     outside_list = []
#     for _outside in outside:
#         outside_list.append(_outside)
#     outside_list


#     dist = tbody_list[1](attrs={'data-stat': 'avg_distance_def_actions_gk'})
#     dist_list = []
#     for _dist in dist:
#         dist_list.append(_dist)
#     dist_list

    
#     with open(f'../assets/gk/{name}.csv', 'w') as csv_file:
#         fieldnames = [
#             'Season','Game','Start','Minute','Against', 'Against90', 
#             'Sot', 'Saves', 'Save %', 'Clean-sheet', 'Clean-sheet %', 
#             'Psxg', 'Psnp', 'Net','Psxg90', 'Launch', 'Plaunch', 'Lave', 'Gkave', 'Plave', 'Cross', 'Cstop', 'Outside', 'Dist'
#         ]
#         writer = csv.DictWriter(csv_file,fieldnames=fieldnames)

#         writer.writeheader()

#         for (season,game, start, minute,against,against90, sot, save, saveper,clean_sheet,clean_sheetper, psxg, psnp, net, psxg90, launch, plaunch,lave, gkave, plave, cross, cstop, outside, dist) in zip(season_list, game_list, start_list, minute_list, against_list, against90_list, shots_on_tgt_list, save_list, save_pct_list,clean_sheet_list, clean_sheet_pct_list, psxg_list, psnp_list,net_list, psxg90_list, launch_list, plaunch_list, lave_list, gkave_list, plave_list, cross_list, cstop_list, outside_list, dist_list):
#             writer.writerow({
#                 'Season': season,
#                 'Game': game, 
#                 'Start':start, 
#                 'Minute': minute, 
#                 'Against': against, 
#                 'Against90':against90, 
#                 'Sot':sot,  
#                 'Saves':save, 
#                 'Save %':saveper, 
#                 'Clean-sheet':clean_sheet, 
#                 'Clean-sheet %':clean_sheetper,
#                 'Psxg':psxg,
#                 'Psnp':psnp,
#                 'Net':net,
#                 'Psxg90':psxg90,
#                 'Launch':launch,
#                 'Plaunch':plaunch,
#                 'Lave':lave,
#                 'Gkave':gkave,
#                 'Plave':plave,
#                 'Cross':cross,
#                 'Cstop':cstop,
#                 'Outside':outside,
#                 'Dist':dist
#             })   




def get_attack_data():
    url ='https://fbref.com/en/squads/206d90db/2020-2021/s10731/Barcelona-Stats-La-Liga'
    res = requests.get(url)
    ## The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile('<!--|-->')
    soup = BeautifulSoup(comm.sub("", html.text),'lxml')
    tbody = soup.findAll("tbody")
    tbody_attack = tbody[7]

    players = tbody_attack.find_all(attrs={'data-stat':'player'})
    player_list = []
    for player in players:
        player_list.append(player.text)

    scas = tbody_attack.find_all(attrs={'data-stat':'sca'})
    sca_list = []
    for sca in scas:
        sca_list.append(sca.text)

    sca_per90s = tbody_attack.find_all(attrs={'data-stat': 'sca_per90'})
    sca_per90_list = []
    for sca_per90 in sca_per90s:
        sca_per90_list.append(sca_per90.text)

    sca_passes_lives = tbody_attack.find_all(attrs={'data-stat': 'sca_passes_live'})
    sca_passes_live_list = []
    for sca_passes_live in sca_passes_lives:
        sca_passes_live_list.append(sca_passes_live.text)

    sca_passes_deads = tbody_attack.find_all(attrs={'data-stat': 'sca_passes_dead'})
    sca_passes_dead_list = []
    for sca_passes_dead in sca_passes_deads:
        sca_passes_dead_list.append(sca_passes_dead.text)

    sca_dribbles = tbody_attack.find_all(attrs={'data-stat': 'sca_dribbles'})
    sca_dribble_list = []
    for sca_dribble in sca_dribbles:
        sca_dribble_list.append(sca_dribble.text)

    sca_shots = tbody_attack.find_all(attrs={'data-stat': 'sca_shots'})
    sca_shot_list = []
    for sca_shot in sca_shots:
        sca_shot_list.append(sca_shot.text)

    sca_fouleds = tbody_attack.find_all(attrs={'data-stat': 'sca_fouled'})
    sca_fouled_list = []
    for sca_fouled in sca_fouleds:
        sca_fouled_list.append(sca_fouled.text)

    sca_defenses = tbody_attack.find_all(attrs={'data-stat': 'sca_defense'})
    sca_defense_list = []
    for sca_defense in sca_defenses:
        sca_defense_list.append(sca_defense.text)


    gcas = tbody_attack.find_all(attrs={'data-stat': 'gca'})
    gca_list = []
    for gca in gcas:
        gca_list.append(gca.text)


    gca_per90s = tbody_attack.find_all(attrs={'data-stat': 'gca_per90'})
    gca_per90_list = []
    for gca_per90 in gca_per90s:
        gca_per90_list.append(gca_per90.text)


    gca_passes_lives = tbody_attack.find_all(attrs={'data-stat': 'gca_passes_live'})
    gca_passes_live_list = []
    for gca_passes_live in gca_passes_lives:
        gca_passes_live_list.append(gca_passes_live.text)

    gca_passes_deads = tbody_attack.find_all(attrs={'data-stat': 'gca_passes_dead'})
    gca_passes_dead_list = []
    for gca_passes_dead in gca_passes_deads:
        gca_passes_dead_list.append(gca_passes_dead.text)

    gca_dribbles = tbody_attack.find_all(attrs={'data-stat': 'gca_dribbles'})
    gca_dribble_list = []
    for gca_dribble in gca_dribbles:
        gca_dribble_list.append(gca_dribble.text)

    gca_shots = tbody_attack.find_all(attrs={'data-stat': 'gca_shots'})
    gca_shot_list = []
    for gca_shot in gca_shots:
        gca_shot_list.append(gca_shot.text)

    gca_fouleds = tbody_attack.find_all(attrs={'data-stat': 'gca_fouled'})
    gca_fouled_list = []
    for gca_fouled in gca_fouleds:
        gca_fouled_list.append(gca_fouled.text)

    gca_defenses = tbody_attack.find_all(attrs={'data-stat': 'gca_defense'})
    gca_defense_list = []
    for gca_defense in gca_defenses:
        gca_defense_list.append(gca_defense.text)

    with open('/work/assets/barca/barca_attack.csv', 'w')as csv_file:
        fieldnames = ['player', 'sca', 'sca90', 's_passlive', 's_passdead', 's_drib', 's_sh', 's_fld', 's_def','gca', 'gca90','g_passlive', 'g_passdead', 'g_drib', 'g_sh', 'g_fld', 'g_def']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for player, sca, sca90, s_passlive, s_passdead, s_drib, s_sh, s_fld, s_def,gca, gca90,g_passlive, g_passdead, g_drib, g_sh,g_fld,g_def in zip(player_list,sca_list, sca_per90_list, sca_passes_live_list ,sca_passes_dead_list,sca_dribble_list,sca_shot_list,sca_fouled,sca_defense_list,gca_list,gca_per90_list, gca_passes_live_list,gca_passes_dead_list,gca_dribble_list,gca_shot_list,gca_fouled_list,gca_defense_list):
            writer.writerow({'player':player, 'sca':sca, 'sca90':sca90, 's_passlive':s_passlive, 's_passdead':s_passdead, 's_drib':s_drib, 's_sh':s_sh, 's_fld':s_fld, 's_def':s_def,'gca':gca, 'gca90':gca90,'g_passlive':g_passlive, 'g_passdead':g_passdead, 'g_drib':g_drib, 'g_sh':g_sh, 'g_fld':g_fld, 'g_def':g_def})

    





if __name__ == '__main__':
    get_pass_data()