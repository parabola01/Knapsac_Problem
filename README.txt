Aleksandra Jaroszek

Kod implementuje algorytm genetyczny, który rozwiązuje popularny dyskretny problem optymalizacyjny czyli 
problem plecakowy. Nazwa zagadnienia pochodzi od maksymalizacyjnego problemu wyboru przedmiotów, 
tak aby ich sumaryczna wartość była jak największa i aby jednocześnie mieściły się w plecaku. 

Algorytm genetyczny składa się z następujących części:
1. losowo inicjalizuje populacje przez tworzenie listy chromosomów reprezentowanych jako listy bitów.
Na populacje składa się tyle chromosomów ile podamy jako argument "population_size", natomiast
pojedyńczy chromosom ma tyle bitów ile rzeczy rozważamy jako możliwe do umieszczenia w plecaku.

2.funkcji oceny, która określa wartość i wagę plecaka dla każdego chromosomu. Iteruje ona przez elementy listy "items"
i jeżeli dana wartość chromosomu jest równa 1 to dodaje wartość i wagę elementu do danych sum. W przypadku
gdy waga jest większa niż maksymalna waga to wartość jest ustawiana na 0, jest to rozwiązanie błędne.
Funkcja zwraca wartość i wagę jako tuple.

3.dwóch funkcji odpowiadających za krzyżowanie: jednopunktowe i dwupunktowe. Pobiera ona jako agrumenty dwoje rodziców
a następnie losuje odpowiednio jeden lub dwa punkty a następnie tworzy dziecko łącząc części rodziców powstałe
po podzieleniu ich przez wylosowane punkty.

4.funkcji mutacji, która losowo zamienia bity o ile wylosowana zostanie liczba mniejsza od zadanego
prawdopodobieństwa mutacji.

5.głównej pętli algorytmu, która zawiera odpowiednio
	-ocenę populacji za pomocą utworzenia listy ktorek w której każdemu chromosomowi w populacji przypisujemy jego
	wartość funkcji dopasowania
	-sortowanie populacji w oparciu o wartość (pierwszy element krotki) w kolejności malejącej
	-selekcję populacji czyli wybór najlepszych chromosomów z posortowanej populacji
	-losowy wybór rodziców z wyselekcjonowanej populacji
	-losowy wybór typu krzyżowania
	-mutacja dzieci powstałych w wyniku krzyżowania
	-dodanie nowo powstałych dzieci do populacji

6.algorytm zwraca najlepszy chromosom w populacji oraz wartość funkcji dopasowania, która mu odpowiada.

Testy należy rozpatywać następująco: każdy chromosom, który otrzymujemy jako najlepszy odpowiada przedmiotom, które
powinny być optymalnie włożone do plecaka. Jeżeli wartość bitu wynosi 1 to przedmiot powinien zostać włożony,
jeżeli zaś 0 przedmiot nie powinien znaleźć się w plecaku.
Należy mieć na uwadze, że algorytmy genetyczne nie zawsze dają najlepsze rozwiązanie. Jednak w przypadku zadanych problemów
ich złożoność oraz odpowiadnie ustawienie parametrów powodowało, że mój algorytm dawał we wszystkich przeprowadzanych
testach rozwiązanie optymalne.

