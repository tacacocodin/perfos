

Clock.bpm=90

               
Root.default = var([0], 8)

Scale.default.set(P[0:24], tuning = P[0:24] )

Scale.default.set("major")

print(Effects)

print(SynthDefs)


#///////////// v1

##TROPICO LLUVIOSO PARTE 1###


#p1 >> loop("14.1-estamosaqui.wav",dur=8,amp=0.051) #4s

p2 >> stretch("ola1", dur = 6, lpf = 1200,amp=0.0,pan=[0.2,-0.2]) #dur 7

p3 >> stretch("pajaro1",P[0:9], dur = 5, pan = [-1,1],formant=1,amp=1.5,lpf=1200).spread()

p4 >> loop("zumbido1",P[0:4],amp=0.5,lpf=[3700,2800,0,100],vib=0, pan = [1,0.5, -0,5, -1]).spread()




Master().room=0.1
Master().mix=0

##TROPICO LLUVIOSO PARTE 2###

Group(p2,p3,p4).stop()

a1 >> stretch("pajaro2",dur= 30,mix=0.4 ,room=0.42,hpf=0,lpf=0,cut=4,amp=1.8).spread()

a3 >> stretch("seagull1", dur=5, amp=1, pan = -1, swell=2)

a6 >> stretch("seagull1", dur=10, amp=[1.29,0.62,0.95], spin=0, pshift=-33,lpf=1000)

a2 >> play("{[vvo] [---] [222]}",chop=3,formant=30,coarse=0,pan=0.41,amp=0.91, bend =-5)

a4 >> play("{[vvo] [---] [222]}",chop=4,formant=30,coarse=0,pan=-0.41,amp=0.91,echo=0.2)

a5 >> stretch("rana1", dur = 9, amp = 0.8, room=0.4,mix=0.75)


a7 >> gong([(0,3,-2),(9,5,-4),(8,3,-6),(7,9,-5)], amp = 2, dur=3/2, sus=2,vib=20,lpf=PRand([1200,100,500,100,10])).every(5, "offadd", 2).every(3, "reverse").every(5, "stutter", 3, dur=3, pan=[-1,1], oct=PRand([6,4,5,3,7])) #amp desde 0.02 max 0.15

a7.solo()

Group(a7,a1,a6).solo()

Master().lpf=0

Master().vib=0

Master().bend=0

##PARTE 3 TROPICO LLUVIOSA###

#pt.1
#(no puedo ver nada despues de mi mano, el bosque no me deja)

Master().amp=0.0

Clock.bpm=100

c1 >> jbass(var([5,3,-1,-4], 3), dur=0.7, amp = 0.4)

f3 >> play("t  t   t", amp=1)

c2 >> play("x x x", amp = 1)

g4 >> play("s", amp = 1.3, dur = [0.5])

f1 >> stretch("pajaro4", dur=12, formant=100, amp=1.2, pan=1)

f2 >> stretch("pajaro5", pan=-1, amp=1.3, dur =9, formant=70)

m1 >> arpy([7,9,13],mix=0.3, amp=1, dur = 0.5, room = 2, vib=2, sus = 1, oct=PRand([6,4,5,3,7]))

t1 >> stretch("ola2", dur = 5, pan = PRand([-1, -0.5, 0,  0.5, 1]), amp = 0.02)

Group(f1,f2,m1).solo()

#pt.2
#(que terrible tempestad me asota en este lodoso y humedo bosque)

#mantener el anterior y juntar con este
r1 >> jbass(var([7,3,8,6], 3), dur=1, amp = 0.4, sus = 1.5)



r3 >> play("  k  ew  [--------]", amp=0.5, dur=0.5,lpf=1200)

r1.solo()

r2 >> play("xxx", amp = 1.4).spread()

r4 >> play(" pero todo pasa",amp=1.2, mix=0.4, room=1).spread()

r5 >> play(" el bosque te dejara tranquilo",amp=1,pshift=-22,room=0.52,mix=0.7)

m1 >> arpy([9,4,19], amp=1.5, dur = 0.5, room = 2, vib=5, sus = 1, oct=PRand([6,4,5,3,7]))

m1.stop()

m1.amp=0.0

#interludio - el bosquecito humedo de un momento a otro se seco y siento la boca seca, sabe a cobre esta colina

