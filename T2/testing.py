#construyo la delone clasica, con los puntos y los vertices de las aristas restringidas
#duda 1: si una arista partia en un punto de la triangulacion ese vertice va a estar dos veces? 
#duda: que pasa si se ingresan dos puntos iguales en mi wea 

#van a quedar aristas no respetadas 
#quiero que aparezca esa arista en la triangulacion 
# como hago para que se respete esa arista? 

# la q me interesa como solucion es usar intercambio de diagonales, operacion que conocen 
# para respetar la arista 

#tengo una direccion parto de a a b 
# tomo los dos primeros de la lista, genero haciendo intercambio de diagonales 
# voy a generar dos triangulos 
# uno abajo uno arriba sigo trbajando con el triangulo que pinte en verde 
# ahora genere este nuevo triangulo t1 y tengo t1 con t2 ahora 
# hago un nuevo intercambio de diagonales entre estos dos 
# avanzo de a pares 
# voy a generar 
# pizarra borrando asi podria hacerse facil po 
# en los ultimos dos se intercambia y queda respetando la arista 

#avanzo por pares 
#conj de triangulos que van cortando la arista 
# con t1 t2 intercambio diagonales
# me queda un triangulo q aun corta la arista, tomo ese con el siguiente del conjunto 
# intercambio de diagonales y asi sigo hasta que quedan solo dos y ell ultimo intercambio respeta la arista
# perooo ? estan en orden los triagulos? 
# osea no puedo hacer intercambio entre el primero y el ultimo seria la media caga 
# como detecto y ordeno los triangulos que cortan la arista??

#esto es un post o durante? 
# es un post proceso pq yo construyo primero delone clasica de los puntos incluidos los vertices de las aristas 
# cone so tego ua triangulacion q no respete las aristas 

#si no esta respetada encontrar los triangulosque interceptan la arista 
#post proceso para respetar la arista 


#pensando enla tarea 
# seria eso unp post proceso
# hacer la triagulacion de deloe 

#los vertices para q aparezcan como puntos de la triangulacion 
# SI UNO ESTABA DE ANTES QUE PASA 

#pero falta lo deee si esta detro o fuera de la wea si tiene hoyos y asi ono 
#hay q como q pitearse a esos de afeura 

# conj de triangulos t1 t2 tn  que cortan la arita 
# parto de t1 t2 hago intercambio de aristas 

# cuando hago el intercambio echo anperdee en calidad 
#alreves que necesito en deloe clasica 
#intercambio de delone restringida no vaa ser tan 
#no va a ser tan buena como la delone 

#uno de edsos dos solo uno va a cortar la arista, ese es el q va con el siguiete e intercambio 

#no estaos itroduciendo puntos 
#q bacan las propiedades de cambiar las diagonales 

#esto tiee un probelma  pq todo tieee problemas nadaes perfecto  >:C 

#AYNO Q PASA SI NO FORMAN CUADRILATERO CONVECSO 
#eso no pasaria pq la wea era deline o no jj 

#si h ago intercambio obtengo triangulacion no valida 
# me toi saliendo del poligono formado 
#lo q hacemos en ese caso si t1 y t2 o pareja del camino 

# no son localmente 
#no forman una figura convexta 
# me salto el triangulo t1 
# y hago el intercambio entre t2 y t3 

#y si esos tbm se salto de t3 a t4 yo creo po 
#cuando salto de e intercambio 
#el nuevo con el primero 
#parto de nuevo de a a b ahi podre hacer el intercambio de diaognales 

#ya a ver primero 
#me salto el t1 
#intercambio los sig 2 
#luego 
#cuando h ago el entre t2 y t3 

#tengo ahora el t1 y un nuevo 
#t 2', es el de abajo no se como elegir entre los dos nuevos 


#pero no importa porque se parte de nuevo entre a y b 
#osea de al ppio
#pero ... entonces los nuevos hay que ingresarlos al grupo de triangulow 
#en que orden? sitego  que saber cual de los dos nuevos es el t2' 

#como??

