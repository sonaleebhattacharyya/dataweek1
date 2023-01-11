# create_customers =  ####################### TO DO ################################

# FOLLOW PROJECT INSTRUCTIONS TO CREATE TABLE FOR CUSTOMER DATA
create_customers = """ CREATE TABLE customers(
                            id SERIAL PRIMARY KEY, 
                            first_name VARCHAR(50), 
                            last_name VARCHAR(50), 
                            email VARCHAR(50), 
                            gender VARCHAR(10) 
                            );"""
insert_customers = """
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Traver', 'Jakubovitch', 'tjakubovitch0@aol.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Clair', 'Creaney', 'ccreaney1@dion.ne.jp', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Kiele', 'McQuaker', 'kmcquaker2@ca.gov', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Rodge', 'Marchington', 'rmarchington3@thetimes.co.uk', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Kylie', 'Quinane', 'kquinane4@businesswire.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Freda', 'Coppeard', 'fcoppeard5@deviantart.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Prince', 'Jozwiak', 'pjozwiak6@slideshare.net', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Stephine', 'Cogzell', 'scogzell7@dmoz.org', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Kelly', 'Boyington', 'kboyington8@arstechnica.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Karrah', 'Cunah', 'kcunah9@feedburner.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('West', 'Caccavale', 'wcaccavalea@e-recht24.de', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Alvie', 'Hulls', 'ahullsb@studiopress.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Merry', 'Erett', 'merettc@github.io', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Bliss', 'Rouchy', 'brouchyd@instagram.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Almire', 'Guice', 'aguicee@diigo.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Donetta', 'Dantesia', 'ddantesiaf@meetup.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Jerrome', 'Shambrook', 'jshambrookg@ustream.tv', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Fernandina', 'Fleming', 'fflemingh@imgur.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Russell', 'Filoniere', 'rfilonierei@amazon.de', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Wyndham', 'Dillistone', 'wdillistonej@tinypic.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Nicolais', 'Andreone', 'nandreonek@eventbrite.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Leeanne', 'Turbefield', 'lturbefieldl@i2i.jp', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Perice', 'De Ortega', 'pdeortegam@lycos.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Gerard', 'Penhale', 'gpenhalen@wisc.edu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Malena', 'Chapelhow', 'mchapelhowo@google.com.au', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Willamina', 'Calles', 'wcallesp@ted.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Olag', 'Kindread', 'okindreadq@statcounter.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Calvin', 'Andrejs', 'candrejsr@elegantthemes.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Jobey', 'De''Vere - Hunt', 'jdeverehunts@sfgate.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Clevey', 'Tindley', 'ctindleyt@ucsd.edu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Evvie', 'Greedy', 'egreedyu@sun.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Tess', 'Grzegorczyk', 'tgrzegorczykv@nps.gov', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Keenan', 'Scorthorne', 'kscorthornew@multiply.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Aurelea', 'Paterson', 'apatersonx@goo.ne.jp', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Winnie', 'Hannaway', 'whannawayy@microsoft.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Morris', 'Straneo', 'mstraneoz@rambler.ru', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Clayson', 'Manuely', 'cmanuely10@google.pl', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Johny', 'Oldacre', 'joldacre11@hatena.ne.jp', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Morgun', 'Cotesford', 'mcotesford12@yahoo.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Ignacio', 'Putton', 'iputton13@naver.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Jasen', 'Pickett', 'jpickett14@techcrunch.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Karen', 'Jura', 'kjura15@wunderground.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Dynah', 'Petchey', 'dpetchey16@prnewswire.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Maje', 'Hairsnape', 'mhairsnape17@comsenz.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Marice', 'Epps', 'mepps18@netscape.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Devondra', 'Stock', 'dstock19@nationalgeographic.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Helen-elizabeth', 'Pargiter', 'hpargiter1a@imageshack.us', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Ira', 'Scothron', 'iscothron1b@ehow.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Salomone', 'Hitcham', 'shitcham1c@wix.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Sonia', 'Berger', 'sberger1d@arstechnica.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Reade', 'Bouzek', 'rbouzek1e@pbs.org', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Constantin', 'Simmonds', 'csimmonds1f@homestead.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Valentia', 'Brauns', 'vbrauns1g@unc.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Biron', 'Gandar', 'bgandar1h@nationalgeographic.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Gage', 'Melsome', 'gmelsome1i@google.es', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Tristan', 'Messer', 'tmesser1j@infoseek.co.jp', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Tedda', 'Bounde', 'tbounde1k@example.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Tamara', 'Heathwood', 'theathwood1l@bbb.org', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Danita', 'Zelley', 'dzelley1m@techcrunch.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Jody', 'Redmell', 'jredmell1n@360.cn', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Ilyssa', 'Hanlin', 'ihanlin1o@mysql.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Esmeralda', 'Thirwell', 'ethirwell1p@ebay.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Jo', 'Bysshe', 'jbysshe1q@icq.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Rae', 'Hubberstey', 'rhubberstey1r@jalbum.net', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Farrell', 'Telling', 'ftelling1s@eventbrite.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Gib', 'Spearman', 'gspearman1t@hostgator.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Inglebert', 'Marzella', 'imarzella1u@phpbb.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Goober', 'Fishly', 'gfishly1v@who.int', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Ree', 'Semken', 'rsemken1w@t-online.de', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Baily', 'Kwietek', 'bkwietek1x@shutterfly.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Aleksandr', 'Cavalier', 'acavalier1y@amazon.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Shellysheldon', 'Fahrenbacher', 'sfahrenbacher1z@huffingtonpost.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Shawn', 'Kleehuhler', 'skleehuhler20@google.com.br', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Saxe', 'Faltin', 'sfaltin21@nyu.edu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Cassandry', 'Fellnee', 'cfellnee22@mayoclinic.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Bili', 'Franckton', 'bfranckton23@github.io', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Drusy', 'Dalbey', 'ddalbey24@ebay.co.uk', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Moritz', 'Maylott', 'mmaylott25@google.pl', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Justis', 'Girault', 'jgirault26@ning.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Corine', 'Windaybank', 'cwindaybank27@soup.io', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Adolphus', 'Bunford', 'abunford28@stanford.edu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Dexter', 'McMinn', 'dmcminn29@jiathis.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Tynan', 'Averies', 'taveries2a@pen.io', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Whitman', 'Orrill', 'worrill2b@nytimes.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Joana', 'Bercevelo', 'jbercevelo2c@berkeley.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Shanda', 'Brymner', 'sbrymner2d@ebay.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Alexander', 'McNee', 'amcnee2e@webeden.co.uk', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Kyle', 'Sawney', 'ksawney2f@si.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Gus', 'Wilne', 'gwilne2g@arstechnica.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Clareta', 'Wilcocke', 'cwilcocke2h@g.co', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Corina', 'Etoile', 'cetoile2i@google.pl', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Melisa', 'McCardle', 'mmccardle2j@youku.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Jacky', 'Lanceley', 'jlanceley2k@psu.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Jordan', 'Griffiths', 'jgriffiths2l@myspace.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Nehemiah', 'Myott', 'nmyott2m@wikimedia.org', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Bobbie', 'Leet', 'bleet2n@acquirethisname.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Trenton', 'Tarburn', 'ttarburn2o@1und1.de', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Gayla', 'Ashwell', 'gashwell2p@sfgate.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ('Alva', 'Cornbill', 'acornbill2q@sina.com.cn', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Kristen', 'Axtonne', 'kaxtonne2r@engadget.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Zorine', 'Towson', 'ztowson2s@symantec.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Penelopa', 'Barnsdall', 'pbarnsdall2t@msu.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Abey', 'Fortescue', 'afortescue2u@samsung.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Hewet', 'Ruggs', 'hruggs2v@youtu.be', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Elizabet', 'Paskins', 'epaskins2w@techcrunch.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Gabbi', 'Gribben', 'ggribben2x@php.net', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Boigie', 'Resdale', 'bresdale2y@is.gd', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Traver', 'Morris', 'tmorris2z@state.gov', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Terrence', 'Tinmouth', 'ttinmouth30@cdbaby.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Georges', 'Sinfield', 'gsinfield31@about.me', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Mina', 'McLice', 'mmclice32@moonfruit.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Burnaby', 'Trotman', 'btrotman33@loc.gov', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Agustin', 'Guterson', 'aguterson34@princeton.edu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Bard', 'Maciejewski', 'bmaciejewski35@blogs.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Hanan', 'Hamlen', 'hhamlen36@loc.gov', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Vincents', 'Cutill', 'vcutill37@berkeley.edu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Clarisse', 'Parell', 'cparell38@newyorker.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Latisha', 'Jiroutka', 'ljiroutka39@mac.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Glenden', 'Vipan', 'gvipan3a@topsy.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Felix', 'Shailer', 'fshailer3b@squarespace.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Ottilie', 'Maffeo', 'omaffeo3c@un.org', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Rosina', 'Tawton', 'rtawton3d@psu.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Ardra', 'Hawford', 'ahawford3e@wufoo.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Jedidiah', 'Duinkerk', 'jduinkerk3f@bing.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Carree', 'MacAiline', 'cmacailine3g@telegraph.co.uk', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Kenon', 'Altham', 'kaltham3h@fastcompany.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Randie', 'Litzmann', 'rlitzmann3i@usatoday.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Lissie', 'Beranek', 'lberanek3j@shop-pro.jp', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Berenice', 'Trillo', 'btrillo3k@bbc.co.uk', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Honor', 'Sekulla', 'hsekulla3l@vistaprint.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Dwayne', 'Baumber', 'dbaumber3m@scribd.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Tedd', 'Oloshkin', 'toloshkin3n@yellowpages.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Guglielmo', 'Viger', 'gviger3o@moonfruit.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Maryann', 'Mildenhall', 'mmildenhall3p@washington.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Issi', 'Crimmins', 'icrimmins3q@photobucket.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Urban', 'Boorer', 'uboorer3r@infoseek.co.jp', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Hermon', 'Skitral', 'hskitral3s@mail.ru', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Arabelle', 'Yoskowitz', 'ayoskowitz3t@nps.gov', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Guendolen', 'Whether', 'gwhether3u@delicious.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Ameline', 'Gionettitti', 'agionettitti3v@virginia.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Henka', 'Carrivick', 'hcarrivick3w@wordpress.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Tiebout', 'Beine', 'tbeine3x@cbsnews.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Bryana', 'Eburah', 'beburah3y@nasa.gov', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Adria', 'Miners', 'aminers3z@comsenz.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Kristoforo', 'Alti', 'kalti40@biblegateway.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Gard', 'Youens', 'gyouens41@csmonitor.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Charley', 'McCollum', 'cmccollum42@about.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Aubrie', 'Rubinovitch', 'arubinovitch43@utexas.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Falito', 'Volonte', 'fvolonte44@google.co.jp', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Barthel', 'Isaak', 'bisaak45@freewebs.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Monah', 'Quick', 'mquick46@t.co', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Alonzo', 'Stoller', 'astoller47@omniture.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Ferrell', 'Barrowcliff', 'fbarrowcliff48@vimeo.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Jeno', 'Tregent', 'jtregent49@ihg.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Gabe', 'Lissenden', 'glissenden4a@miibeian.gov.cn', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Rosanne', 'Bool', 'rbool4b@umich.edu', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Forrester', 'Bowmer', 'fbowmer4c@uol.com.br', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Tiffanie', 'Karlicek', 'tkarlicek4d@soup.io', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Ben', 'Heinritz', 'bheinritz4e@slate.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Kary', 'Castagno', 'kcastagno4f@networkadvertising.org', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Temple', 'Beaves', 'tbeaves4g@msu.edu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Dante', 'Demaine', 'ddemaine4h@amazon.co.jp', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Dael', 'Chown', 'dchown4i@cisco.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Maddie', 'Shawyers', 'mshawyers4j@examiner.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Erick', 'Peggrem', 'epeggrem4k@dropbox.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Heddi', 'Condliffe', 'hcondliffe4l@house.gov', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Felice', 'Barszczewski', 'fbarszczewski4m@creativecommons.org', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Hort', 'Arnold', 'harnold4n@google.co.uk', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Findley', 'Bolsteridge', 'fbolsteridge4o@posterous.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Gustave', 'Scown', 'gscown4p@dot.gov', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Clare', 'Coggan', 'ccoggan4q@mapy.cz', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Charmian', 'Duding', 'cduding4r@hugedomains.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Sharleen', 'Sambals', 'ssambals4s@t-online.de', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Letty', 'Gridley', 'lgridley4t@bluehost.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Chiquita', 'Lotwich', 'clotwich4u@1und1.de', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Codi', 'MacAlaster', 'cmacalaster4v@creativecommons.org', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Morgen', 'Desporte', 'mdesporte4w@ameblo.jp', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Glad', 'Orford', 'gorford4x@cpanel.net', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Annalee', 'Spriddle', 'aspriddle4y@ox.ac.uk', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Clary', 'Linnett', 'clinnett4z@cpanel.net', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Luke', 'Treby', 'ltreby50@ft.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Ula', 'Goodliff', 'ugoodliff51@barnesandnoble.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Sander', 'Farnfield', 'sfarnfield52@nymag.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Prentice', 'Bossom', 'pbossom53@examiner.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Bianca', 'Topper', 'btopper54@tmall.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Corty', 'Standingford', 'cstandingford55@yellowbook.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Rozelle', 'Huntley', 'rhuntley56@wikimedia.org', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Nadiya', 'Eldredge', 'neldredge57@bloomberg.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Loraine', 'Mityushin', 'lmityushin58@scribd.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Abbe', 'Cordero', 'acordero59@zimbio.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Lizzie', 'Aitchinson', 'laitchinson5a@digg.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Robinia', 'Wagg', 'rwagg5b@angelfire.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Shane', 'Argontt', 'sargontt5c@stumbleupon.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Romy', 'Johnsson', 'rjohnsson5d@guardian.co.uk', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Bathsheba', 'Coppins', 'bcoppins5e@oaic.gov.au', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Alec', 'Hanretty', 'ahanretty5f@webeden.co.uk', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Andie', 'Khoter', 'akhoter5g@rakuten.co.jp', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Kiley', 'Baribal', 'kbaribal5h@webmd.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Roz', 'MacCook', 'rmaccook5i@seesaa.net', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Kayle', 'Iskowicz', 'kiskowicz5j@elegantthemes.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Bord', 'Theobald', 'btheobald5k@sakura.ne.jp', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Salaidh', 'De Ruggero', 'sderuggero5l@howstuffworks.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Leland', 'Flook', 'lflook5m@barnesandnoble.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Yorker', 'Dufaire', 'ydufaire5n@hostgator.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Javier', 'Willmett', 'jwillmett5o@people.com.cn', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Vitoria', 'McRinn', 'vmcrinn5p@canalblog.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Dana', 'Grogan', 'dgrogan5q@google.ru', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Jessy', 'Olijve', 'jolijve5r@microsoft.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Zerk', 'Kaine', 'zkaine5s@elpais.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Budd', 'Seekings', 'bseekings5t@gnu.org', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Blinni', 'Robertson', 'brobertson5u@baidu.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Regina', 'Feathersby', 'rfeathersby5v@is.gd', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Aristotle', 'Moseley', 'amoseley5w@de.vu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Barbey', 'Thorns', 'bthorns5x@amazon.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Jedediah', 'Camelli', 'jcamelli5y@foxnews.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Marthena', 'Tissington', 'mtissington5z@admin.ch', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Alta', 'Bernardin', 'abernardin60@theglobeandmail.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Hewe', 'Thing', 'hthing61@oakley.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Brade', 'Chatburn', 'bchatburn62@domainmarket.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Culley', 'Routley', 'croutley63@phpbb.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Tristan', 'Brammar', 'tbrammar64@xinhuanet.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Kylie', 'Allen', 'kallen65@sourceforge.net', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Peyter', 'Floweth', 'pfloweth66@cdc.gov', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Anatollo', 'Give', 'agive67@ibm.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Diena', 'Patriche', 'dpatriche68@alibaba.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Tremaine', 'Marchello', 'tmarchello69@huffingtonpost.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Bondie', 'Adlem', 'badlem6a@smh.com.au', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Lydia', 'Hollyar', 'lhollyar6b@flavors.me', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Nester', 'Cullimore', 'ncullimore6c@weather.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Lefty', 'Ogus', 'logus6d@ask.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Quentin', 'Foard', 'qfoard6e@imgur.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Sebastian', 'Eggleston', 'seggleston6f@list-manage.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Jesselyn', 'Deeming', 'jdeeming6g@canalblog.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Mariann', 'Oguz', 'moguz6h@naver.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Winna', 'Ashelford', 'washelford6i@comcast.net', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Mala', 'Welbrock', 'mwelbrock6j@accuweather.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Pooh', 'Schwerin', 'pschwerin6k@dmoz.org', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Nil', 'Emanueli', 'nemanueli6l@ibm.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Latashia', 'Pitkins', 'lpitkins6m@vimeo.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Darb', 'Johannesson', 'djohannesson6n@princeton.edu', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Linell', 'Sambath', 'lsambath6o@cdc.gov', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Durante', 'Feacham', 'dfeacham6p@mysql.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Arlen', 'De Cruz', 'adecruz6q@google.cn', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Colby', 'Pinnijar', 'cpinnijar6r@facebook.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Ichabod', 'Cully', 'icully6s@mapquest.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Kaitlynn', 'Leatham', 'kleatham6t@amazon.com', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Cleon', 'Hargrove', 'chargrove6u@stumbleupon.com', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Allan', 'Hedgecock', 'ahedgecock6v@51.la', 'M');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Edie', 'Honeywood', 'ehoneywood6w@hud.gov', 'F');
INSERT INTO customers (first_name, last_name, email, gender) VALUES ( 'Monte', 'Rowlett', 'mrowlett6x@friendfeed.com', 'M'); """