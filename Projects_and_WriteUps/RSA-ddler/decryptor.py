import sympy
output=[12331, 329796147429, 74123515046928094799825188664648897435800820530055170843191646450844356103736, 43902742405476161131473929002315604273, 12944, 27735580683, 78973387595019170784612458521728960323264867786515401685321385965026793856403, 31919992337066015048720993940025631713, 2347, 734847565824, 101271357811948351746604313864755895370188204420625050803278149660722073946239, 56349663930743838272275153491291168002, 8982, 2328310511064, 106058552522508819565468995006183368211991722056203258411598135921256264292248, 51792942655418674841644497405567291075, 11875, 384399163511, 35616979992135835717966741760639566123331219536421186604525024997159995343459, 40823011766295422493409073278264153576, 9039, 1129412837944, 49932432102491735682672329915063718414997565757845935029236989016277672292325, 13039422778599220469692552984865152667, 9053, 2181825073000, 84112885952588821792250635403984208020788974809389408663739568743119424997740, 30474861076101697076037209063127855525, 10835, 2430426096125, 11951553580270835032619325940480717483281377890052128849411588756090281688706, 63745756952654317830500039851174786720]
file=open("./2.txt",'w')
n=2140324650240744961264423072839333563008614715144755017797754920881418023447140136643345519095804679610992851872470914587687396261921557363047454770520805119056493106687691590019759405693457452230589325976697471681738069364894699871578494975937497937
for i in range(0,len(output),4):
    s=str(i)+'\t'+str(round(output[i]%n))+'\n'
    print(s)
    file.write(s)
file.close()