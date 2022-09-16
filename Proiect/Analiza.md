## Descriere studiu

Studiul urmărit prezintă o perioada extinsă din care au fost extrase datele dar pentru simplificare majoritatea factorilor sunt din anul 2010. Variabilele folosite conțîn date despre un hotel ales aleatoriu aflat în capitală uneia dintre cele 80 de țări care participa la studiu și un prim review al acestuia colectat de pe TripAdvisor.com. Țîn să menționez că rating-ul colectat nu definește calitatea țării respective, și, că in orice altă țară, există o multitudine de factori care pot afecta acest rating precum: un client nemulțumit, alegerea unui hotel care nu îndeplinea anumite criterii și care nu mai există la momentul actual, perioada in care a fost lăsat review-ul etc. 

Analiză factorilor se va face în funcție de variabile care țîn de hotel și variabile ce țîn de destinație. Primele au fost descrise mai sus, așa că in continuare voi vorbi despre analiză destinației unde voi utiliza variabile precum GDP (PIB) și variabilele dimensiunii culturale ale lui Hofstede.

Variabilele lui Hofstede descriu efectele culturii unei societății asupra valorilor acesteia, și cum aceste valori se referă la comportament. De asemenea, variabilele fac parte dintr-o teorie cu același nume care este derivată din analiză factorială. Modelul lui Hofstede constă în 6 dimensiuni prezentate prin 6 variabile: indexul distanței puterii, individualism versus colectivism, masculinitate versus feminitate, indexul evitării incertitudinii, orientarea pe termen lung versus orientarea pe termen scurt și indulgență versus reținere. În continuare voi prezența câteva detalii despre fiecare variabilă.

**Indexul distanței puterii („power distance index”) (PDI)** reprezintă felul în care o societate gestionează inegalitățile dintre persoane. Oamenii din societățile cu un index ridicat acceptă o ordine ierarhică în care fiecare persoană are un loc al sau. Pe de altă parte, în societățile care prezintă un index scăzut, oamenii încearcă să egalizeze distribuția puterii.

O societate în care legăturile dintre indivizi sunt slabe, unde fiecare îi pasă numai de sine ori doar de familia să prezintă un **individualism (IDV)** ridicat. Societățile individualiste pot părea reci, de la climă la o dispunere întinsa a orașelor ori interacțiuni rezervate între persoane. 

**Masculinitatea (MAS)** reprezintă preferința unei societăți către realizări, eroism, asertivitate și recompense materiale pentru succes. Opusul sau, feminitatea, arată preferința pentru cooperare, modestie și grijă pentru cei slabi.

**Evitarea incertitudinii (UAI)** exprimă nivelul la care membrii unei societăți se simt amenințați de incertitudine, ambiguitate și situațîi necunoscute. Țările cu un index ridicat nu tolerează ideile și comportamentul neortodox. Pe de altă parte, țările cu un index scăzut au o atitudine mult mai relaxată, încearcă să evite conflictul și caută siguranță în reguli.

**Orientarea pe termen lung (LTO)** denotă legătura unei culturi cu trecutul și acceptarea viitorului. Societățile cu un nivel scăzut preferă să mențină tradițiile și le este greu să accepte schimbarea. Pe de altă parte, cele cu un nivel înalt încurajează economisirea și eforturile către o educație modernă că un mod de a se pregăti pentru viitor.

**Indulgență (IVR)** arată tendința unei societăți de a permite satisfacerea relativ liberă a nevoilor umane de baza și naturale ce țin de nevoia oamenilor a se bucură de viață și a se distra. Pe partea opusă, reținerea prezintă o societate care suprimă aceste nevoi și le înlocuiește cu norme sociale stricte.

Observațiile sunt reprezentate de un număr de 80 de țări considerate unele dintre principalele destinații turistice urbane la nivel mondial.