#segudo how dela noche 

#para el de la atarea q hacemos 
#primero tiene razon 
#valeria y bea de q el respeto de arista lo vamos a hacer como un post proceso 
#vamos a construir la triangulacion clasica de los puntos yvamos a agegar los vertices de la arista para que cuando respetemos la arista la arista este formada por dos vertices de la triangulacion 

#revisamos si la arista esta en la triangulacion si esta no tengo que hacer nada fue respetada de manrera natural 
# si no esta encuentro esta secuencia ordenada de triangulos que corta la arists de sde a a hasta b 

# por pares veo si puedo hacer intercambio de diagonales 
# llo hago (si se puede por weas no conveas)

#quedara un solo triangulo de esos dos nuevos que ocrta la arista 
#veo cual es y el otro se ovida ya esta lito 
#ese q era con el siguiente ahaora 

#con ese y con el sig ago intercambio d diagonales
#cuado tenga solo 2 q cortan al hacer el cambio erspeto la arista 


#cuidado en el cmino de q si me encuentro con un par de triangulos 
#que no forman una figura conveca no puedo cambiar de diagoanles 
# me olvido del primer triangulo 
#y hago el segundo con el sig 

#en la secuencia,,, se puede mostrar de quebbueno 

#repetir el proeso 
#si me quedaron triagnulos parto denuevode a ab conl os que quedaron 
# no pasa mucho 

# de los 2 y 3 que haci como sabi cual de los nuevos va ates:(( 
# 
# how 3))

#si ya tengo restringida y quiero agragr u pinto, problema distinto ,creo 
#q ese no hay que hacerlo cierto ?

#agregar un punto usar el test del circulo restringiod 
# preguntar 
#tendria que agregar a la estructura de datos 
#podria argegarlo delone y dsps post proceso 

#o agregarlo directamente restrinido 

#cong de arists restringidas neuvas 
#se repite el post proceso 
#triagulo guardar indo en las arisats si son o no .- . no como el pico eso 


#guardar el cjto de aristas restringidas mejor 

#cuanto toi haciendo el test del circulo restringido
#toi haciendo el test del circulo restringido me encuentro con q tengo una arista ab restringidad y quiero agregar el punto d 
# resrtingido 
#agrego ese triangulo el adb 
#no acepto el intercambio de diagonales 
#tener una tiangulacion un poco peor pero es ua de delone restringida con respectoa esa arista
#para agregar putos considerar el test del circulo restringido

#como q es preguntar si la q tengo que matar es restringida o no?
#pregunto eso antes de hacer el test y ya¿ 

# bueno eso es lo q necesitan para la tarea 
# para la tarea de triangulacion de delone restringida 
# hacer unn post proceso de respeto de aristas
#lo otro no cierto?
# hay otros problemas 
#consideremos el problema siguiente 
# what 
#esto sera tarae o no 
# quiero construir la aaa chucha el hoyo

#ya obj con hoyo 
#siempre estamos hablando de 2d 
# poligono ocn bordes poligonales y tiene en el interior una perforazion que no necesita ser triangularizada q tbm es un poligono 
# como lo haceemos? 


# ctm me ahogo 
# como se modela un poligono 
# what 
# en ese sentido se pueden usar los vertices pra representarla no¿ 
#puedo usar los vertices ordenados ahi los ordene 
# para modelarlo 
#b1b2 una arista b2b3 una arista 
#si los tengo desordenados no tengo informacion 
#tambien tengo que hacer un post proceso de respeto de arista 
#delone de essos vertices y post proceso de respeto de arista 

#en q sentido respeto de aristas lo q hicimos po beltran 

#hago lo delone de lso vertices y me queda una wea q no respeta esas aristas restirngidas

#nuestras weas deberian soportar hoyos??? pq pa eso si o si hay q hacer algo aparte 

#seria como esa la triangulacion de delone 
#no esta respetando el obj 

#lo q tengo q hacer es hacer 
#usar un algoritmo 

