DATASET_COLORSTRIP
#In colored strip datasets, each ID is associated to a color box/strip and can have an optional label. Color can be specified in hexadecimal, RGB or RGBA notation. When using RGB or RGBA notation, you cannot use COMMA as the dataset separator

#lines starting with a hash are comments and ignored during parsing

#=================================================================#
#                    MANDATORY SETTINGS                           #
#=================================================================#
#select the separator which is used to delimit the data below (TAB,SPACE or COMMA).This separator must be used throughout this file (except in the SEPARATOR line, which uses space).

#SEPARATOR TAB
#SEPARATOR COMMA
SEPARATOR SPACE

#label is used in the legend table (can be changed later)
DATASET_LABEL Taxonomy

#dataset color (can be changed later)
COLOR #000000

#=================================================================#
#                    OPTIONAL SETTINGS                            #
#=================================================================#

#If COLOR_BRANCHES is set to 1, branches of the tree will be colored according to the colors of the strips above the leaves.
#When all children of a node have the same color, it will be colored the same, ie. the color will propagate inwards towards the root.
COLOR_BRANCHES 1

#each dataset can have a legend, which is defined below
#for each row in the legend, there should be one shape, color and label
#shape should be a number between 1 and 5:
#1: square
#2: circle
#3: star
#4: right pointing triangle
#5: left pointing triangle

LEGEND_TITLE Taxonomy
LEGEND_SHAPES 1 1 1 1 1 1
LEGEND_COLORS #e21a1c #dd7a50 #86ce84 #28b1aa #4a72a5 #72727b
LEGEND_LABELS Metazoa Fungi Viridiplantae Bacteria Viruses Other
# LEGEND_SHAPES 1 1 1 1 1 1 1 1 1 1 1 1
# LEGEND_COLORS #e31a1c #fb9a99 #ff7f00 #fdbf6f #b15928 #6a3d9a #cab2d6 #1f78b4 #a6cee3 #33a02c #ffff99 #969696 
# LEGEND_LABELS Leotiomycetes Sordariomycetes Eurotiomycetes Dothideomycetes other_Pezizomycotina other_Ascomycota other_Fungi other_Opisthokonta other_Eukaryota Bacteria Archaea Viruses 

#=================================================================#
#     all other optional settings can be set or changed later     #
#           in the web interface (under 'Datasets' tab)           #
#=================================================================#

#width of the colored strip
STRIP_WIDTH 35

#left margin, used to increase/decrease the spacing to the next dataset. Can be negative, causing datasets to overlap.
#MARGIN 5

#border width; if set above 0, a border of specified width (in pixels) will be drawn around the color strip 
#BORDER_WIDTH 2

#border color; used when BORDER_WIDTH is above 0
#BORDER_COLOR #969696

#always show internal values; if set, values associated to internal nodes will be displayed even if these nodes are not collapsed. It could cause overlapping in the dataset display.
#SHOW_INTERNAL 1

#Internal tree nodes can be specified using IDs directly, or using the 'last common ancestor' method described in iTOL help pages

#=================================================================#
#       Actual data follows after the DATA keyword                #
#=================================================================#
DATA

#Examples:
#assign a red colored strip to leaf 9606, with label 'Human' (label is displayed in the mouseover popups)
#9606 #ff0000 Human

