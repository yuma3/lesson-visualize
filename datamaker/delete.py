

for i in range(df.shape[0]):
    if [name for name in df_pass['Player']][i] == pickup_player[1]:
        axes[0].scatter(
            df_pass[Xtheme][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme][i] /
            df_pass['Minute90'][i],
            alpha=1,
            s=plt_size,
            color=colors[1],
            label=[
                name for name in df_pass['Player']][i])
        axes[1].scatter(
            df_pass[Xtheme2][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme2][i],
            alpha=1,
            s=plt_size,
            color=colors[1])

    elif [name for name in df_pass['Player']][i] == pickup_player[3]:
        axes[0].scatter(
            df_pass[Xtheme][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme][i] /
            df_pass['Minute90'][i],
            alpha=1,
            s=plt_size,
            color=colors[2],
            label=[
                name for name in df_pass['Player']][i])
        axes[1].scatter(
            df_pass[Xtheme2][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme2][i],
            alpha=1,
            s=plt_size,
            color=colors[2])

    elif [name for name in df_pass['Player']][i] == pickup_player[4]:
        axes[0].scatter(
            df_pass[Xtheme][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme][i] /
            df_pass['Minute90'][i],
            alpha=1,
            s=plt_size,
            color=colors[4],
            label=[
                name for name in df_pass['Player']][i])
        axes[1].scatter(
            df_pass[Xtheme2][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme2][i],
            alpha=1,
            s=plt_size,
            color=colors[4])

    elif [name for name in df_pass['Player']][i] == pickup_player[0]:
        axes[0].scatter(
            df_pass[Xtheme][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme][i] /
            df_pass['Minute90'][i],
            alpha=1,
            s=plt_size,
            color=colors[3],
            label=[
                name for name in df_pass['Player']][i])
        axes[1].scatter(
            df_pass[Xtheme2][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme2][i],
            alpha=1,
            s=plt_size,
            color=colors[3])

    elif [name for name in df_pass['Player']][i] == pickup_player[5]:
        axes[0].scatter(
            df_pass[Xtheme][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme][i] /
            df_pass['Minute90'][i],
            alpha=1,
            s=plt_size,
            color=colors[5],
            label=[
                name for name in df_pass['Player']][i])
        axes[1].scatter(
            df_pass[Xtheme2][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme2][i],
            alpha=1,
            s=plt_size,
            color=colors[5])

    else:
        axes[0].scatter(
            df_pass[Xtheme][i] /
            df_pass['Minute90'][i],
            df_pass['Finalthird'][i] /
            df_pass['Minute90'][i],
            alpha=0.3,
            s=plt_size,
            color=colors[0])
        axes[1].scatter(
            df_pass[Xtheme2][i] /
            df_pass['Minute90'][i],
            df_pass[Ytheme2][i],
            alpha=0.3,
            s=plt_size,
            color=colors[0],
            label=[
                name for name in df_pass['Player']][i])
        axes[1].set_axisbelow(True)

axes[0].set_xlim(0, xrange)
axes[0].set_ylim(0, yrange)
axes[1].set_xlim(0, xrange2)
axes[1].set_ylim(0, yrange2)
axes[0].set_xlabel(str(Xtheme) + 'Pass per 90')
axes[0].set_ylabel(str(Ytheme) + 'Pass per 90')
axes[1].set_xlabel(Xtheme + 'per 90')
axes[1].set_ylabel(Ytheme + 'per 90')
# plt.gcf().text(0,-0.05,"@Bucciaratimes")
plt.text(-35, -25, '@Bucciaratimes', color='white', fontsize=12)
fig.legend(bbox_to_anchor=(0.05, 1), loc=3, fontsize=13, ncol=3)
fig.savefig(
    f'/work/output/{team}/pickup_oam_player_pass1.png',
    bbox_inches='tight')


dribbles_completed = table.find_all(attrs={'data-stat': 'dribbles_completed'})
dribbles_completed_list = []
for dribbles_completed in dribbles_completed[1:-1]:
    dribbles_completed_list.append(dribbles_completed.text)
dribbles_completed_list



touches = table.find_all(attrs={'data-stat': 'touches'})
touches_list = []
for touches in touches[1:-1]:
    touches_list.append(touches.text)
touches_list

pressures = table.find_all(attrs={'data-stat': 'pressures'})
pressures_list = []
for pressures in pressures[1:-1]:
    pressures_list.append(pressures.text)
pressures_list

xg = table.find_all(attrs={'data-stat': 'xg'})
xg_list = []
for xg in xg[1:-1]:
    xg_list.append(xg.text)
xg_list

xa = table.find_all(attrs={'data-stat': 'xa'})
xa_list = []
for xa in xa[1:-1]:
    xa_list.append(xa.text)
xa_list

sca = table.find_all(attrs={'data-stat': 'sca'})
sca_list = []
for sca in sca[1:-1]:
    sca_list.append(sca.text)
sca_list

gca = table.find_all(attrs={'data-stat': 'gca'})
gca_list = []
for gca in gca[1:-1]:
    gca_list.append(gca.text)
gca_list

passes_pct = table.find_all(attrs={'data-stat': 'passes_pct'})
passes_pct_list = []
for passes_pct in passes_pct[1:-1]:
    passes_pct_list.append(passes_pct.text)
passes_pct_list

carries = table.find_all(attrs={'data-stat': 'carries'})
carries_list = []
for carries in carries[1:-1]:
    carries_list.append(carries.text)
carries_list

carry_progressive_distance = table.find_all(attrs={'data-stat': 'carry_progressive_distance'})
carry_progressive_distance_list = []
for carry_progressive_distance in carry_progressive_distance[1:-1]:
    carry_progressive_distance_list.append(carry_progressive_distance.text)
carry_progressive_distance_list