#como primer paso construyo la triangulacion de delone clasica de los vertices 
# y despues respeto las aristas 
# cuando tengo un poligono se hace un proceso en orden 
#veo si b1 b2 esta y la respeto 

#con eso voy a tener 
# una triangulacion q respeta el objeto 
#si hago eso con mi ejemplo 

#voy a tener triangulos por dentro por fuera, otro problema 
# empezar a eliminar aristas?
# delone restringida del obj y dsps como siguiete post proceso sacar los triangulos que esta por fuera del objeto 
#omg sii 
# lo puedes ver como eliminar aritas
#olo q hago es scacar esos tianuglos 

# considerando q tuvieramos un arreglo de los triangulos despues solamente ahora me puedo im<ginar q es alinear por ese arreglo para ir revisando q queden fuera del obj o no 
#hay algua forma de saber 

#seguir el borde del poligonos 

#no revisaria sobre todos los triangulos 

#sobre los q tienen una arista sobre el borde 
#veria si los triangulos que comparten esa arista estan por fuera o por dentro del objeto 
#tenemos que pesar 
#yo iba un poco a eso 
# si yo recorro 
#ordenado 
#yo aqui puse los verties 

#si  yo lo recorro ordenado voy de bq a b2 
# se q el interior del obj esta a la izquierda 

# ahh si po siepre 

#el orden de los vertices cuando describo el poligono es importante 
#se que cuando me muevo recorriendo los vertices que forman aristas
#v2 v6 no forman una asista 
#son ordenados 
#de b1 a b2 
#voy caminando a mi izq esta el interior del obj 

#lo uso pa eliminar los tringulos de afuera 

#ahora tenemos otro probelma 
#si tengo un 
# poligono interior

#yaaa tenique ver las aristas restringidas 

#pero si es ua arista dentro omas q no ipliaca hoyo ahi izq es adetro pero derechatbm ??? 
#HOW NO SE Q 

#hueco q no es parte del obj  
#lo q yo hago ahi es describir los poigonos interiores se describen usando el  otro orden 

#los interiores usando el sentido de los punteros 

#osea este obj de ahi 
#va a tener el orden al reves 
# tengo el obj el poligono interior descrito en el otro sentido 
# y con esa convencion cuando yo recorro los vertices del poligono interior sigo teniendo a mi izq el inerior de un obj 

# enotnces como uf ven #esto de
#estos pronlemas son bien importantes 
#DIFIciles de ascar 
#sw q resuelven problemas de ing arquitectura dd tengo objq tienen q ser respetados 



#si yo tengo un poligono interior 
#hueco vacio no parte del obj 

#si yo tengo un poligono interior 
# q es u hueco esta vacio no es parte del obj 
# si triangulo tbm voy a tener triangulos en el interior del poligono q tienen q ser eliminados 

#entonces se escriben en ese sentido el otro en el otro sentido 
# 
# # poligono exterior en un sentido, puede haber mas de un interior 
# # ahora lo que yo puse en esa tarea dado un ocnj de aristas no esta el 
# eestos probelams de eliminar 
# respetar encontrar una triangulacion delone restringida del objeto 
# y de eliminar los trianguls q on estan en el interior del obj no es parte d ela tarea 
# a ver
# volver un poco 
# tu querias q repitiera no se q mierda 
# yo estaba explicando de q es posible que me encuentre co un caso patologico en q yo tenga 
#  yo quiero respetar esa arista de abajo
# 3 triangulos que curzan 
# tecnica de intercambio tomo el primero y el siguiente pero no peudome voy  salir del obj generar 
# tiranuglacion no valida 
#t1 t2 t3 
# en vez de hacer intercamvio etre t1 t2 hace entre t2 t3 
# forrman una figura convexa" 
# cuado hago el wea este nuevo triagulo que forme aca 
# corta la arista 
# y forma unafigura convexa co este t1 t' 
# intercambio diagonals y genero estos dos triangulos fiales 
# que son
# son esos dos rojos 
# en este ejemplo entre los dos tiangulos finales hayuno bien malo
# si introduzco puntos meidos podria obtener  una mejor tirangulcion q esa 
# estos problemas de respetar aristas respetar poligonos puedo respetar poligonos interiorees 
# yo puedo tener cambios de materia
#l no necesariamente un hueco
# un hoyo cambio de amterial y esa interface en los cambios de material tieneq ser respetado 
# uedo tener obj q tengan cmabio de material aqui estos 
# restricciones sobre la geometria 
# se le llama triangularizar tslg 
# PSLG esto biene el ingles 
# grafo de linea recatasfdkjgfdj plantar streit line grafo 
# problemaes en q mis datos sea como los problemas sea q tengo un poligono aristas restringidas puntos restringidos 
#q tienen q ser respetados 
#como q puntos 
# ud ven q puedo estar generando trianguos bien malos 
# problema q sigue como hago para mejorar una triangulacion 
# dleon clasia o para mejorar una restringida 