m2 >> blip ([[1,3],5,[7,4,3]], dur=0.5 , room=2, amp =1.5, sus=3, lpf= [2500,3000,5000], oct=PRand([2,4,5,3,7]), pan=PRand([0.5,-1,-0.5,1, 0.2, -0.2])).every(3, "offadd", 1).every(1, "stutter", 2, dur=3, pan=[-0.61,0.51], oct=5)

w3 >> stretch("seagull1", dur=7, amp=1.1, bend=[-1,1],pan=PRand([0.5,-1,-0.5,1, 0.2, -0.2]))

m3 >> bug ([3,6,13,6], amp =1, oct=PRand([1,4,5,3,7]),dur=3,sus=1.5,lpf=2000).spread()


Master().lpf=500
Master().room=0.6
Master().mix=1

#pt.3
#(no siento nada, siento todo, adios amigx, fue increible


y1 >> glass([(0,-6,9,2,-4,-2)], amp=1.5).spread()

y2 >> stretch("ola2", dur=16, amp=0, lpf=[1600,1200,100], echo=2, pshift=PRand([0.7,-0.5,-1,1,0.9])).spread()

y3 >> viola([(8,-6,12,7)], sus=1, dur=2, oct=2, amp=1, lpf=600).spread()

y4 >> orient([(8,-6,12,7)], sus=1, dur=9, oct=3, amp=1, lpf=600).spread()

y5 >> space([(8,-6,12,22)], sus=1, dur=3, oct=[3], amp=1, lpf=800).spread()

# transición final

#conecta con seccion anterior

y6 >> ambi([(0,3,5),(1,7),(3,1),([7,5,9,9])], attack=1.5, dur=2, oct=4, amp=2,pan=linvar([0.3,-0.3],32)).spread()

Group(y1,y3,y4,y5).stop()

y7 >> bell ([7,5,8,(5,(9,5,(3,[3,7])))] ,sus=2, dur=4, oct=5, amp=0.4, lpf=1000, reverb=0).every(2, "offadd", 2).every(2, "reverse").every(4, "stutter", 12, dur=3, pan=[-1,1], oct=PRand([6,4,5,3,7]))

y8 >> loop("agua1",P[0:7:1],amp=2,room=0.0,mix=0.5).spread()

y9 >> loop("pajaro4",P[0:7:1],amp=0.5,room=0.9,mix=0.21).spread() #.stop()

Group(y7,y6,y9).solo()

Group(y7,y6,y9).stop()

# trance 1 

l2 >> loop("49.1-maderaGolpe.wav", dur = 2, amp=2, room=0.2,mix=0.3,lpf=2500).stop()

l3 >> loop("46.1-palo.wav",dur=2, amp=2, room=2,mix=0.2,bpf=1000,formant=10).stop()

l4 >> jbass([3,12,17,7,21,-2], amp=linvar([0.05,0.1],32), dur = 6/3,oct=5, room =0.2, mix=0.2).every(9, "offadd", 3).every(3, "stutter", 3, dur=3, pan=[-0.61,0.51], oct=5)


l5 >> marimba([1], amp=0.7, dur=[1/4,3/4], pan=0, hpf=100, room=2, oct=var([3,5],16)).stop()

l6 >> blip ([(2,3,5),(0,3,9),(7,3,9),[9,6,11,0]],amp=0,dur=[0.25],mix=0.7,room=0.8, oct=7,echo=0).stop() #cambio en las terceras notas, dejar en copy y borrar

l7 >> loop("26.1-chorroInfinito.wav",dur=4,formant=2,amp=var([1.4,3.3],[2,5,1]),spin=0).spread().stop() #3

l8 >> play("xx x xx xxx x x", amp = 3).every(2, "offadd", 7).stop()

l9 >> loop("49.1-maderaGolpe.wav", dur = 2, amp=3, room=0.2,mix=0.3,lpf=2500,pshif=11).stop()



#trance 2

Master().lpf=100


k1 >> loop("16.3-aguaChicharras.wav",dur=8, amp=1) #3s

k2 >> loop("16.4-splashRio.wav",dur=8,coarse=2,bpf=5000, amp=0.3)#1s

k3 >> loop("16.5-splash2.wav",dur=8,formant=10,bpf=2000,pan=-1,amp=0.0) #1s

