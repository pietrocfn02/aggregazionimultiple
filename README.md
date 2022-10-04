# aggregazioni multiple


# Setup e preparazione

Per far partire il progetto è necessario installare django
è disponibile il file requirements.txt contenente le librerie richieste per il progetto.
Si consiglia di installare tutte le librerie tramite un ambiente virtuale python

# Avvio

Una volta installate le dipendenze, spostarsi nella tabella "aggregazioni_multiple" (quella contenente al suo interno il file manage.py)
e lanciare i seguenti comandi per costruire e popolare la base di dati: 

python manage.py makemigrations

python manage.py migrate 

python manage.py loaddata data.json 



Una volta eseguita questa operazione, può essere avviato il server tramite il comando

python manage.py runserver


Il server sarà attivo all'indirizzo 

http://localhost:8000
