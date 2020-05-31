/*facts - flight(1st airport, company,2nd airport, price, distance)*/

flight(toronto, aircanada, london, 500, 360).
flight(toronto, united, london, 650, 420 ).
flight(toronto, united, madrid,1000,600).
flight(toronto, ibeira, madrid, 850, 540).
flight(toronto, aircanada, madrid, 950, 540).

flight(madrid, ibeira, toronto, 875, 525).
flight(madrid, united, toronto, 1025, 585).
flight(madrid, aircanada, toronto, 975, 525).
flight(madrid, aircanada, barcelona, 175, 105).
flight(madrid, ibeira, barcelona, 205, 110).
flight(madrid, ibeira, valencia, 115, 95).
flight(madrid, ibeira, malaga, 125, 105).

flight(barcelona,ibeira,london,260,270).
flight(barcelona,ibeira, valencia,150,105).
flight(barcelona,ibeira, madrid,160,95).
flight(barcelona,aircanada,madrid,140,90).

flight(london,aircanada,toronto,575,440).
flight(london,united,toronto,725,500).
flight(london,ibeira,barcelona,295,320).

flight(malaga, ibeira, valencia, 130, 150).
flight(malaga, ibeira, madrid, 100, 90).

flight(valencia, ibeira, barcelona, 150, 95).
flight(valencia, ibeira, madrid, 80, 70).
flight(valencia, ibeira, malaga, 120, 140).

flight(paris, united, toulouse, 85,  180).

flight(toulouse, united, paris, 75, 150).

/*Airports - airport(city, airport tax, min security delay)*/
airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).
airport(london, 75, 80).

/*Rules*/
is_there_flight(X, Y) :- flight(X, _, Y, _, _).
cheap_flight(X, A, Y) :- flight(X, A, Y, P, _), P<400 .
is_two_flight_possible(X, Y) :- flight(X, _, Z, _, _), flight(Z, _, Y, _, _), Z \== X, Z \== Y.
is_aircanada_cheap_flight(X, Y) :- flight(X, A, Y, _, _), A == aircanada.
is_flight_from_aircanada(X, Y) :- flight(X, A, Y, _, _), A == united -> flight(X, B, Y, _, _), B == aircanada.







