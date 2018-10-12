def inlezen_beginstation(stations):
    while True:
        beginstation = input('Wat is uw beginstation?')
        if beginstation in stations:
            return beginstation
        else:
            print('De trein komt niet in', beginstation)

def inlezen_eindstation(stations,beginstation):
    while True:
        eindstation = input('Wat is uw eindstation?')
        if eindstation in stations:
            if stations.index(eindstation) > stations.index(beginstation):
                return eindstation
            else:
                print('De trein gaat niet achteruit')
        else:
            print('De trein komt niet in', eindstation)


def omroepen_reis(stations,beginstation,eindstation):
    print('Het beginstation', beginstation, 'is het', str(stations.index(beginstation) + 1) + 'e station in het traject')
    print('Het eindstation', eindstation, 'is het', str(stations.index(eindstation) + 1) + 'e station in het traject')
    print('De afstand bedraagt', stations.index(eindstation) - stations.index(beginstation), 'station(s)')
    print('De prijs van het kaartje is', (stations.index(eindstation) - stations.index(beginstation)) * 5, 'euro')
    print('\n')
    if stations.index(eindstation) - stations.index(beginstation) == 0:
        print('Je stapt in op:', beginstation)
        print('-')
        print('Je stapt uit op:', eindstation)
    else:
        print('Je stapt in op:', beginstation)
        for i in stations:
            if stations.index(i) > stations.index(beginstation) and stations.index(i) < stations.index(eindstation):
                print('Tussenstop: ', i)
        print('Je stapt uit op: ', eindstation)
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum','Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch','Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations,beginstation)
omroepen_reis(stations,beginstation,eindstation)
