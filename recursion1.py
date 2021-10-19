#s

pengar = 1932
jarn=200
silver=500
guld=1000
g_smycken=0
s_smycken= 0
j_smycken=0
def smycke(pengar,guld,silver,jarn,g_smycken,s_smycken,j_smycken):
if pengar >=guld:
g_smycken=g_smycken+1
pengar = pengar-gulda
smycke(pengar,guld,silver,jarn,g_smycken,s_smycken,j_smycken)
elif pengar >=silver:
s_smycken=s_smycken+1
pengar=pengar-silver
smycke(pengar,guld,silver,jarn,g_smycken,s_smycken,j_smycken)
elif pengar >= jarn:
j_smycken=j_smycken+1
pengar=pengar-jarn
smycke(pengar,guld,silver,jarn,g_smycken,s_smycken,j_smycken)
else:
print("inte råd")
print("g: ",g_smycken," s: ",s_smycken," j :",j_smycken," pengar kvar:",pengar)

smycke(pengar,guld,silver,jarn,g_smycken,s_smycken,j_smycken)
