# generic-service
Met de generic-service kan je eenhoudig, aan de hand van de omgevingen structuur en edwh plugin, een service opbouwen en deze vervolgens deployen op bijv. de utils server. Door deze manier van werken wordt het, ontwikkelen en implementeren van nieuwe services, gedaan op dezelfde werkwijze als onze omgevingen. 

## captain hooks (verplicht)
Hierin staan de commands verwerkt die voor ons een backup of restore mogelijk maken. Deze commands zijn dan ook (veelal) eenvoudig te kopieren en te plakken in de code. 

## setup-init.sh (optioneel)
Mocht er bij een service een startup script benodigd zijn, vergeet deze dan niet mee te nemen, ter voorbeeld is hier een startupscript genomen van een willkeurige service. Denk bij het vervangen van dit bestand wel aan naamgeving en format, ook heeft niet elke service een seup script nodig. Bekijk daarom geod de documentatie van de service die je wilt opzetten.

## backup (optioneel)
Mocht je een backup willen kan je een (interne) backup maken die je kan mappen naar deze map. Hierbij ligt het heel erg aan de configuratie van de service en hoe deze de backup heeft geregeld. 

## docker-compose.yml (verplicht)
Vul hier de compose aan met configuratie vanuit de compose van de service. Let hierbij wel op of de service gebruik maakt van een proxy, bijv. nginx, en of je deze dan nog moet ombouwen o.i.d.

## tasks.py (verplicht)
Hierin zit alle config die in de .env moet komen te staan, dit kan dan weer gebruikt worden in de docker-compose, shell scripts en ew tools.

## .env (verplicht)
Deze wordt (deels) opgezet bij (edwh) setup maar vergeet niet hierin specifieke variabelen toe te voegen die aangeroepen worden vanuit de docker-compose. 

## config.toml (veprlicht)
Hoeft beheerder niet zelf aan te maken, daarom wordt deze ook niet meegenomen in deze repository. Door (edwh) setup te doen wordt deze automatisch aangemaakt. 

 
