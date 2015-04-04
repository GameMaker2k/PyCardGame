#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: cardgame.py - Last Update: 04/04/2015 Ver. 1.0.0 RC 1 - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
import os, sys, platform, re, pygame, random;

pygamename = "Card Game 21";
size = width, height = 640, 480;
screen = pygame.display.set_mode(size);
screen_rect=screen.get_rect();
pygame.display.set_caption(pygamename);
pygame.init();
pygame.display.init();
pygame.mixer.init();
pygame.font.init();
cardbacknum = "1";
cardsetnum = "1";
bkgdsetnum = "1";
filepath = os.path.dirname(os.path.realpath(__file__));
print("Current Path: "+filepath);
pybgimg = pygame.image.load(filepath+"/"+os.path.join("backgrounds", bkgdsetnum+".jpg"));
print("Loading Background Image "+filepath+"/"+os.path.join("backgrounds", bkgdsetnum+".jpg"));
screen.blit(pybgimg,(0, 0));
cardbackleft = pygame.image.load(filepath+"/"+os.path.join("cards"+cardsetnum, "b"+cardbacknum+"pl.png"));
print("Loading Image "+filepath+"/"+os.path.join("cards"+cardsetnum, "b"+cardbacknum+"pl.png"));
screen.blit(cardbackleft,(274, 0));
cardbackright = pygame.image.load(filepath+"/"+os.path.join("cards"+cardsetnum, "b"+cardbacknum+"pr.png"));
print("Loading Image "+filepath+"/"+os.path.join("cards"+cardsetnum, "b"+cardbacknum+"pr.png"));
screen.blit(cardbackright,(357, 0));
cardback = pygame.image.load(filepath+"/"+os.path.join("cards"+cardsetnum, "b"+cardbacknum+"fv.png"));
print("Loading Image "+filepath+"/"+os.path.join("cards"+cardsetnum, "b"+cardbacknum+"fv.png"));
screen.blit(cardback,(286, 0));
pygame.display.flip();
pymusic=pygame.mixer.music.load(filepath+"/"+os.path.join("music", "1.mp3"));
print("Loading Music "+filepath+"/"+os.path.join("music", "1.mp3"));
pygame.mixer.music.play(0);
cardnum = 1;
cardcol = 0;
maxcol = 8;
cardrow = 1;
maxrow = 4;
handtotal = 0;
failedhandtotal = 0;
fullhandtotal = 0;
successhandtotal = 0;
failedtries = 0;
failedlist = [0];
successfulltries = 0;
successlist = [0];
fullcardlist = [0];
cardimg={};
cardnumtype={};
cardvalue={};
cardnametype={};
cardpath={};
playedcards=[0];
numofcardsup=0;
maxnumofcardsup=52;
cardsuittranstable={1: "s", 2: "h", 3: "d", 4: "c"};
cardsuittable={1: "Spades", 2: "Hearts", 3: "Diamonds", 4: "Clubs"};
cardsuittablealt={"s": "Spades", "h": "Hearts", "d": "Diamonds", "c": "Clubs"};
cardtrantable={1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "j", 12: "k", 13: "q"};
cardvaluetable={"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "j": 10, "k": 10, "q": 10};
cardnametrantable={1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "King", 13: "Queen"};
cardnametablealt={"1": "Ace", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "10", "j": "Jack", "k": "King", "q": "Queen"};
cardpickup = pygame.mixer.Sound(filepath+"/"+os.path.join("sound", "click.wav"));
print("Loading Sound "+filepath+"/"+os.path.join("sound", "click.wav")+"\n");
running = True;
while running:
 for event in pygame.event.get():
  if event.type == pygame.MOUSEBUTTONUP:
   pygame.display.set_caption(pygamename+" - Score: "+str(handtotal)+"; Failed Score: "+str(failedhandtotal));
   getmpos = pygame.mouse.get_pos();
   if((getmpos[0]>=274 and getmpos[0]<=369) and (getmpos[1]>=0 and getmpos[1]<=97) and cardrow<=maxrow and numofcardsup<maxnumofcardsup):
    fullcardnum=0;
    trycount=0;
    ftrycount=0;
    strycount=0;
    while fullcardnum in playedcards:
     '''randcardnum = random.randint(1, 54);'''
     randcardnum = random.randint(1, 52);
     if(randcardnum>=1 and randcardnum<=13):
      cardnumtype[cardnum] = 1;
     if(randcardnum>=14 and randcardnum<=26):
      cardnumtype[cardnum] = 2;
     if(randcardnum>=27 and randcardnum<=39):
      cardnumtype[cardnum] = 3;
     if(randcardnum>=40 and randcardnum<=52):
      cardnumtype[cardnum] = 4;
     if(randcardnum>=53 and randcardnum<=54):
      cardnumtype[cardnum] = 5;
     if(cardnumtype[cardnum]<=5):
      cardvalue[cardnum] = randcardnum - ((cardnumtype[cardnum] - 1) * 13);
     fullcardnum=int(str(cardnumtype[cardnum])+str(cardvalue[cardnum]));
     trycount = trycount + 1;
     fullcardlist.append(fullcardnum);
     if(fullcardnum in playedcards):
      failedtries = failedtries + 1;
      ftrycount = ftrycount + 1
      failedlist.append(fullcardnum);
      failedhandtotal = failedhandtotal + cardvaluetable[cardtrantable[cardvalue[cardnum]]];
      fullhandtotal = fullhandtotal + cardvaluetable[cardtrantable[cardvalue[cardnum]]];
      print("PreRandom Number: "+str(randcardnum)+"; Random Number: "+str(fullcardnum)+"; Failed; Failed Tries: "+str(failedtries));
      print("Cannot Pick up "+cardnametrantable[cardvalue[cardnum]]+" of "+cardsuittable[cardnumtype[cardnum]]+"; Was picked up on turn "+str(playedcards.index(fullcardnum))+"; Value: "+str(cardvaluetable[cardtrantable[cardvalue[cardnum]]]));
     if(fullcardnum not in playedcards):
      successfulltries = successfulltries + 1;
      strycount = strycount + 1
      successlist.append(fullcardnum);
      successhandtotal = successhandtotal + cardvaluetable[cardtrantable[cardvalue[cardnum]]];
      fullhandtotal = fullhandtotal + cardvaluetable[cardtrantable[cardvalue[cardnum]]];
      print("PreRandom Number: "+str(randcardnum)+"; Random Number: "+str(fullcardnum)+"; Success; Successfull Tries: "+str(successfulltries));
      print("Number of Tries: "+str(trycount)+"; Failed Tries: "+str(ftrycount)+"; Successfull Tries: "+str(strycount));
      print("Picked up "+cardnametrantable[cardvalue[cardnum]]+" of "+cardsuittable[cardnumtype[cardnum]]+"; Value: "+str(cardvaluetable[cardtrantable[cardvalue[cardnum]]]));
    numofcardsup = numofcardsup + 1;
    playedcards.append(fullcardnum);
    print("Card "+str(numofcardsup)+" out of "+str(maxnumofcardsup));
    print("Column: "+str(cardcol + 1)+" of "+str(maxcol)+"; Row: "+str(cardrow)+" of "+str(maxrow));
    cardnametype[cardnum] = cardsuittranstable[cardnumtype[cardnum]];
    handtotal = handtotal + cardvaluetable[cardtrantable[cardvalue[cardnum]]];
    pygame.display.set_caption(pygamename+" - Score: "+str(handtotal)+"; Failed Score: "+str(failedhandtotal));
    if(cardnumtype[cardnum]<=4):
     cardpath[cardnum] = filepath+"/"+os.path.join("cards"+cardsetnum, cardnametype[cardnum]+cardtrantable[cardvalue[cardnum]]+".png");
    if(cardnumtype[cardnum]==5):
     cardpath[cardnum] = filepath+"/"+os.path.join("cards"+cardsetnum, cardnametype[cardnum]+cardtrantable[cardvalue[cardnum]]+".png");
    print("Loading Image "+cardpath[cardnum]);
    cardimg[cardnum] = pygame.image.load(cardpath[cardnum]);
    print("Playing Sound "+filepath+"/"+os.path.join("sound", "click.wav")+"\n");
    cardpickup.play();
    screen.blit(cardimg[cardnum],(((72 * cardcol) + 33), (97 * cardrow)));
    pygame.display.flip();
    cardnum = cardnum + 1;
    cardcol = cardcol + 1;
    if(cardcol==maxcol):
     cardcol = 0;
     cardrow = cardrow + 1;
    if(cardrow>maxrow):
     cardrow = 1;
  if event.type==pygame.QUIT:
   running = False;
  if event.type==pygame.KEYDOWN:
   if event.key==pygame.K_ESCAPE or event.key==pygame.K_q:
    running = False;