# probablemente el trianguo q ta generando yo ahi no sea aceptable hacer algo pa mejorarlo 
# a eso va el tercer porblema que esta puesto en 
# como tarea 
# nosotros ya vimos que 
# no se 
# a ver imaginense  que yo tenga 
# dos circulos discretizados 

# circulo discretizados van a ser poligonos 
# teno un circulo  
# q ddefine ele borde ecterior y el interior q tiene una perfonariozn 
#triangulacion delone restringifa horrible 
# estoy sacando le tuve que sacar los triangulos fuera dle obj 
# al interior del hueco tambiene +
#esta triangulacion
# mas o menos si 
# esa deberia ser la rtiangulacion q fea 
# desde el punto de vista de la aplicaciones es muy mala 
# necesito ahi pa mejorar esa triangulacion 
# mas puntos 
# agragr puntos necesito agregar puntos 
# la distribucion de putnos es mala 
# es la mejor triauglacion q uedo generar 
# es la mejor posinle dados los datos 
# # si tengo 4 datos qe definen un rectangulo finito 
# # mi mejor tirnauglacion va  atener dos trianuglso bien malos 
# #agegarr mas puntos sobres las aristas q es lo que mas me convendia ahi 
# aqui mas untos al interior del obj me conviene eno en las aristas 
# esta es unamotivacion apra loq  voy a presentar en la proxima clase
# duda
# en el 
# no se si puede volver a mostrar esa figurita q era como una especie de u 
# ensando q al eliminar los q estan dentro de esta u 
# yo tendria q eliminar el proximo 
# caso q quede una isla 
# pq si yo elimino los q estan a la iz 
# yo no puedo tener triangulos q esten en parte dentro y en parte fuera del obj 
# ahi dd tengo la 
# ahi tengo quehacer el trbajao de intercambio de aristas 
# ver como me resulta esto 
# mi pregunta es con el segudo 
# acudnao se eliminan los que quedan dentro del hoyo 
# si voy bajanado
# cuenta reloj vengo del cacho de la derecha bajando eliminar a mi dereca 
# el trianuglo directo contra la derecha si sigo me tompo con el otro cacho 
# triangulos q no debo eliminar 
# si esa es mi duda 
# 
# pueda quedar triagulos como entre os dos cachos como al medio 
# ah si po 
# cuando yo haga respeto de aristas 
# es complicado aca 
# cuando haga intercambio de aritsas a atener ext e interiore s
# pero ira cahca
# no  hay punto al medio 
# no puede quedar un triangulo a ams de un triangulo dedistancia de la wea porque 
# significaria q hay un punto ahi lotando po y si eso esta fuesra no puede ser  

