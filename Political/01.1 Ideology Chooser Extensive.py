import random
NumbSets= int(input("How many sets do you want? "))
ocracy_dict = {
    "Democracy": ["Demarchy", "Census democracy", "Direct democracy", "Electocracy", "Herrenvolk democracy", "Liberal democracy", "Liquid democracy", "Representative democracy", "Social democracy", "Soviet democracy", "Totalitarian democracy", "Electoral autocracy", "Digital democracy"],
    "Oligarchy": ["Aristocracy", "Ergatocracy", "Geniocracy", "Hamarchy", "Kraterocracy", "Kritarchy", "Meritocracy", "Netocracy", "Noocracy", "Plutocracy", "Particracy", "Stratocracy", "Synarchism", "Technocracy", "Theocracy", "Timocracy"],
    "Autocracy": ["Civilian dictatorship", "Military dictatorship"]
}

power_dict = {
    "Monarchy": ["Absolute monarchy", "Constitutional monarchy", "Crowned republic", "Elective monarchy"],
    "Republic": ["Classical republic", "Constitutional republic", "Democratic republic", "Federal republic", "Religious republic", "Parliamentary republic", "Presidential republic", "People's republic", "Semi-presidential republic", "Directorial republic", "Merchant republic"]
}

Ideologies = ["Abahlali baseMjondolo","Absolute monarchism","Absolute monarchy","Absolutism","Absolutist corporatism","Abstentionism","African socialism","Agonistic liberalism","Agorism","Agrarian reformism","Agrarian socialism","Agrarianism","Alt-lite movement","Alt-right movement","Alter-globalization movement","Analytical feminism","Analytical Marxism","Anarcha-feminism","Anarchism","Anarchism without adjectives","Anarcho-capitalism","Anarcho-communism","Anarcho-naturism","Anarcho-pacifism","Anarcho-primitivism","Anarcho-punk","Anarcho-Socialism","Anarcho-syndicalism","Anarcho-transhumanism","Animal rights movement","Anti anti-communism","Anti-abortion movement","Anti-aging movement","Anti-austerity movement","Anti-Centrism","Anti-clericalism","Anti-consumerism","Anti-corporate activism","Anti-corporate movement","Anti-feminism","Anti-globalization movement","Anti-immigration movement","Anti-immigrationism","Anti-imperialism","Anti-intellectualism","Anti-LGBT movement","Anti-Masonry","Anti-militarism","Anti-nuclear movement","Anti-politics","Anti-revisionary Marxism","Anti-revisionism","Anti-unionism","Anti-war movement","Antidisestablishmentarianism","Antisemitism","Apoliticism","Arab socialism","Archeio-Marxism","Aristocracy","Aryanism","Associative democracy","Austro-libertarianism","Austro-Marxism","Autarchism","Authoritarian capitalism","Authoritarian conservatism","Authoritarian democracy","Authoritarian populism","Authoritarian socialism","Autocracy","Autonomism","Ba'athism","Back-to-the-land movement","Barracks communism","Barracks socialism","Benevolent dictatorship","Bernsteinism","Bioconservatism","Bioregional democracy","Bioregionalism","Black anarchism","Black conservatism","Blanquism","Bordigism","Bourgeois democracy","Bourgeois nationalism","Brazilian Integralism","Brezhnevism","Bruderhofs","Budapest School","Buddhist anarchism","Business nationalism","Byzantinism","Caesaropapism","Californian Ideology","Car-free movement","Care-focused feminism","Castroism","Catholic Worker Movement","Caudillismo","Ceaușism","Cellular democracy","Centrist Marxism","Chartists","Chaulieu–Montal tendency","Chauvinism","Chicagoanism","Christian anarchism","Christian anti-Masonry","Christian communism","Christian democracy","Christian right","Christian socialism","Christofiasism","Civic conservatism","Civic nationalism","Civil libertarianism","Class collaborationism","Classical conservatism","Classical fascism","Classical liberal radicalism","Classical liberalism","Classical Marxism","Classical republicanism","Clericalism","Climate movement","Co-operatism","Collaborative e-democracy","Collectivist anarchism","Colonialism","Communalism","Communard movement","Communards","Communist egoism","Communist state","Communitarian corporatism","Communitarianism","Communization","Compassionate conservatism","Complementarianism","Confessionalism","Conflict theories","Consequentialist libertarianism","Conservation movement","Conservative corporatism","Conservative democracy","Conservative feminism","Conservative left","Conservative liberalism","Conservative libertarianism","Conservative populism","Conservative socialism","Conservative welfarism","Consociationalism","Constitutional democracy","Constitutional dictatorship","Constitutional liberalism","Constitutional monarchism","Constitutionalism","Cooperativism","Copyleft","Copyright reform movement","Corporate capitalism","Corporate nationalism","Corporate statism","Corporate welfarism","Corporatocracy","Cosmopolitan democracy","Cosmopolitanism","Council communism","Council democracy","Counter-economics","Counterintelligence state","Crowned republic","Crypto-anarchism","Crypto-fascism","Cult of Reason","Cult of the Supreme Being","Cultural conservatism","Cultural feminism","Cultural globalizationism","Cultural liberalism","Cultural nationalism","Cyber-utopianism","Cyberfeminism","De Leonism","De-Stalinization","Deep Green Resistance","Defensive democracy","Degrowth movement","Demagogy","Demarchism","Democratic capitalism","Democratic centralism","Democratic confederalism","Democratic globalization","Democratic liberalism","Democratic mundialization","Democratic republicanism","Democratic socialism","Democratic transhumanism","Deng Xiaoping Theory","Dependency theory","Despotism","Developmentalism","Diaspora nationalism","Dictablanda","Dictatorship","Difference feminism","Diggers","Digital authoritarianism","Đilasism","Direct democracy","Disestablishmentarianism","Distributism","Dominionism","Dubčekism","E-democracy","E-government","E-participation","Earth liberation movement","Eco-capitalism","Eco-communalism","Eco-communism","Eco-fascism","Eco-feminism","Eco-modernism","Eco-nationalism","Eco-socialism","Ecoauthoritarianism","Ecocentrism","Ecofeminism","Ecological modernization","Economic antisemitism","Economic corporatism","Economic democracy","Economic egalitarianism","Economic globalizationism","Economic liberalism","Economic nationalism","Economic populism","Economic progressivism","Egalitarianism","Egoist anarchism","Egoist communism","Electoral democracy","Enlightened absolutism","Equality feminism","Equity feminism","Esoteric fascism","Ethical socialism","Ethnic democracy","Ethnic nationalism","Ethnocracy","Eurasianism","Eurocommunism","Euroscepticism","Expansionist nationalism","Expropriative anarchism","Extropianism","Fabianism","Falangism","Far-right ultranationalism authoritarianism","Fascism","Fascist corporatism","Fascist mysticism","Fascist syndicalism","Feminist theology","Feudal fascism","Fiscal conservatism","Fiscal environmentalism","Fitzhughism","Focalism","Fourierism","Frankfurt School","Free-market anarchism","Free-market anti-capitalism","Free-market environmentalism","Free-market fundamentalism","Free-market socialism","Free-marketism","Freemasonry","Freiwirtschaft","Freudo-Marxism","Freudo–Marxism","Fully automated luxury communism","Fusionism","Gender feminism","Geolibertarianism","Georgism","Glasnost","Global citizens movement","Global justice movement","Globalism","Gonzalo Thought","Gorbachevism","Gradualism","Gramscianism","Green anarchism","Green conservatism","Green left","Green liberalism","Green libertarianism","Green municipalism","Green Zionism","Guevarism","Guided democracy","Guild socialism","Guildism","Harambee","Hard Euroscepticism","Hegelian Marxism","Herrenvolk democracy","Hindu anarchism","Ho Chi Minh Thought","Homonationalism","Hoxhaism","Humanism","Husakism","Hutterites","Icarians","Illegalism","Illiberal democracy","Illiberalism","Immediatism","Immortalism","Imperialism","Impossibilism","Inclusive democracy","Individualist anarchism","Individualist feminism","Industrial democracy","Instrumental Marxism","Insurrectionary anarchism","Integral nationalism","Integralism","Interactive democracy","International communism","International socialism","Intersectional feminism","Inverted totalitarianism","Irredentism","Islamic anarchism","Islamic communism","Isolationism","Jacobins","Jewish anarchism","Jewish communism","Jingoism","Johnson–Forest tendency","Juche","Kadarism","Kautskyism","Kaysone Phomvihane Thought","Khrushchev Thaw","Khrushchevism","Kibbutz movement","Kimilsungism","Kimilsungism–Kimjongilism","Kinship corporatism","Kraterocracy","Labor feminism","Labour movement","Labourism","Laissez-faire","Laissez-faire socialism","Land reform movement","Landless Workers' Movement","Langian socialism","Lassallism","Lebensraum","Left communism","Left Shachtmanism","Left-libertarianism","Left-wing antisemitism","Left-wing laissez-faire","Left-wing nationalism","Legal egalitarianism","Leninism","Lesbian feminism","Levellers","LGBT conservatism","Liberal autocracy","Liberal centrism","Liberal communitarianism","Liberal conservatism","Liberal constitutionalism","Liberal corporatism","Liberal democracy","Liberal egalitarianism","Liberal feminism","Liberal internationalism","Liberal moderatism","Liberal nationalism","Liberal populism","Liberal progressivism","Liberal radicalism","Liberal republicanism","Liberal socialism","Liberal syncretism","Liberal transhumanism","Liberal welfarism","Liberation nationalism","Libertarian communism","Libertarian conservatism","Libertarian feminism","Libertarian Marxism","Libertarian municipalism","Libertarian paternalism","Libertarian possibilism","Libertarian Republicanism","Libertarian socialism","Libertarian transhumanism","Libertarianism","Lipstick feminism","Liquid democracy","Localism","Lusitanian integralism","Luxemburgism","Mafia state","Majoritarianism","Makhaevism","Makhnovism","Managerial state","Managerialism","Manifest destiny","Mao Zedong Thought","Mao-Spontex","Maoism","Maoism–Third Worldism","Market democracy","Market populism","Market socialism","Market-oriented left-libertarianism","Marxism","Marxism–De Leonism","Marxism–Leninism","Marxism–Leninism–Maoism","Marxism–Leninism–Maoism–Prachanda Path","Marxist democracy","Marxist feminism","Marxist humanism","Marxist revisionism","Marxist–Leninist atheism","Marxist–Leninist democracy","Material feminism","Maternal feminism","Maurassisme","Media democracy","Messianism","Metaxism","Military dictatorship","Millennial socialism","Millian socialism","Minarchism","Minoritarianism","Modern egalitarianism","Modern republicanism","Monarchism","Multiparty democracy","Municipal socialism","Muscular liberalism","Muslim anti-Masonry","Mutualism","Mutualist movement","Nashism","Nasserism","National Bolshevism","National capitalism","National communism","National conservatism","National corporatism","National Democracy","National liberalism","National mysticism","National populism","National socialism","National syndicalism","National-anarchism","Nativism","Natural-rights libertarianism","Naxalism","Nazi-Maoism","Nazism","Nechayevism","Nechayevshchina","Neo-colonialism","Neo-corporatism","Neo-fascism","Neo-feminism","Neo-feudalism","Neo-Gramscianism","Neo-imperialism","Neo-Legionarism","Neo-liberalism","Neo-Luddism","Neo-Marxism","Neo-mutualism","Neo-nationalism","Neo-Nazism","Neo-reactionary movement","Neo-republicanism","Neo-Sovietism","Neo-Stalinism","Neoclassical liberalism","Neoconservatism","Net neutrality movement","Neue Marx-Lektüre","New antisemitism","New Democracy","New Synthesis","Nkrumaism","Non-partisan democracy","Nordic model","Nouvelle Droite","Occupy movement","Ochlocracy","Oligarchy","One-party state","Open Marxism","Open-source-software movement","Ordoliberalism","Orthodox Jewish anarchism","Orthodox Marxism","Orthodox Trotskyism","Owenism","Pabloism","Pacifism","Paleoconservatism","Paleolibertarianism","Palingenetic ultranationalism","Pan-nationalism","Panarchism","Para-fascism","Parecon","Parliamentary democracy","Parpolity","Participatory budgeting","Participatory democracy","Participatory justice","Participatory planning","Paternalistic conservatism","Patriarchalism","Patriotism","Peace movement","Penal populism","People's democracy","People's dictatorship democracy","People's Multiparty Democracy","Perestroika","Philosophical anarchism","Physiocracy","Piqueteros","Platformism","Pluralist democracy","Plutocracy","Pol Potism","Police state","Political egalitarianism","Political globalizationism","Political Marxism","Political religion","Populism","Posadism","Positive environmentalism","Possibilism","Post-anarchism","Post-colonial anarchism","Post-colonial nationalism","Post-communism","Post-consumerism","Post-fascism","Post-genderism","Post-growth","Post-left anarchism","Post-Marxism","Post-modern feminism","Post-politicism","Postcolonial theology","Praxis School","Pre-Marxist communism","Presidential democracy","Primitive communism","Pro-feminism","Procedural democracy","Producerism","Progressive conservatism","Progressive corporatism","Progressivism","Proletarian democracy","Prometheanism","Propertarianism","Protectionism","Proto-fascism","Proto-socialism","Proudhonian socialism","Pythagoreanism","Queer anarchism","Queer communism","Queer ecology","Queer nationalism","Queer socialism","Race supremacy","Racial antisemitism","Racial democracy","Racial nationalism","Radical centrism","Radical democracy","Radical environmentalism","Radical feminism","Radical nationalism","Radical right-wing populism","Radicalism","Radicals","Rankovićism","Reactionary modernism","Reactionary populism","Real socialism","Really Really Free Market movement","Reform movement","Reformism","Reformist socialism","Regionalism","Religious anarchism","Religious anti-Zionism","Religious antisemitism","Religious apoliticism","Religious communism","Religious egalitarianism","Religious environmentalism","Religious humanism","Religious liberalism","Religious nationalism","Religious pacifism","Religious socialism","Representative democracy","Republican democracy","Revanchism","Revolutionary democracy","Revolutionary nationalism","Revolutionary socialism","Revolutionary syndicalism","Rewilding","Ricardian socialism","Right-wing laissez-faire","Right-wing nationalism","Right-wing populism","Romantic nationalism","Saint-Simonianism","Scientific communism","Scientific Outlook on Development","Scientific socialism","Sectarian democracy","Secular humanism","Secular liberalism","Secular religion","Secular state","Secularism","Segregationism","Semi-democracy","Semi-direct democracy","Senghorism","Separatist feminism","Sex-positive feminism","Shachtmanism","Shakers","Singularitarianism","Sinistrisme","Situationism","Smithian socialism","Social anarchism","Social conflict theory","Social conservatism","Social corporatism","Social Darwinism","Social democracy","Social democratic corporatism","Social democratic populism","Social democratic Shachtmanism","Social democratic transhumanism","Social democratic welfarism","Social ecology","Social egalitarianism","Social feminism","Social justice movement","Social liberalism","Social libertarianism","Social populism","Social progressivism","Socialism in one country","Socialism of the 21st century","Socialism with Chinese characteristics","Socialisme ou Barbarie","Socialist democracy","Socialist feminism","Socialist nationalism","Socialist patriotism","Socialist populism","Socialist Yugoslav nationalism","Socialist Yugoslavism","Soft authoritarianism","Soft despotism","Soft Euroscepticism","Solidar corporatism","Solidarity","Songun","Sorelianism","Sortitionism","Souverainism","Sovereign democracy","Sovereignism","Soviet anti-Zionism","Soviet antisemitism","Soviet democracy","Soviet nationalism","Soviet nostalgia","Soviet socialist patriotism","Spartacism","Specifism","Spiritual ecology","Spiritual left","Spontaneism","Spoonerian socialism","Stalinism","Standpoint feminism","State capitalism","State corporatism","State feminism","State religion","Steady-state economy","Steiner–Vallentyne school","Stratocracy","Structural Marxism","Substantive democracy","Supremacism","Sustainable capitalism","Syncretism","Syndicalism","Synthesis anarchism","Techno-fascism","Techno-populism","Techno-progressivism","Techno-utopianism","Technocracy movement","Technogaianism","Technoliberalism","Technolibertarianism","Territorial nationalism","Thealogy","Theoconservatism","Theocracy","Theonomy","Theophilanthropy","Third camp","Third camp socialism","Third camp Trotskyism","Third International Theory","Third Position","Third Positionism","Third Way","Third World socialism","Third Worldism","Three Principles of the People","Three Represents","Timocracy","Titoism","Tkachevism","Tolstoyan movement","Tory democracy","Totalitarian democracy","Totalitarianism","Traditionalist conservatism","Trans-exclusionary radical feminism","Transfeminism","Transnational progressivism","Transnational repression","Trasformismo","Tripartism","Trotskyism","Tuckerite socialism","Ubuntuism","Ujamaa","Ultra-leftism","Ultramontanism","Ultranationalism","Unorthodox Trotskyism","Utopian socialism","Vanguardism","Veblenian socialism","Veganarchism","Vegetarian eco-feminism","Völkisch movement","Voluntaryism","Vperedism","War communism","War socialism","Welfare chauvinism","Western conservatism","Western Marxism","Westminster democracy","Whiggism","Wobblyism","Womanist theology","Women's liberation movement","Workerism","Workers' self-management","Workplace democracy","World communism","World socialism","World Socialist Movement","World-systems theory","Xi Jinping Thought","Yugo-nostalgia","Zapatistas"]

for i in range(NumbSets):
    random_ocracy = random.choice(list(ocracy_dict.keys()))
    ocracy_picked = random.choice(ocracy_dict[random_ocracy])
        
    power_choose = random.choice(list(power_dict.keys()))
    power_picked = random.choice(power_dict[power_choose])
    print("")
    print(f"Values for Party {i+1}:")
    print(f"Type of ocract: {ocracy_picked}")
    print(f"Type of power: {power_picked}")
    for o in range(10):
        SocioPicked = random.choice(Ideologies)
        print(f"Ideology {o+1}: {SocioPicked}")

    