k4 >> loop("16.6-splash3.wav",dur=8,bpf=6000,formant=3,pan=1, amp=0.0) #1s

k5 >> sawbass ([-3, -2, 7, 9, 13], amp=0, dur= 5/3, room=0.2, mix=0.2,sus=2).every(4, "offadd", 17).every(7, "stutter", 6, pan=[-0.61,0.51], oct=6).every(5, "reverse")

k6 >>  bell([(-3,1), (-2,2), (7,3), (9,6), 13], amp=0.05, dur= 5/3,sus=4, room=1, mix=1).every(4, "offadd", PRand([17,19,2,1])).every(2, "stutter", 1, pan=[-0.61,0.51], oct=7).every(3, "reverse")

k7 >> loop("41.2-ave4.wav",dur=16, amp=0.5,pan=-1)

k8 >> loop("36.2-aveSqweeks.wav",dur=16,amp=0.5)

Master().room=0.5

Master().mix=0.6

Master().vib=10
Master().tremolo=1
Master().amp=linvar([0.3,0],32)


print(SynthDefs)

# trance 3


j1 >> loop("27.1-insectoKick.wav",dur=1,amp=0.93) #2
j2 >> loop("28.1-kickLata1.wav",dur=5/2,amp=0.3) #1
j3 >> loop("28.2-kickArrastre.wav",dur=7/3,amp=0.3) #1
j4 >> loop("28.3-kick3Suave.wav",dur=8,amp=0.4) #1
j5 >> loop("28.4-kickDecay.wav",dur=4,amp=0.4) #1
j6 >> loop("28.5-kickMetalico.wav",dur=8,amp=0.4) #1
j7 >> loop("28.6-gong.wav",dur=8,amp=0.4) #2
Group(j1,j2,j3,j4,j5,j6,j7).bpf=3100

Group(j1,j2,j3,j4,j5,j6,j7).formant=0#var([2,4,0,7],PRand([8,48,16]))

Group(j1,j2,j3,j4,j5,j6,j7).vib=12
Group(j1,j2,j3,j4,j5,j6,j7).stutter=0
Group(j1,j2,j3,j4,j5,j6,j7).room=0.4
Group(j1,j2,j3,j4,j5,j6,j7).mix=0.6
Group(j1,j2,j3,j4,j5,j6,j7).pan=PRand([0.1,0.7,-0.6,-0.8])

Group(j1,j2,j3,j4,j5,j6,j7).amp=0

Group(j1,j2,j3,j4,j5,j6,j7).spread()






j8 >> loop("14.2-grabarchicharras.wav",P[1:16],dur=8, amp=var([0.5,2],[32,0]))

Group(j1,j2,j3,j4,j5,j6,j7).stop()

b1 >> loop("38.1-ave1.wav",dur=16, amp = 1, bend = 2, room = 2 , mix = 0.71).every(5, "offadd", PRand([17,19,2,1])).every(7, "stutter", 2, dur=3, pan=[-0.61,0.51], oct=7).every(3, "reverse").spread() #2

b2 >> loop("38.2-ave2.wav",dur=2, amp=2.9, room = 2 , mix = 0.62, pan = -1, glide = 2)

b3 >> loop("41.1-ave3.wav",dur=4, amp = 2.8)

b4 >> loop("41.2-ave4.wav",dur=8, amp=3)

b4.stop()

b5 >> sinepad ([(1,6,8),12,(0,7),10],amp=0.0,dur=10,mix=0.4,room=0.9,oct=4)

b6 >> sinepad ([(1,6,8),12,(0,7),10],amp=0.0,dur=7,mix=0.5,room=0.3,oct=5)

b7 >> sinepad ([(1,6,8),12,(0,7),10],amp=0.0,dur=7,mix=0.3,room=0.5,oct=6)

w1 >> loop("37.1-chicharrasRio.wav",dur=8,amp=15,bpf=0,room=0.1,mix=0.2,pan=[1,-1,0.2]).spread()

w2 >> loop("42.1-chicharrasLejanas.wav",dur=8,amp=15,hpf=0,pan=[-1,1,0.4,-0.2]).spread()

w4 >> marimba((2,0),amp=0.0,dur=1,oct=4,mix=0.4,room=0.2)