# tengo q identificar los trianuglos q estan en el interior 
# es complicado aca pq tienes dos borddesyy pero si te vas moiendo en orden vas sisuitendo la definicion del poligono 
# va a resultar 
# ddigamos 
# dsjgfk aver a ver 
# detalle detalle pero esto funciona 
# tu dices q teestas moviendo 
# hizo u respeto de bordes hay dos triangulos fuera del obj
# vas por el borde y sacas el de a izq si 
# de b2a b3 lo mismo 
# tengo el exterior del obja mi derecha 
# ese triangulo tbm esta en el interior y lo saco
# ahi hay q ser cuidadoso con conseguir los vertices ordenados 
# con las convencioes que estoy usando 
# si yo quisiera sacar 
# tengo un poligono interior 
# tengo que saacar los triauglosos en el interior del oligono interior pq no perteneces al obj 
# uso la cnonvencion al reves describiendo vertices pal otro snetido pero funciona 
# bueno a ver 
# nosotros sabemos q estamos porq nosotros decidimos asi 
# sabemos que 
# la arista restringida esta definida por dos vertices de la triagnulacion 
# parto encontrando un trignualo que tiene uno de esos verties  que corta 
# que corta la arista digamos 
# puedo usar otra manera 
# 
# puedo usar 
# no ecesariamente tengo que usar intersecciones 
# tengo que identificar unt irnauglo que contiene al vertice a y q es cortado por esa arista 
# sigo por los vecinos de ese triangulo encontrando los q cortan la arista 
# se entendio? 
# omo encentras un primer triangulo que corta la arista 
# tendras que recorrer 
# es unpost proceso que se hace una sola vez y no 

# a ver 
# hay alguna forma facil de saber por que trianuglos pasa la arista restringida 
# SII ESTE ES MI HOW 
# encontrar los triangulos q la cortan 
# bueno a ver sabemos q estamos nosotros lo decidimos asi 
# sabemos que la arista restringida esta definida por dos vertices de la trianglacion 
# parto encontrando un triangulo que tine uno de esos vertices 
# y q corta la arista digamoss... ???? puedo ousar otra manera 
# no necesariamente usar intersecciones 
# identificar un triangulo q contiene al vertice a y que es cortado por la arista 
# vecions de ese triangulo encontrando los q cortan la aritsa  osea
# como encuentras el primer tringulo 
# recorrer... 
# pos proceso q se hace una sola vez y no necesita
# puedo optimizar y en una pasada encontrar todos los triangulso q tienen un vertice de cada arista como jkfnd 
# 
# tengo una arista q quiero q se respete 
# se que esa arista esta definida por dos verties de la triangulocacion 
# 
# 
# enuentro el conj q comparten ese vertice 
# encuentro el q corta la arista y sigo por sus vecinos hasta encontrar el  triangulo del otro vertice 
# 
# sipo pq tienen q esstar ordenados 
# en realidad lo q necesitan es el test de la orientacin para moverse 
# no necesitan calcular intersecciones 
# 
# tienen un sw q implementaron 
# q es un algoritmo casi delone 
# no implementaron la uncion recursiva 
# delone clasico 
# no necesitan imlementar el delone completo 
# 
# basta con q usen el sw q ud implementaron 
# este es un 
# una apuesta xd q  
# hacer un respeto de arista sobre eso cmo funcinoara eso  
# deberia fucionar 
# tenian q e esta tarea tenian q implementar el delone completo 
# pero creo q niisquiera es necesario 
# es necesario q este funcionando la tarea anterior 
# el delone con un intercambio de diagonales pero q eso este funcionando 
# 
# y a eso introducir la parte de las aristas restringidas 
# comprobar q haya funcionado lo de restriccio de arista basta con q ver q las 
# weas queden bien delimitadas 
# mitchel dice q eso se puede comprobar en codigo 
# pero es dificil 
# se puede hacer 
# en realidad para todas las coas se pueden hacer validaciones 
# pueden ser caras pero no importa pq es fuera del costo del algoritmo 
# lo pueden hacer para la tarea 
# pero si  mas q todo me preocupaba de geometrias simples no cosas muy grandes 
# con miles de aristas restringidas o cosas asi 
# siempre partan con prolemas chicos en q uno pueda hacerlo a mano 
# una foto verle las aristas y wea 
# 
# libreria de dibujo ara colocarle a las aristas restringidas 
# con matplotlib no recuerdo 
# 
# todo se ´puedkfkjddfk  