![image](https://user-images.githubusercontent.com/76962878/190699798-fba97d72-32d5-428e-9141-4bfb5eeed2bd.png)
 
>Figură 1: Țările incluse în studiu (cu negru pe hartă)

## Analiza Exploratorie a Factorilor
Pentru analiză datelor voi folosi analiză exploratorie a factorilor. Această metodă este proiectată cu scopul de a identifica relațiile de baza dintre variabilele măsurate. Ajută la interpretarea datelor prin reducerea numărului de variabile înainte de a construi modelul de analiză. Totodată, va extrage variația comună maximă din toate variabilele și le va pune într-un scor comun.

După cum spune și numele, această analiză e folosită pentru cercetarea factorilor care afectează un anumit domeniu, o rată, o țară etc. Astfel, obiectivul meu va fi să conduc o analiză care în final să îmi arate dacă factorii aleși produc sau nu o variație în satisfacția clienților din industria hotelieră.

Pentru o prima modelare a datelor se va realiza o corelogramă cu toate variabilele pentru a vedea care dintre ele nu sunt folositoare analizei aflată în desfășurare ori dacă variabilele prezintă o corelație mult prea mare unele cu altele.

Am ales analiză exploratorie a factorilor pentru acest studiu deoarece față de alte analize, modelul este mult mai conceptual și permite existența variabilelor latente (așa numiții factori). În domeniul de studiu ales - satisfacția clienților din industria hotelieră - e necesar să înțeleg cum diferiți factori influențează variația dintre variabile și dacă acestea produc o creștere/scădere a satisfacției, de aceea o analiză precum AEF e mult mai captivantă decât o altă.

## Rezultate

* ### Corelograma indicilor KMO

![image](https://user-images.githubusercontent.com/76962878/190699859-5727731f-f55a-4a40-b8d7-8ec40a679552.png)

>Figură 2: Heatmap KMO index

Din corelograma indicilor KMO putem află care este factorabilitatea valorilor principale. Valorile mari regăsite în diagramă (peste 0.6 - reprezentate cu albastru închis) reprezintă prezența unei corelații puternice între valorile analizate. De exemplu, pot spune că o mare majoritate a factorilor mei (în număr de 13) au potențial de a deveni factori principali în analiză. 

Una dintre cele mai puternice legături se regăsește la ratingul calității somnului pentru hotelele analizate. De aici reiese că satisfacerea unui client e foarte conectată cu confortul primit în țară pe care o vizitează, și nivelul de odihnă de care are parte. Pe de altă parte, valoare PIB-ului precum și indexul pdi („distanță puterii”) joacă un rol la fel de important în ratingul final oferit hotelului, deci satisfacția clientului. Un PIB ridicat poate însemnă că țară vizitată este una dintre primele alegeri ale călătorilor, turismul având un rol foarte important în economia unei țări. Indexul pdi arată inclinația turiștilor de a pune accentul pe tipul de conducere și problemele politice a unei țări, înainte de a face alegerea unei vizite în țară respectivă. Astfel, valoarea ridicată arată cum instabilitatea unei țări și felul cum această pune valoare pe egalitatea dintre persoane poate afecta zona turistică a acesteia.

* ### Varianța factorilor
![image](https://user-images.githubusercontent.com/76962878/190699970-17029732-1545-4c29-a8d1-a9939592d847.png)

>Figură 3: Tabel varianța factorilor

Pentru a știi de câți factori avem nevoie pentru analiză, ne vom uită la valorile proprii, ori așa numitele eigenvalues, care ne vor arată cât de mult varianta variabilelor este explicată de un factor. De exemplu, primul factor are o variație de 3.7 ceea ce înseamnă că factorul poate explică variația a 3.7 variabile.

Pentru estimarea numărului de factori voi folosi testul Bartlett. Vom acceptă drept factori acele variații cu un nivel mai mare decât rezultatul testului. Testul Bartlett cercetează ipoteza nulă care verifică dacă matricea de corelație este una identică adică presupună că nu există corelație prezența între variabile.

Pentru a respinge ipoteza nulă vom arată că valoare lui p statistic este mai mică decât 0.05, deci afirmăm că există corelație între variabile cu un nivel de încredere de 95%.

Ponderea prezintă procentul de variație acoperit din variația totală pentru fiecare valoare în parte iar ponderea cumulată face o suma a tuturor ponderilor pentru a știi în final factorii care vor fi considerați potriviți pentru analiză.
 
 ![image](https://user-images.githubusercontent.com/76962878/190700021-6ba37b73-415e-492b-83af-d28753c0e959.png)

>Figură 4: Plot de varianță

După criteriul Kaiser (prezentat cu verde în figura 4) avem doar 4 componente , cele care au variație mai mare decât 1. După criteriul Cattell avem tot 4 dar folosind un altfel de calcul: pierderea de varianta a componenței 5 față de componentă 4 este mai mare decât cea a componenței 4 față de componentă 3. Aceste două criterii sunt folosite pentru analiză componentelor principale mai mult decât pentru o analiză a factorilor, de aceea mă voi opri din căutarea numărului de factori la componentă 10 folosind testul Bartlett. 

Următorul pas este folosirea rotației care ajută la obținerea unei structuri mult mai simple și ușor interpretabile. Pentru tipul de rotație, îmi voi îndrepta atenția spre rotația „varimax” care maximizează variația totală explicată de factori printr-o suma între corelațiilor factoriale și mediile pătratelor corelațiilor factoriale pe fiecare factor. În același timp, rotația de tip varimax are grijă că factorii creați să nu fie corelați (nu există ortogonalitate). 

* ### Corelograma si analiza factorilor
 ![image](https://user-images.githubusercontent.com/76962878/190700038-d18074fd-4da9-497d-afb4-cb260e3f9988.png)

>Figură 5: Corelograma dintre variabile si factori

Figura 5 prezintă coeficienții de corelație între variabilele principale și cei 10 factori. Pentru primul factor putem observă corelația puternică a acestuia cu orice ține de ratingul oferit hotelului. 

Criteriile de evaluare se încadrează în două categorii: subiective și obiective. Criteriile subiective sunt valoarea, calitatea somnului și serviciile iar cele obiective, care sunt predominante, sunt locația și camera. Curățenia este văzută că un criteriu subiectiv și obiectiv. 

Acest prim factor arată cauzele ce țîn de satisfacția clienților din hotele, de aceea îl putem categoriza că fiind nivelul de confort a clienților.

Pentru al doilea factor observăm că cea mai mare valoarea regăsită este la PIB și variabilă de individualitate a țării. Dacă pentru primul factor accentul este pe hotel, al doilea prezintă țară și economia să că fiind un factor definitoriu pentru satisfacția turiștilor. Aici vorbim de țări bogate care prezintă un procent ridicat al turismului. Totodată, prezența individualității arată o inclinație a turiștilor spre țări care nu sunt atât de primitoare, poate această inclinație denotă proveniența dintr-o astfel de țară a turiștilor ori o călătorie doar în scop de business și nu de turism. Factorul este invers corelat cu distanță puterii ceea ce arată că, în comparație cu nivelul unui individualism crescut al țării vizitate și PIB-ul ridicat, țară poate prezența o distribuție a puterii inegală. Deci, în concluzie, o țară bogată și rece poate avea un sistem economic bazat pe capitalism.

Factorul 3 este concentrat pe stelele hotelului și prețul. Atunci când descompunem ratingurile oferite hotelelor, aflăm că diferența între nivelele raportate de satisfacție a clienților este datorată de atributele hotelelor. Astfel, turiștii sunt dispuși să aleagă hotele care sunt mai populare și au o reputație bună în rândul clienților. Turiștii vor verifică site-uri precum TripAdvisor pentru alegerea unui loc în care să își petreacă vacanță, și totodată să le ofere o satisfacție ridicată. 

În factorul 4 putem observă dorința unei vacanțe în țări care sunt orientate spre viitor și care prioritizează progresul. Corelația inversă cu indulgență unei țări duce la o întrebare: de ce ar fi inclinați turiștii spre țări care suprimă nevoia de distracție a oamenilor? Răspunsul la această întrebarea vine din comparația acestei variabile cu cea normal corelată. Progresul unei țări poate duce de cele mai multe ori la un nivel scăzut al dorinței de satisfacere a nevoilor umane ce țîn de distracția și nevoia oamenilor de a se bucură de viață.   

Factorul 5 prezintă o corelație mare cu ratingul oferit pentru servicii. Uneori, serviciile oferite de hotele pot depășii așteptările clientului înainte de a plătii cazarea. Atât aspectele legate de așteptări cât și cele legate de performanță ale hotelului influențează satisfacția generală a clientului. Printre serviciile oferite de industria hotelieră se enumeră calitatea formării profesionale a personalului și amabilitatea, nivelul local de dezvoltare a ospitalității, mâncarea și băuturile oferite.

Următorii doi factori analizează locația hotelului. O caracteristică importantă care determina un nivel ridicat al satisfacției este comoditatea oferită de serviciile hoteliere. Pentru un turist, este mult mai convenabil că locația aleasă să fie cât mai aproape de atracțiile oferite de fiecare oraș în parte, decât să piardă mult timp doar cu transportul dintr-o parte în altă. Variabilă „hotel distance” arată cât de departe este hotelul de centrul orașului. În concluzie, locația hotelului este o parte integrantă a calității generale a serviciilor ospitaliere și afectează direct ratingul general. Clienții care sunt mulțumiți de servicii au tendința să ofere ratinguri ridicate locației.

Factorul 8, precum F3, prezintă atributele hotelului că fiind o cauza determinantă a satisfacerii generale a turiștilor. Astfel, se pare că mărimea hotelului reprezentată prin numărul de camere este un factor de decizie pentru clienți. 

În continuare, putem observă o preferința pentru țările cu un nivel ridicat de masculinitate. Această tendința se atribuie țărilor care au o istorie bogată precum Japonia ori țări europene influențate de cultură germană (Wikipedia). 

În final, ultimul factor prezintă o corelație inversă cu indexul UAI care arată predispunerea turiștilor pentru țările care nu „evita incertitudinea”. Astfel, în contextul actual este important pentru călători să aleagă țări care acceptă noul și diferitul, societatea tinde să impună mai puține reglementări, iar mediul permite liberă exprimare. 

Cei 10 factori analizați, variabilele conținute și categoria din care fac parte sunt prezentate mai jos:
1.	Confort: overall_rating, cleanliness_rating, rooms_rating, sleepquality_rating, value_rating
2.	Bogăția unei țări: GDP, IDV, PDI (invers)
3.	Hotel: hotel_stars, price
4.	Progres: Indexul LTO, IVR (invers)
5.	Servicii: service_rating
6.	Destinație: location_rating
7.	Comoditate: hotel_distance
8.	Mărimea hotelului: hotel_norooms
9.	Istorie și atracții: MAS
10.	Libera exprimare: UAI (invers)

* ### Scoruri factoriale
![image](https://user-images.githubusercontent.com/76962878/190700065-c010678b-c03f-493c-b2b4-0432421a1cfe.png)

>Figură 6: Plot scoruri factoriale

În figura 6, putem vedea conexiunea dintre fiecare factori și variabilele inițiale. După cum putem observă, nivelul de confort al unui hotel (F1) și bogăția țării în care se află hotelul (F2) se poate regăși în țări dezvoltate precum Japonia, Nouă Zeelandă și Australia și în multe țări din Europa. Astfel, colțul din dreapta sus prezintă acele țări care au ratinguri ridicate și prezintă o mare individualitate si un PIB ridicat. 

Dacă ar fi să împărțim plotul în două parți, în partea de sus observăm o împrăștiere a țărilor dezvoltate iar în cea de jos se află țările cu un PIB mai scăzut în comparație cu cele de mai sus. Totodată, țările din partea dreapta a plotului sunt acele țări care prezintă ratinguri ridicate a hotelurilor analizate, iar în partea stânga regăsim acele hoteluri în care regăsim ratinguri scăzute ale serviciilor ospitaliere. 

* ### Corelații
![image](https://user-images.githubusercontent.com/76962878/190700082-31c82ed5-0daf-4787-88b2-ef2e2915a7e9.png)  | ![image](https://user-images.githubusercontent.com/76962878/190700096-6e1f8f56-38d6-4432-8c36-404f08011a42.png)
------------- | -------------
Figură 8: Cercul corelațiilor pentru F1 si F2  | Figură 7: Cercul corelațiilor pentru F3 si F4

Pentru cercul corelațiilor dintre factori, putem observă că atunci când alegem să facem o interpretare între primii doi factori, orice alți factori prezintă o inclinație a valorilor spre centrul cercului deoarece nivelul de semnificație scade. De aceea, am ales să fac o interpretare a factorilor 1 și 2, pentru o mai ușoară prezentare a datelor. Cele două cercuri sunt caracteristice testului Bartlett (cu albastru închis în figura 8) și a testului Cattell (cu albastru deschis). 

Distribuția observățiilor în spațiul celor doi primi factori arată o mai mare aglomerație pe linia F2 pentru majoritatea variabilelor cu excepția individualități, a PIB și PDI care sunt amplasate la extremitățile cercului corelațiilor, pe linia F1.  Comparând acest cerc cu corelograma putem conclude că această aglomerație a valorilor pe linia F2 este rezultatul unor valori foarte apropiate de 0. Datorită unor diferențe destul de mari între cei doi factori, avem această dispersie a valorilor.

Totodată, majoritatea variabilelor se află în cadranul 1 și 4 a cercului, ceea ce denotă o corelație pozitivă cu primul factor analizat. Deci, valorile aflate în cadranul 1 prezintă o corelație pozitivă cu ambii factori analizați, iar cele aflate în cadranul 4 prezintă o corelație pozitivă cu primul factor și o corelație negativă cu cel de al doilea. 

## Concluzii

În concluzie, creșterea numărului recenziilor și a rezervărilor online - călătorii (în special cei care scriu recenzii pe TripAdvisor.com și alte servicii online) sunt din ce în ce mai înclinați să aleagă hotelurile pe baza reputației lor online, ceea ce crește șansele că hotelurile de înaltă calitate să fie selectate.  Abundența din ce în ce mai mare a recenziilor online și a informațiilor legate despre țările vizitate a dus la decizii mai bine informate legate de selectarea hotelurilor și, în cele din urmă, la o mai bună satisfacție generală a clienților. 

## Bibliografie
https://en.wikipedia.org/wiki/Hofstede%27s_cultural_dimensions_theory
https://www.hofstede-insights.com/models/national-culture/
https://towardsdatascience.com/factor-analysis-a-complete-tutorial-1b7621890e42
https://www.datacamp.com/community/tutorials/introduction-factor-analysis
https://en.wikipedia.org/wiki/Exploratory_factor_analysis
https://www.analyticsvidhya.com/blog/2020/10/dimensionality-reduction-using-factor-analysis-in-python/


