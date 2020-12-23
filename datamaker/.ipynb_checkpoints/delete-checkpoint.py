sca_par90s = tbody_attack.find_all(attrs={'data-stat': 'sca_par90'})
sca_par90_list = []
for sca_par90 in sca_par90s:
    sca_par90_list.append(sca_per90.text)

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
for sca_fouled in sca_fouled:
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


gca_passes_lives = tbody_attack.find_all(
    attrs={'data-stat': 'gca_passes_live'})
gca_passes_live_list = []
for gca_passes_live in gca_passes_lives:
    gca_passes_live_list.append(gca_passes_live.text)

gca_passes_deads = tbody_attack.find_all(
    attrs={'data-stat': 'gca_passes_dead'})
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
for gca_fouled in gca_fouled:
    gca_fouled_list.append(gca_fouled.text)

gca_defenses = tbody_attack.find_all(attrs={'data-stat': 'gca_defense'})
gca_defense_list = []
for gca_defense in gca_defenses:
    gca_defense_list.append(gca_defense.text)
