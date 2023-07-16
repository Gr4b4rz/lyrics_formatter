# Lyrics formatter

Lyrics formatter.
This program uses input lyrics files to create files that can be imported to OrionGT controller.

<table>
<tr>
<th> Before </th>
<th> After </th>
</tr>
<tr>
<td valign='top'>

```
Ref. Skosztujcie i zobaczcie jak dobry jest Pan,
skosztujcie i zobaczcie jak dobry jest Pan.

1. Będę błogosławił Pana po wieczne czasy,
Jego chwała będzie zawsze na moich ustach.
Dusza moja chlubi się Panem,
niech słyszą to pokorni i niech się weselą.

Ref. Skosztujcie i zobaczcie jak dobry jest Pan,
skosztujcie i zobaczcie jak dobry jest Pan.

2. Uwielbiajcie razem ze mną Pana,
wspólnie wywyższajmy Jego Imię,
szukałem pomocy u Pana, a On mnie wysłuchał
i uwolnił od wszelkiej trwogi.

Ref. Skosztujcie i zobaczcie jak dobry jest Pan,
skosztujcie i zobaczcie jak dobry jest Pan.

3. Spójrzcie na Niego, a rozpromienicie się radością,
oblicza Wasze nie zapłoną wstydem.
Oto biedak zawołał i Pan go wysłuchał
i wybawił ze wszystkich ucisków.

Ref. Skosztujcie i zobaczcie jak dobry jest Pan,
skosztujcie i zobaczcie jak dobry jest Pan.

4. Anioł Pana otacza szańcem bogobojnych,
aby ocalić tych, którzy w Niego wierzą,
skosztujcie i zobaczcie, jak Pan jest dobry,
szczęśliwy człowiek, który się do Niego ucieka.

Ref. Skosztujcie i zobaczcie jak dobry jest Pan,
skosztujcie i zobaczcie jak dobry jest Pan.

5. Bójcie się Pana wszyscy Jego święci,
gdyż bogobojni nie zaznają biedy,
bogacze zubożeli i zaznali głodu,
szukającym Pana niczego nie zabraknie.

Ref. Skosztujcie i zobaczcie jak dobry jest Pan,
skosztujcie i zobaczcie jak dobry jest Pan.

6. Pan słyszy wołających o pomoc
i ratuje ich od wszelkiej udręki
Pan jest blisko ludzi skruszonych w sercu
i wybawia złamanych na duchu.

Ref. Skosztujcie i zobaczcie jak dobry jest Pan,
skosztujcie i zobaczcie jak dobry jest Pan.

7. Wiele nieszczęść spada na sprawiedliwego
lecz ze wszystkich Pan go wybawia
On czuwa nad każdą jego kością
ani jedna z nich nie zostanie złamana.

Ref. Skosztujcie i zobaczcie jak dobry jest Pan,
skosztujcie i zobaczcie jak dobry jest Pan.
```

</td>
<td valign='top'>

```
Skosztujcie i zobaczcie
Ref. Skosztujcie i
zobaczcie jak dobry jest
Pan, skosztujcie i
zobaczcie jak dobry jest
Pan.



1. Będę błogosławił Pana
po wieczne czasy, Jego
chwała będzie zawsze na
moich ustach. Dusza moja
chlubi się Panem, niech
słyszą to pokorni i
niech się weselą.

Ref. Skosztujcie i
zobaczcie jak dobry jest
Pan, skosztujcie i
zobaczcie jak dobry jest
Pan.



2. Uwielbiajcie razem ze
mną Pana, wspólnie
wywyższajmy Jego Imię,
szukałem pomocy u Pana,
a On mnie wysłuchał i
uwolnił od wszelkiej
trwogi.

Ref. Skosztujcie i
zobaczcie jak dobry jest
Pan, skosztujcie i
zobaczcie jak dobry jest
Pan.



3. Spójrzcie na Niego, a
rozpromienicie się
radością, oblicza Wasze
nie zapłoną wstydem. Oto
biedak zawołał i Pan go
wysłuchał i wybawił ze
wszystkich ucisków.

Ref. Skosztujcie i
zobaczcie jak dobry jest
Pan, skosztujcie i
zobaczcie jak dobry jest
Pan.



4. Anioł Pana otacza
szańcem bogobojnych, aby
ocalić tych, którzy w
Niego wierzą, skosztuj-
cie i zobaczcie, jak Pan
jest dobry, szczęśliwy
człowiek, który się do
Niego ucieka.
Ref. Skosztujcie i
zobaczcie jak dobry jest
Pan, skosztujcie i
zobaczcie jak dobry jest
Pan.



5. Bójcie się Pana
wszyscy Jego święci,
gdyż bogobojni nie
zaznają biedy, bogacze
zubożeli i zaznali
głodu, szukającym Pana
niczego nie zabraknie.

Ref. Skosztujcie i
zobaczcie jak dobry jest
Pan, skosztujcie i
zobaczcie jak dobry jest
Pan.



6. Pan słyszy wołających
o pomoc i ratuje ich od
wszelkiej udręki Pan
jest blisko ludzi
skruszonych w sercu i
wybawia złamanych na
duchu.

Ref. Skosztujcie i
zobaczcie jak dobry jest
Pan, skosztujcie i
zobaczcie jak dobry jest
Pan.



7. Wiele nieszczęść
spada na sprawiedliwego
lecz ze wszystkich Pan
go wybawia On czuwa nad
każdą jego kością ani
jedna z nich nie
zostanie złamana.

Ref. Skosztujcie i
zobaczcie jak dobry jest
Pan, skosztujcie i
zobaczcie jak dobry jest
Pan.



```

</td>
</tr>
</table>


## Input data

It expects input song to be in format presented below. Verse means here both verse and chorus:
```
<verse>
<empty line>
<verse>
<empty line>
...
<verse>
```

## Usage
```
python3 format_lyrics.py "Skosztujcie i zobaczcie" --input_file songs/skosztujcie_i_zobaczcie.txt --output_file 05.TXT
```

Or to check if song is in data file
```
python3 format_lyrics.py "Bóg nad swym ludem" --check VISOR.DAT
```

More in `python3 format_lyrics.py --help`

## Song import
To import output lyrics file to the OrionGT controller:
- Save it in XX.txt format on your SD card.
- Put card in the OrionGT controller
- Turn on controller
- Hold turn-on button for ~2 seconds
- Choose song import
- Choose song to import, and category