#assign a green, semi-transparent (alpha 0.5) strip to an internal node, without any label. If 'Show internal values' is set to 'No', this will only be displayed if the node is collapsed. 
#9606|5664 rgba(0,255,0,0.5)
XP_046969005.1-171605-Vanessa_cardui-Insecta #e21a1c Metazoa
WP_053605648.1-1441095-Bacillus_gobiensis-Firmicutes #28b1aa Bacteria
WP_019122359.1-1118054-Brevibacillus_massiliensi-Firmicutes #28b1aa Bacteria
WP_143847815.1-2597270-Bacillus_sp_P16_2019-Firmicutes #28b1aa Bacteria
WP_059105621.1-1649580-Bacillus_shacheensis-Firmicutes #28b1aa Bacteria
WP_061573397.1-1452-Bacillus_atrophaeus-Firmicutes #28b1aa Bacteria
WP_099679932.1-1408-Bacillus_pumilus-Firmicutes #28b1aa Bacteria
WP_041088181.1-889306-Jeotgalibacillus_soli-Firmicutes #28b1aa Bacteria
WP_007208772.1-246144-Enterococcus_italicus-Firmicutes #28b1aa Bacteria
WP_113713644.1-135735-Bacillus_endophyticus-Firmicutes #28b1aa Bacteria
WP_019393954.1-1402861-Bacillus_filamentosus-Firmicutes #28b1aa Bacteria
WP_120192015.1-342944-Sinobaca_qinghaiensis-Firmicutes #28b1aa Bacteria
lac1626.10-691651-Lerema_accius-Insecta #e21a1c Metazoa
WP_036052855.1-1385935-Leptolyngbya_sp_Heron_Is-Cyanobacteria #28b1aa Bacteria
WP_086349110.1-1834193-Enterococcus_sp_9E7_DIV0-Firmicutes #28b1aa Bacteria
WP_091509822.1-658219-Microbulbifer_yueqingensi-Proteobacteria #28b1aa Bacteria
WP_099303637.1-2014782-Bacillus_sp_Marseille_P3-Firmicutes #28b1aa Bacteria
WP_095317567.1-79880-Bacillus_clausii-Firmicutes #28b1aa Bacteria
WP_078392438.1-228576-Bacillus_patagoniensis-Firmicutes #28b1aa Bacteria
WP_091613642.1-1122204-Marinococcus_luteus-Firmicutes #28b1aa Bacteria
WP_079476981.1-1371-Marinococcus_halophilus-Firmicutes #28b1aa Bacteria
WP_046366959.1-549295-Flavihumibacter_petaseus-BacteroChlorobi #28b1aa Bacteria
WP_036748112.1-1654360-Photobacterium_galatheae-Proteobacteria #28b1aa Bacteria
WP_102797123.1-366582-Bowmanella_denitrificans-Proteobacteria #28b1aa Bacteria
WP_110458214.1-614070-Shewanella_algidipiscicol-Proteobacteria #28b1aa Bacteria
WP_124155706.1-1458930-Okeania_hirsuta-Cyanobacteria #28b1aa Bacteria
WP_017660055.1-102127-Geitlerinema_sp_PCC_7105-Cyanobacteria #28b1aa Bacteria
WP_124742576.1-2491024-Bacillus_sp_C1_1-Firmicutes #28b1aa Bacteria
WP_134259633.1-300825-Bacillus_lehensis-Firmicutes #28b1aa Bacteria
WP_095301005.1-2021690-Bacillus_sp_7586_K-Firmicutes #28b1aa Bacteria
WP_034638000.1-574376-Bacillus_manliponensis-Firmicutes #28b1aa Bacteria
GBP38409.1-151549-Eumeta_japonica-Insecta #e21a1c Metazoa
QUERY_XP_037965243.1-51655-Plutella_xylostella-Insecta #e21a1c Metazoa
Hcyd006487.1-33424-Heliconius_cydno-Insecta #e21a1c Metazoa
WP_003758719.1-1641-Listeria_grayi-Firmicutes #28b1aa Bacteria
WP_046221640.1-265726-Photobacterium_halotolera-Proteobacteria #28b1aa Bacteria
WP_120512697.1-1616783-Photobacterium_sp_LAM907-Proteobacteria #28b1aa Bacteria
WP_138494546.1-1768003-Paenibacillus_pinistramen-Firmicutes #28b1aa Bacteria
WP_130000768.1-2511172-Sporolactobacillus_sp_TH-Firmicutes #28b1aa Bacteria
XP_026317611.1-1477025-Hyposmocoma_kahamanoa-Insecta #e21a1c Metazoa
WP_116253301.1-2135471-Pedobacter_sp_OV280-BacteroChlorobi #28b1aa Bacteria
WP_160036102.1-2689577-Paenibacillus_sp_An7-Firmicutes #28b1aa Bacteria
WP_068699318.1-1462996-Paenibacillus_yonginensis-Firmicutes #28b1aa Bacteria
WP_094094899.1-1619311-Paenibacillus_physcomitre-Firmicutes #28b1aa Bacteria
WP_141604441.1-1380157-Terrilactibacillus_laevil-Firmicutes #28b1aa Bacteria
WP_101566164.1-2066053-Bacillus_sp_UMB0893-Firmicutes #28b1aa Bacteria
WP_029280944.1-246786-Bacillus_indicus-Firmicutes #28b1aa Bacteria
WP_019153565.1-1287657-Bacillus_massiliosenegale-Firmicutes #28b1aa Bacteria
WP_141432255.1-2578211-Bacillus_sp_03113-Firmicutes #28b1aa Bacteria
KOB77979.1-104452-Operophtera_brumata-Insecta #e21a1c Metazoa
WP_036060410.1-1006155-Listeria_weihenstephanens-Firmicutes #28b1aa Bacteria
WP_036099736.1-1494964-Listeria_riparia-Firmicutes #28b1aa Bacteria
WP_036087941.1-1552123-Listeria_booriae-Firmicutes #28b1aa Bacteria
WP_011703250.1-1643-Listeria_welshimeri-Firmicutes #28b1aa Bacteria
WP_003749612.1-1640-Listeria_seeligeri-Firmicutes #28b1aa Bacteria
WP_111143643.1-1638-Listeria_ivanovii-Firmicutes #28b1aa Bacteria
WP_163655106.1-1844999-Listeria_sp_PSOL_1-Firmicutes #28b1aa Bacteria
WP_099222512.1-2026604-Listeria_costaricensis-Firmicutes #28b1aa Bacteria
WP_090657928.1-1465490-Parafilimonas_terrae-BacteroChlorobi #28b1aa Bacteria
WP_057934744.1-687842-Pedobacter_ginsenosidimut-BacteroChlorobi #28b1aa Bacteria
WP_016111878.1-1396-Bacillus_cereus-Firmicutes #28b1aa Bacteria
WP_029325391.1-1380110-Bacillus_sp_RP1137-Firmicutes #28b1aa Bacteria
WP_160909488.1-462910-Pontibacillus_yanchengens-Firmicutes #28b1aa Bacteria
WP_026698630.1-427072-Bacillus_chagannorensis-Firmicutes #28b1aa Bacteria
WP_107583668.1-200989-Alkalicoccus_saliphilus-Firmicutes #28b1aa Bacteria
WP_147804953.1-1667239-Alkalicoccus_halolimnae-Firmicutes #28b1aa Bacteria
WP_100486282.1-1591408-Sporolactobacillus_pectin-Firmicutes #28b1aa Bacteria
WP_135347906.1-1465501-Sporolactobacillus_shorea-Firmicutes #28b1aa Bacteria
WP_010896911.1-86665-Bacillus_halodurans-Firmicutes #28b1aa Bacteria
WP_160545405.1-2320880-bacterium_1xD42_11-other_Bacteria #28b1aa Bacteria
WP_066054044.1-519977-Bacillus_korlensis-Firmicutes #28b1aa Bacteria
WP_095320602.1-1397-Bacillus_circulans-Firmicutes #28b1aa Bacteria
WP_163185821.1-2709706-Bacillus_sp_34_1-Firmicutes #28b1aa Bacteria
WP_089742245.1-531814-Gracilibacillus_ureilytic-Firmicutes #28b1aa Bacteria
WP_153834647.1-563735-Gracilibacillus_thailande-Firmicutes #28b1aa Bacteria
XP_026317766.1-1477025-Hyposmocoma_kahamanoa-Insecta #e21a1c Metazoa
WP_036065592.1-1494963-Listeria_grandensis-Firmicutes #28b1aa Bacteria
WP_153648577.1-1642-Listeria_innocua-Firmicutes #28b1aa Bacteria
WP_160464817.1-1639-Listeria_monocytogenes-Firmicutes #28b1aa Bacteria
WP_036073252.1-1494960-Listeria_aquatica-Firmicutes #28b1aa Bacteria
WP_007546995.1-1069827-Listeria_fleischmannii-Firmicutes #28b1aa Bacteria
WP_121319477.1-2183917-Flavobacterium_sp_JRR_20-BacteroChlorobi #28b1aa Bacteria
WP_114792988.1-577386-Niabella_yanshanensis-BacteroChlorobi #28b1aa Bacteria
WP_142526254.1-425512-Pedobacter_westerhofensis-BacteroChlorobi #28b1aa Bacteria
WP_029276620.1-475254-Pedobacter_borealis-BacteroChlorobi #28b1aa Bacteria
WP_035545139.1-1543706-Halobacillus_sp_BBL2006-Firmicutes #28b1aa Bacteria
WP_090842834.1-745820-Bacillus_daliensis-Firmicutes #28b1aa Bacteria
WP_168007195.1-1237094-Bacillus_luteus-Firmicutes #28b1aa Bacteria
WP_044642370.1-1329796-Risungbinella_massiliensi-Firmicutes #28b1aa Bacteria
WP_036072068.1-647910-Listeria_rocourtiae-Firmicutes #28b1aa Bacteria
WP_167628760.1-2705293-Listeria_sp_CLIP_2019_00-Firmicutes #28b1aa Bacteria
WP_088839006.1-1918331-Listeria_sp_ILCC792-Firmicutes #28b1aa Bacteria
WP_088840738.1-1918333-Listeria_sp_ILCC797-Firmicutes #28b1aa Bacteria
WP_071637528.1-986-Flavobacterium_johnsoniae-BacteroChlorobi #28b1aa Bacteria
WP_166577523.1-2683257-Emticicia_sp_ODNR4P-BacteroChlorobi #28b1aa Bacteria
WP_073235892.1-288992-Pedobacter_caeni-BacteroChlorobi #28b1aa Bacteria
WP_108198914.1-2135716-Pedobacter_sp_OK291-BacteroChlorobi #28b1aa Bacteria
WP_144449175.1-688079-Bacillus_nanhaiisediminis-Firmicutes #28b1aa Bacteria
WP_100398976.1-2014005-Bacillus_sp_FJAT_44742-Firmicutes #28b1aa Bacteria
WP_090798676.1-1882751-Paenibacillus_sp_GP183-Firmicutes #28b1aa Bacteria
WP_138884098.1-2582849-Paenibacillus_mesophilus-Firmicutes #28b1aa Bacteria
WP_053400457.1-284581-Bacillus_koreensis-Firmicutes #28b1aa Bacteria
WP_041262048.1-332410-Exiguobacterium_sibiricum-Firmicutes #28b1aa Bacteria
WP_029331839.1-223958-Exiguobacterium_oxidotole-Firmicutes #28b1aa Bacteria
WP_055969375.1-1736294-Exiguobacterium_sp_Leaf1-Firmicutes #28b1aa Bacteria
WP_053454574.1-1684312-Exiguobacterium_sp_BMC_K-Firmicutes #28b1aa Bacteria
WP_047394365.1-1224749-Exiguobacterium_sp_ZWU00-Firmicutes #28b1aa Bacteria
WP_089751993.1-396056-Halobacillus_alkaliphilus-Firmicutes #28b1aa Bacteria
WP_014642871.1-1570-Halobacillus_halophilus-Firmicutes #28b1aa Bacteria
WP_036129681.1-2269046-Listeria_sp_SHR_NRA_18-Firmicutes #28b1aa Bacteria
WP_036094245.1-1497681-Listeria_newyorkensis-Firmicutes #28b1aa Bacteria
WP_115753968.1-1621700-Listeria_kieliensis-Firmicutes #28b1aa Bacteria
WP_122864963.1-2268407-Listeria_thailandensis-Firmicutes #28b1aa Bacteria
WP_149091793.1-2595005-Rufibacter_sp_NBS58_1-BacteroChlorobi #28b1aa Bacteria
WP_074604215.1-430522-Pedobacter_steynii-BacteroChlorobi #28b1aa Bacteria
WP_124582968.1-2153359-Pedobacter_sp_KBW06-BacteroChlorobi #28b1aa Bacteria
WP_086546033.1-1986952-Sphingobacteriaceae_bacte-BacteroChlorobi #28b1aa Bacteria
WP_131528232.1-2530456-Pedobacter_sp_RP_3_21-BacteroChlorobi #28b1aa Bacteria
WP_155705574.1-1778678-Paenibacillus_psychroresi-Firmicutes #28b1aa Bacteria
WP_081415818.1-356658-Bacillus_kribbensis-Firmicutes #28b1aa Bacteria
WP_065525016.1-414778-Planococcus_donghaensis-Firmicutes #28b1aa Bacteria
WP_165205063.1-1398745-Bacillaceae_bacterium_SIJ-Firmicutes #28b1aa Bacteria
WP_134701468.1-1644106-Ammoniphilus_sp_YIM_7816-Firmicutes #28b1aa Bacteria
WP_034625643.1-333138-Bacillus_okhensis-Firmicutes #28b1aa Bacteria
WP_081734160.1-1411-Bacillus_akibai-Firmicutes #28b1aa Bacteria
WP_067623968.1-182455-Alicyclobacillus_acidiphi-Firmicutes #28b1aa Bacteria
WP_123920133.1-2014076-Bacillus_sp_FJAT_42376-Firmicutes #28b1aa Bacteria
WP_090236692.1-459525-Fictibacillus_solisalsi-Firmicutes #28b1aa Bacteria
WP_082316246.1-1684141-Bacillus_sp_FJAT_26652-Firmicutes #28b1aa Bacteria
WP_126556950.1-2014872-Dictyobacter_kobayashii-Chloroflexi #28b1aa Bacteria
WP_114597350.1-2282449-Exiguobacterium_sp_RIT59-Firmicutes #28b1aa Bacteria
WP_131972915.1-2183920-Exiguobacterium_sp_B203-Firmicutes #28b1aa Bacteria
WP_088838017.1-2051906-Exiguobacterium_sp_N4_1P-Firmicutes #28b1aa Bacteria
WP_159173283.1-2653141-Exiguobacterium_sp_9Y-Firmicutes #28b1aa Bacteria
WP_041255581.1-1399115-Exiguobacterium_sp_MH3-Firmicutes #28b1aa Bacteria
WP_077319212.1-84407-Virgibacillus_proomii-Firmicutes #28b1aa Bacteria
WP_066235618.1-1458-Bacillus_fastidiosus-Firmicutes #28b1aa Bacteria
WP_125660398.1-1712516-Paenibacillus_baekrokdami-Firmicutes #28b1aa Bacteria
pgl330.24-45779-Papilio_glaucus-Insecta #e21a1c Metazoa
WP_115889230.1-1265740-Flavobacterium_cutihirudi-BacteroChlorobi #28b1aa Bacteria
WP_026729617.1-281361-Flavobacterium_denitrific-BacteroChlorobi #28b1aa Bacteria
WP_144335988.1-1393049-Flavobacterium_daemonense-BacteroChlorobi #28b1aa Bacteria
WP_077922310.1-1955701-Spirosoma_sp_209-BacteroChlorobi #28b1aa Bacteria
WP_081754957.1-44251-Paenibacillus_durus-Firmicutes #28b1aa Bacteria
WP_066377672.1-1850362-Bacillus_sp_FJAT_27264-Firmicutes #28b1aa Bacteria
WP_101634765.1-2053044-Bacillus_sp_V5_8f-Firmicutes #28b1aa Bacteria
WP_139365176.1-304268-Bacillus_alkalitelluris-Firmicutes #28b1aa Bacteria
WP_076346249.1-252246-Alicyclobacillus_vulcanal-Firmicutes #28b1aa Bacteria
WP_035413441.1-1423321-Bacillus_sp_SJS-Firmicutes #28b1aa Bacteria
WP_155111722.1-1491830-Bacillus_mangrovi-Firmicutes #28b1aa Bacteria
WP_151758543.1-2607529-Dictyobacter_vulcani-Chloroflexi #28b1aa Bacteria
WP_126631138.1-2014873-Dictyobacter_alpinus-Chloroflexi #28b1aa Bacteria
WP_064299205.1-1805000-Exiguobacterium_sp_KKBO1-Firmicutes #28b1aa Bacteria
WP_149427954.1-41170-Exiguobacterium_acetylicu-Firmicutes #28b1aa Bacteria
XP_028163132.1-93504-Ostrinia_furnacalis-Insecta #e21a1c Metazoa
XP_028169241.1-93504-Ostrinia_furnacalis-Insecta #e21a1c Metazoa
XP_026750490.1-7137-Galleria_mellonella-Insecta #e21a1c Metazoa
WP_080236875.1-564064-Spirosoma_rigui-BacteroChlorobi #28b1aa Bacteria
WP_080837803.1-1816691-Cohnella_sp_6021052837-Firmicutes #28b1aa Bacteria
WP_077604051.1-582851-Oceanobacillus_sojae-Firmicutes #28b1aa Bacteria
WP_125841241.1-28037-Streptococcus_mitis-Firmicutes #28b1aa Bacteria
WP_025219157.1-1145276-Lysinibacillus_varians-Firmicutes #28b1aa Bacteria
WP_146500593.1-2599619-Planomicrobium_sp_CPCC_1-Firmicutes #28b1aa Bacteria
WP_062307910.1-192387-Alicyclobacillus_sendaien-Firmicutes #28b1aa Bacteria
WP_116278507.1-302167-Virgibacillus_dokdonensis-Firmicutes #28b1aa Bacteria
WP_072741657.1-1911587-Virgibacillus_sp_6R-Firmicutes #28b1aa Bacteria
WP_050349855.1-1473-Virgibacillus_pantothenti-Firmicutes #28b1aa Bacteria
CAB3223843.1-874455-Arctia_plantaginis-Insecta #e21a1c Metazoa
CAB3223885.1-874455-Arctia_plantaginis-Insecta #e21a1c Metazoa
XP_013143111.1-76194-Papilio_polytes-Insecta #e21a1c Metazoa
XP_014367593.1-76193-Papilio_machaon-Insecta #e21a1c Metazoa
XP_034830422.1-2795564-Aphantopus_hyperantus-Insecta #e21a1c Metazoa
XP_023947862.1-110368-Bicyclus_anynana-Insecta #e21a1c Metazoa
XP_032521973.1-278856-Danaus_plexippus_plexippus-Insecta #e21a1c Metazoa
XP_013199825.1-680683-Amyelois_transitella-Insecta #e21a1c Metazoa
Pint013456.1-58824-Plodia_interpunctella-Insecta #e21a1c Metazoa
pse2087.9-40077-Phoebis_sennae-Insecta #e21a1c Metazoa
XP_030025021.2-7130-Manduca_sexta-Insecta #e21a1c Metazoa
XP_037293796.1-7130-Manduca_sexta-Insecta #e21a1c Metazoa
XP_028043978.1-7092-Bombyx_mandarina-Insecta #e21a1c Metazoa
XP_012546333.1-7091-Bombyx_mori-Insecta #e21a1c Metazoa
WP_095927563.1-1975676-Flavobacterium_sp_ACN2-BacteroChlorobi #28b1aa Bacteria
WP_095951485.1-1920426-Flavobacterium_sp_ACN6-BacteroChlorobi #28b1aa Bacteria
WP_113678485.1-2249356-Flavobacterium_sp_HYN008-BacteroChlorobi #28b1aa Bacteria
WP_097128192.1-1597977-Spirosoma_fluviale-BacteroChlorobi #28b1aa Bacteria
WP_109691380.1-378543-Tumebacillus_permanentifr-Firmicutes #28b1aa Bacteria
WP_127531770.1-59841-Paenibacillus_kobensis-Firmicutes #28b1aa Bacteria
WP_161743978.1-2697035-Paenibacillus_sp_T1-Firmicutes #28b1aa Bacteria
WP_127198615.1-2496267-Paenibacillus_sp_3_5_3-Firmicutes #28b1aa Bacteria
WP_149404144.1-2014874-Dictyobacter_sp_Uno17-Chloroflexi #28b1aa Bacteria
WP_104058477.1-2082395-Jeotgalibacillus_proteoly-Firmicutes #28b1aa Bacteria
WP_124007245.1-290335-Tetragenococcus_koreensis-Firmicutes #28b1aa Bacteria
WP_084971590.1-1303-Streptococcus_oralis-Firmicutes #28b1aa Bacteria
WP_100405586.1-2014074-Bacillus_sp_FJAT_45086-Firmicutes #28b1aa Bacteria
WP_110064571.1-665099-Bacillus_oceanisediminis-Firmicutes #28b1aa Bacteria
WP_099805197.1-1421-Lysinibacillus_sphaericus-Firmicutes #28b1aa Bacteria
WP_096364329.1-28031-Lysinibacillus_fusiformis-Firmicutes #28b1aa Bacteria
WP_121661884.1-152268-Bacillus_litoralis-Firmicutes #28b1aa Bacteria
WP_067847940.1-1123961-Alicyclobacillus_mali-Firmicutes #28b1aa Bacteria
WP_041695031.1-405212-Alicyclobacillus_acidocal-Firmicutes #28b1aa Bacteria
WP_073007011.1-411959-Virgibacillus_chiguensis-Firmicutes #28b1aa Bacteria
WP_121640761.1-2419841-Virgibacillus_sp_Bac330-Firmicutes #28b1aa Bacteria
XP_026725181.1-7111-Trichoplusia_ni-Insecta #e21a1c Metazoa
XP_026725182.1-7111-Trichoplusia_ni-Insecta #e21a1c Metazoa
XP_014367600.1-76193-Papilio_machaon-Insecta #e21a1c Metazoa
KPJ02677.1-66420-Papilio_xuthus-Insecta #e21a1c Metazoa
XP_013143723.1-76194-Papilio_polytes-Insecta #e21a1c Metazoa
KPJ02676.1-66420-Papilio_xuthus-Insecta #e21a1c Metazoa
XP_026490834.1-334116-Vanessa_tameamea-Insecta #e21a1c Metazoa
Herato1505.144-1608923-Heliconius_erato_demophoon-Insecta #e21a1c Metazoa
cce11684.1-691633-Calycopis_cecrops-Insecta #e21a1c Metazoa
Pnap023482.1-78633-Pieris_napi-Insecta #e21a1c Metazoa
WP_111290451.1-687844-Flavobacterium_ginsenosid-BacteroChlorobi #28b1aa Bacteria
WP_144213637.1-459526-Flavobacterium_anhuiense-BacteroChlorobi #28b1aa Bacteria
WP_166693642.1-651143-Fibrella_aestuarina-BacteroChlorobi #28b1aa Bacteria
WP_085414219.1-1834519-Fibrella_sp_ES10_3_2_2-BacteroChlorobi #28b1aa Bacteria
WP_091071781.1-1566279-Paenibacillus_sp_NFR01-Firmicutes #28b1aa Bacteria
WP_079409793.1-1469647-Paenibacillus_ferrarius-Firmicutes #28b1aa Bacteria
WP_039914002.1-39650-Cellvibrio_mixtus-Proteobacteria #28b1aa Bacteria
WP_049629647.1-1622269-Cellvibrio_sp_pealriver-Proteobacteria #28b1aa Bacteria
WP_007904747.1-363277-Ktedonobacter_racemifer-Chloroflexi #28b1aa Bacteria
WP_083256069.1-1714016-Domibacillus_iocasae-Firmicutes #28b1aa Bacteria
WP_082084627.1-1017273-Domibacillus_enclensis-Firmicutes #28b1aa Bacteria
WP_103103589.1-51669-Tetragenococcus_halophilu-Firmicutes #28b1aa Bacteria
WP_050208934.1-1313-Streptococcus_pneumoniae-Firmicutes #28b1aa Bacteria
WP_155114686.1-1305-Streptococcus_sanguinis-Firmicutes #28b1aa Bacteria
WP_101781216.1-1274374-Paenibacillus_antibiotico-Firmicutes #28b1aa Bacteria
WP_152961885.1-47500-Aneurinibacillus_migulanu-Firmicutes #28b1aa Bacteria
WP_095478332.1-2015052-Bacillaceae_bacterium_SAO-Firmicutes #28b1aa Bacteria
WP_091838278.1-1155944-Marininema_halotolerans-Firmicutes #28b1aa Bacteria
WP_090852032.1-930152-Bacillus_salsus-Firmicutes #28b1aa Bacteria
WP_034751042.1-127891-Bacillus_wakoensis-Firmicutes #28b1aa Bacteria
XP_021192953.1-29058-Helicoverpa_armigera-Insecta #e21a1c Metazoa
XP_021193506.1-29058-Helicoverpa_armigera-Insecta #e21a1c Metazoa
PCG77019.1-7102-Heliothis_virescens-Insecta #e21a1c Metazoa
JC_0008963-RA-39708-Junonia_coenia-Insecta #e21a1c Metazoa
MCINX002276-RA-113334-Melitaea_cinxia-Insecta #e21a1c Metazoa
HMEL037780g1.t1-171917-Heliconius_melpomene_melpomene-Insecta #e21a1c Metazoa
Hcyd028712.1-33424-Heliconius_cydno-Insecta #e21a1c Metazoa
cce34640.2-691633-Calycopis_cecrops-Insecta #e21a1c Metazoa
cce80816.1-691633-Calycopis_cecrops-Insecta #e21a1c Metazoa
XP_022122719.1-64459-Pieris_rapae-Insecta #e21a1c Metazoa
XP_022122720.1-64459-Pieris_rapae-Insecta #e21a1c Metazoa
WP_126139400.1-2496558-Paenibacillus_whitsoniae-Firmicutes #28b1aa Bacteria
WP_090914225.1-1761877-Paenibacillus_sp_cl141a-Firmicutes #28b1aa Bacteria
WP_095223311.1-2022548-Virgibacillus_sp_7505-Firmicutes #28b1aa Bacteria
WP_093727177.1-361279-Terribacillus_halophilus-Firmicutes #28b1aa Bacteria
WP_036598144.1-1333845-Paenibacillus_sophorae-Firmicutes #28b1aa Bacteria
WP_038693557.1-169760-Paenibacillus_stellifer-Firmicutes #28b1aa Bacteria
WP_047859441.1-48-Archangium_gephyra-Proteobacteria #28b1aa Bacteria
WP_060531032.1-1616788-Paenibacillus_bovis-Firmicutes #28b1aa Bacteria
WP_026297365.1-135193-Paenibacillus_daejeonensi-Firmicutes #28b1aa Bacteria
WP_128657906.1-1117987-Paenibacillus_sp_598K-Firmicutes #28b1aa Bacteria
WP_076231159.1-1920421-Paenibacillus_sp_FSL_H7-Firmicutes #28b1aa Bacteria
WP_138754065.1-1837342-Paenibacillus_sinopodophy-Firmicutes #28b1aa Bacteria
WP_101642664.1-673318-Bacillus_deserti-Firmicutes #28b1aa Bacteria
WP_082029138.1-1508404-Jeotgalibacillus_malaysie-Firmicutes #28b1aa Bacteria
WP_127507394.1-412861-Paenibacillus_humicus-Firmicutes #28b1aa Bacteria
WP_129480313.1-2212476-Fictibacillus_sp_S7-Firmicutes #28b1aa Bacteria
WP_141687062.1-1017270-Fictibacillus_enclensis-Firmicutes #28b1aa Bacteria
WP_157061633.1-71453-Tetragenococcus_solitariu-Firmicutes #28b1aa Bacteria
WP_124696260.1-1850366-Paenibacillus_sp_7197-Firmicutes #28b1aa Bacteria
WP_025677494.1-225917-Paenibacillus_massiliensi-Firmicutes #28b1aa Bacteria
WP_167062810.1-869555-Paenibacillus_aceris-Firmicutes #28b1aa Bacteria
WP_056829956.1-1736411-Paenibacillus_sp_Soil787-Firmicutes #28b1aa Bacteria
WP_154120962.1-2666075-Paenibacillus_sp_LC_T2-Firmicutes #28b1aa Bacteria
WP_146885453.1-401558-Deinococcus_cellulosilyti-DeinocThermus #28b1aa Bacteria
WP_062535140.1-1475481-Mizugakiibacter_sediminis-Proteobacteria #28b1aa Bacteria
WP_129832095.1-2511995-Pseudolysobacter_antarcti-Proteobacteria #28b1aa Bacteria
WP_087798164.1-1978120-Saccharibacillus_sp_O16-Firmicutes #28b1aa Bacteria
WP_069325725.1-1886670-Paenibacillus_nuruki-Firmicutes #28b1aa Bacteria
WP_137223884.1-2184007-Paenibacillus_sp_CFBP135-Firmicutes #28b1aa Bacteria
WP_139996685.1-2583376-Paenibacillus_paridis-Firmicutes #28b1aa Bacteria
WP_141503553.1-2545753-Paenibacillus_luteus-Firmicutes #28b1aa Bacteria
WP_043882194.1-1406-Paenibacillus_polymyxa-Firmicutes #28b1aa Bacteria
WP_082451850.1-1232431-Paenibacillus_ihuae-Firmicutes #28b1aa Bacteria
WP_129542381.1-1404-Bacillus_megaterium-Firmicutes #28b1aa Bacteria
WP_084160282.1-59839-Paenibacillus_alginolytic-Firmicutes #28b1aa Bacteria
WP_081931989.1-64642-Tetragenococcus_muriaticu-Firmicutes #28b1aa Bacteria
WP_123936648.1-526944-Tetragenococcus_osmophilu-Firmicutes #28b1aa Bacteria
XP_021192965.1-29058-Helicoverpa_armigera-Insecta #e21a1c Metazoa
PCG71259.1-7102-Heliothis_virescens-Insecta #e21a1c Metazoa
WP_115993409.1-1294267-Cohnella_lupini-Firmicutes #28b1aa Bacteria
WP_029098111.1-33942-Brevibacillus_thermoruber-Firmicutes #28b1aa Bacteria
WP_036619244.1-44252-Paenibacillus_macerans-Firmicutes #28b1aa Bacteria
WP_128630222.1-2490856-Paenibacillus_oralis-Firmicutes #28b1aa Bacteria
WP_165100220.1-1850370-Paenibacillus_sp_7124-Firmicutes #28b1aa Bacteria
WP_133568040.1-2512134-Paenibacillus_sp_BK673-Firmicutes #28b1aa Bacteria
WP_028592339.1-363858-Paenibacillus_panacisoli-Firmicutes #28b1aa Bacteria
WP_127684993.1-2499626-Rheinheimera_sp_YQF_1-Proteobacteria #28b1aa Bacteria
WP_144989219.1-2527964-Planctomycetes_bacterium-Planctomycetes #28b1aa Bacteria
WP_014086431.1-748280-Pseudogulbenkiania_sp_NH-Proteobacteria #28b1aa Bacteria
WP_008955265.1-549169-Pseudogulbenkiania_ferroo-Proteobacteria #28b1aa Bacteria
WP_116187842.1-1156355-Paenibacillus_taihuensis-Firmicutes #28b1aa Bacteria
WP_132483337.1-2512154-Paenibacillus_sp_BK736-Firmicutes #28b1aa Bacteria
WP_090578257.1-1884377-Paenibacillus_sp_OV219-Firmicutes #28b1aa Bacteria
WP_126020332.1-2495582-Paenibacillus_albus-Firmicutes #28b1aa Bacteria
WP_157060109.1-459527-Saccharibacillus_kuerlens-Firmicutes #28b1aa Bacteria
WP_088487407.1-2009338-Saccharibacillus_sp_O23-Firmicutes #28b1aa Bacteria
WP_108464248.1-1532905-Paenibacillus_sp_CAA11-Firmicutes #28b1aa Bacteria
WP_148505216.1-1126833-Paenibacillus_beijingensi-Firmicutes #28b1aa Bacteria
WP_134755087.1-1967502-Paenibacillus_sp_MEC069-Firmicutes #28b1aa Bacteria
WP_166152408.1-2716264-Paenibacillus_sp_S3N08-Firmicutes #28b1aa Bacteria
WP_166024810.1-1178594-Bacillus_sp_C11-Firmicutes #28b1aa Bacteria
WP_094939080.1-484184-Paenibacillus_taichungens-Firmicutes #28b1aa Bacteria
WP_079348373.1-1962644-Paenibacillus_sp_VT_16_8-Firmicutes #28b1aa Bacteria
XP_035433165.1-7108-Spodoptera_frugiperda-Insecta #e21a1c Metazoa
KAF9420975.1-7107-Spodoptera_exigua-Insecta #e21a1c Metazoa
XP_035433131.1-7108-Spodoptera_frugiperda-Insecta #e21a1c Metazoa
WP_148929897.1-582686-Paenibacillus_methanolicu-Firmicutes #28b1aa Bacteria
WP_167195742.1-2587092-Paenibacillus_sp_BK720-Firmicutes #28b1aa Bacteria
WP_132303976.1-2512133-Paenibacillus_sp_BK033-Firmicutes #28b1aa Bacteria
WP_085170576.1-903526-Paenibacillus_sp_J6-Firmicutes #28b1aa Bacteria
WP_168129905.1-1850368-Paenibacillus_sp_7028-Firmicutes #28b1aa Bacteria
WP_084266618.1-365617-Paenibacillus_sabinae-Firmicutes #28b1aa Bacteria
WP_127453205.1-59842-Paenibacillus_chondroitin-Firmicutes #28b1aa Bacteria
WP_157319760.1-2682845-Paenibacillus_sp_MAH_34-Firmicutes #28b1aa Bacteria
WP_145666809.1-2587047-Paenibacillus_sp_597-Firmicutes #28b1aa Bacteria
WP_161408697.1-2606219-Paenibacillus_sp_5J_6-Firmicutes #28b1aa Bacteria
WP_061720016.1-446-Legionella_pneumophila-Proteobacteria #28b1aa Bacteria
WP_028206267.1-392320-Paraburkholderia_nodosa-Proteobacteria #28b1aa Bacteria
WP_089133527.1-2584094-Sphingorhabdus_sp_SMR4y-Proteobacteria #28b1aa Bacteria
WP_100095429.1-2077182-Sphingorhabdus_sp_YGSMI2-Proteobacteria #28b1aa Bacteria
XP_035432939.1-7108-Spodoptera_frugiperda-Insecta #e21a1c Metazoa
WP_119600002.1-393251-Paenibacillus_nanensis-Firmicutes #28b1aa Bacteria
WP_155605077.1-225915-Paenibacillus_timonensis-Firmicutes #28b1aa Bacteria
WP_028538168.1-935845-Paenibacillus_sp_J14-Firmicutes #28b1aa Bacteria
WP_085278166.1-343517-Paenibacillus_barengoltzi-Firmicutes #28b1aa Bacteria
WP_083953175.1-209389-Bacillus_acidicola-Firmicutes #28b1aa Bacteria
KAF9420976.1-7107-Spodoptera_exigua-Insecta #e21a1c Metazoa
XP_022830867.1-69820-Spodoptera_litura-Insecta #e21a1c Metazoa
WP_013918226.1-61624-Paenibacillus_mucilaginos-Firmicutes #28b1aa Bacteria
WP_079908823.1-1969111-Paenibacillus_sp_32352-Firmicutes #28b1aa Bacteria
WP_068617779.1-1816681-Paenibacillus_tuaregi-Firmicutes #28b1aa Bacteria
WP_095265627.1-66347-Paenibacillus_campinasens-Firmicutes #28b1aa Bacteria
WP_021298374.1-1450-Alicyclobacillus_acidoter-Firmicutes #28b1aa Bacteria
WP_101591514.1-2054166-Bacillus_sp_M6_12-Firmicutes #28b1aa Bacteria
WP_028395869.1-1208600-Bacillus_sp_FJAT_14578-Firmicutes #28b1aa Bacteria
WP_154308885.1-1983721-Bacillus_lacus-Firmicutes #28b1aa Bacteria
WP_148457737.1-862114-Paenibacillus_faecis-Firmicutes #28b1aa Bacteria
WP_074100085.1-1349435-Paenibacillus_sp_P3E-Firmicutes #28b1aa Bacteria
WP_095288808.1-2022549-Paenibacillus_sp_7516-Firmicutes #28b1aa Bacteria
WP_076121840.1-189426-Paenibacillus_odorifer-Firmicutes #28b1aa Bacteria
WP_148970830.1-189382-Bacillus_aquimaris-Firmicutes #28b1aa Bacteria
WP_098438429.1-1761763-Bacillus_sp_es_034-Firmicutes #28b1aa Bacteria
WP_117323374.1-2303991-Bacillus_glennii-Firmicutes #28b1aa Bacteria
WP_078429602.1-427920-Bacillus_alkalinitrilicus-Firmicutes #28b1aa Bacteria
WP_094598082.1-2026089-Paenibacillus_sp_XY044-Firmicutes #28b1aa Bacteria
WP_074088327.1-1349434-Paenibacillus_sp_P32E-Firmicutes #28b1aa Bacteria
WP_074110196.1-1349436-Paenibacillus_sp_P46E-Firmicutes #28b1aa Bacteria
WP_154892761.1-528191-Paenibacillus_xylanexeden-Firmicutes #28b1aa Bacteria
WP_083392276.1-1678001-Bacillus_sp_MUM_13-Firmicutes #28b1aa Bacteria
WP_090902741.1-1884379-Paenibacillus_sp_OK076-Firmicutes #28b1aa Bacteria
WP_152399504.1-562959-Paenibacillus_cellulositr-Firmicutes #28b1aa Bacteria
WP_095360895.1-2022550-Paenibacillus_sp_7523_1-Firmicutes #28b1aa Bacteria
WP_110821560.1-59845-Paenibacillus_illinoisens-Firmicutes #28b1aa Bacteria
WP_116232942.1-2135608-Paenibacillus_sp_VMFN_D1-Firmicutes #28b1aa Bacteria
WP_145161637.1-159743-Paenibacillus_terrae-Firmicutes #28b1aa Bacteria
WP_105445813.1-1631599-Paenibacillus_sp_AR247-Firmicutes #28b1aa Bacteria
WP_163880214.1-221028-Paenibacillus_favisporus-Firmicutes #28b1aa Bacteria
WP_145138780.1-481743-Paenibacillus_sp_Y412MC1-Firmicutes #28b1aa Bacteria
WP_089549239.1-1443669-Paenibacillus_sp_SSG_1-Firmicutes #28b1aa Bacteria
WP_076172631.1-297318-Paenibacillus_rhizosphaer-Firmicutes #28b1aa Bacteria
