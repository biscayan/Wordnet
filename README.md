# 워드넷 (Wordnet)
워드넷을 활용하여 영어 단어 간의 관계성 파악

<br/>

## 프로젝트 기간 및 참여 인원
- 대학원 2학기 전산언어학2 수업의 선택과제로 프로젝트를 진행하였습니다.
- 프로젝트 기간 : 19.09.26 ~ 19.10.10  
- 프로젝트 인원 : 2명
- 나의 역할 : 코드작성 및 발표  
- 팀원의 역할 : 자료조사 및 ppt작성  

<br/>

## 기술 스택
- Python 3.7.3

<br/>

## 워드넷이란?
1. 워드넷의 정의  
- 워드넷은 영어의 거대한 데이터베이스입니다.  
- 워드넷은 일종의 영어 어휘집으로 활용됩니다.

<br/>

2. 워드넷의 역사
- 1985년, 언어학자이면서 심리학자인 George Armitage Miller의 주도 하에 프린스턴 대학의 인지 과학 연구소에서 워드넷에 대한 연구가 처음으로 진행되었습니다.  
- 1993년, 워드넷이 정식으로 출범하였습니다.

<br/>

3. 워드넷의 데이터베이스
- 워드넷은 전치사, 관사, 대명사와 같은 기능어들은 제외하고 명사, 동사, 형용사, 부사에 대한 정보만 제공합니다.  

- 워드넷 3.0의 데이터베이스는 아래와 같습니다.  

    |품사|단어의 개수|
    |:---:|:---:|
    |명사|117,789|
    |동사|11,529|
    |형용사|22,479|
    |부사|4,481|  

<br/>

## 워드넷의 기능
1. 사전 (Dictionary)
    <details>
    <summary>예시 보기</summary>
    <div markdown="1">

        Input a word : book

        >>>
        book.n.01 : a written work or composition that has been published (printed on pages bound together)
        ['I am reading a good book on economics']

        book.n.02 : physical objects consisting of a number of pages bound together
        ['he used a large book as a doorstop']

        record.n.05 : a compilation of the known facts regarding something or someone
        ["Al Smith used to say, `Let's look at the record'", 'his name is in all the record books']

        script.n.01 : a written version of a play or other dramatic composition; used in preparing for a performance
        []

        ledger.n.01 : a record in which commercial accounts are recorded
        ['they got a subpoena to examine our books']

        book.n.06 : a collection of playing cards satisfying the rules of a card game
        []

        book.n.07 : a collection of rules or prescribed standards on the basis of which decisions are made
        ['they run things by the book around here']

        koran.n.01 : the sacred writings of Islam revealed by God to the prophet Muhammad during his life at Mecca and Medina
        []

        bible.n.01 : the sacred writings of the Christian religions
        ['he went to carry the Word to the heathen']

        book.n.10 : a major division of a long written composition
        ['the book of Isaiah']

        book.n.11 : a number of sheets (ticket or stamps etc.) bound together on one edge
        ['he bought a book of stamps']

        book.v.01 : engage for a performance
        ['Her agent had booked her for several concerts in Tokyo']

        reserve.v.04 : arrange for and reserve (something for someone else) in advance
        ['reserve me a seat on a flight', 'The agent booked tickets to the show for the whole family', "please hold a table at Maxim's"]

        book.v.03 : record a charge in a police register
        ['The policeman booked her when she tried to solicit a man']

        book.v.04 : register in a hotel booker
        []

    </div>
    </details>

<br/>

2. 동의어 (Synonym)
    <details>
    <summary>예시 보기</summary>
    <div markdown="1">

        Input a word : good
        
        >>>
        Synonyms : {'sound', 'commodity', 'proficient', 'skillful', 'well', 'dependable', 'trade_good', 'goodness', 'undecomposed', 'thoroughly', 'ripe', 'respectable', 'good', 'honorable', 'soundly', 'expert', 'just', 'safe', 'honest', 'effective', 'full', 'unspoiled', 'near', 'upright', 'secure', 'serious', 'salutary', 'in_effect', 'beneficial', 'estimable', 'adept', 'right', 'in_force', 'practiced', 'skilful', 'dear', 'unspoilt'}
        
    </div>
    </details>

<br/>

3. 반의어 (Antonym)
    <details>
    <summary>예시 보기</summary>
    <div markdown="1">

        Input a word : good

        >>>
        Antonyms : {'badness', 'evilness', 'evil', 'ill', 'bad'}

    </div>
    </details>

<br/>

4. 상위어 (Hypernym)
    <details>
    <summary>예시 보기</summary>
    <div markdown="1">

        Input a synset : car.n.01

        >>>
        Hypernym :  motor_vehicle
        Hypernym :  automotive_vehicle

    </div>
    </details>

<br/>

5. 하위어 (Hyponym)
    <details>
    <summary>예시 보기</summary>
    <div markdown="1">

        Input a synset : vehicle.n.01

        >>>
        Hyponym :  bumper_car
        Hyponym :  Dodgem
        Hyponym :  craft
        Hyponym :  military_vehicle
        Hyponym :  rocket
        Hyponym :  projectile
        Hyponym :  skibob
        Hyponym :  sled
        Hyponym :  sledge
        Hyponym :  sleigh
        Hyponym :  steamroller
        Hyponym :  road_roller
        Hyponym :  wheeled_vehicle

    </div>
    </details>

<br/>

6. 부분어 (Meronym)
    <details>
    <summary>예시 보기</summary>
    <div markdown="1">

        Input a synset : face.n.01

        >>>
        Meronym :  beard
        Meronym :  face_fungus
        Meronym :  whiskers
        Meronym :  brow
        Meronym :  forehead
        Meronym :  cheek
        Meronym :  chin
        Meronym :  mentum
        Meronym :  eye
        Meronym :  oculus
        Meronym :  optic
        Meronym :  eyebrow
        Meronym :  brow
        Meronym :  supercilium
        Meronym :  facial
        Meronym :  facial_nerve
        Meronym :  nervus_facialis
        Meronym :  seventh_cranial_nerve
        Meronym :  facial_muscle
        Meronym :  facial_vein
        Meronym :  vena_facialis
        Meronym :  feature
        Meronym :  lineament
        Meronym :  jaw
        Meronym :  jowl
        Meronym :  mouth
        Meronym :  nose
        Meronym :  olfactory_organ

    </div>
    </details>

<br/>

7. 전체어 (Holonym)
    <details>
    <summary>예시 보기</summary>
    <div markdown="1">

        Input a synset : finger.n.01

        >>>
        Holonym :  hand
        Holonym :  manus
        Holonym :  mitt
        Holonym :  paw

    </div>
    </details>

<br/>

8. 함의 (Entailment)
    <details>
    <summary>예시 보기</summary>
    <div markdown="1">

        Input a synset : snore.v.01

        >>>
        Entailment :  sleep
        Entailment :  kip
        Entailment :  slumber
        Entailment :  log_Z's
        Entailment :  catch_some_Z's

    </div>
    </details>

<br/>

## 한국어 워드넷
부산대와 카이스트에서는 한국어 워드넷 구축을 위해 연구를 진행하고 있습니다.  
- 부산대의 [KorLex](http://korlex.pusan.ac.kr/)
- 카이스트의 [KWN](http://wordnet.kaist.ac.kr/)