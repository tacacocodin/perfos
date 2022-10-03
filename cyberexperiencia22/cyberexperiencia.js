//ADVERTENCIA:
//La siguiente presentación puede contener imágenes en movimiento que resulten nocivas para personas con fotosensibilidad. 

//cargar threejs
fetch("https://raw.githubusercontent.com/rexmalebka/hydra-threejs/changes/hack/dist/hydra-three.js").then( x=> x.text() ).then(text=>{
  let script = document.createElement("script")
  script.innerHTML = text
  document.body.appendChild(script)
})

//cargar elementos del dom
t = new three()
//definir env
t.scene
t.camera
t.renderer
t.DracoGLTFLoader // for .glb objects

  //cargar glb monte2
t.DracoGLTFLoader.load( 'https://cdn.glitch.global/a3af49b0-ebd9-441b-9b47-705d75cef416/07_Monte.glb?v=1663045366544', function ( gltf )
{
    monte2 = gltf.scene; 
    monte2.scale.set(15, 15, 15);
    monte2.position.y = 6;
    //t.scene.add(monte);
} );

// rotar objeto
  move_f = setInterval(()=>{
    monte2.rotation.y += 0.005 // rotation del glb
  },50)


/////////////////
//////////////////////////////
  // create three js source on hydra
  s0.initTHREE(t)
///////////////////
/////////////////////


// agregar objeto
 t.scene.add(monte2);

src(s1)
.scale(0.99)
.diff(o0)
.scale(1.21)
.mask(shape(4,[0.3,0.4].smooth(2)))
.diff(o0)
.scale(1.01)
.mult(src(s1))
.colorama([0.001,-0.002].smooth(0))
.saturate(1.71)
.blend(o0,0.6789)
.modulate(o0,0.0014)
.scale(1.01)
  .out(o0)

osc(1,2,20).diff(osc(10,20,10)).out()

//setear position del objeto monte2
monte2.position.x = 0; // lados
monte2.position.y = 0; // altura
monte2.position.z = -10; // profundidad
monte2.scale.set(8,8,8) // tamano


///////////////////////////////////
t.DracoGLTFLoader.load( 'https://cdn.glitch.global/a3af49b0-ebd9-441b-9b47-705d75cef416/chicharraEnPiedra.glb?v=1663129134119', function ( gltf )
{
    chicharra = gltf.scene; 
    chicharra.scale.set(25, 25, 25);
    //t.scene.add(monte);
} );

// rotar objeto
  move_f2 = setInterval(()=>{
    chicharra.rotation.y += 0.005 // rotation del glb
  },50)

// agregar objeto
 t.scene.add(chicharra);


//setear position del objeto chicharras
chicharra.position.y = 3;
chicharra.position.z = 2;
chicharra.scale.set(16,16,16) 



/////////////////////////////////

t.DracoGLTFLoader.load( 'https://cdn.glitch.global/a3af49b0-ebd9-441b-9b47-705d75cef416/17_MonteWrecked.glb?v=1663129725536', function ( gltf )
{
    monte0 = gltf.scene; 
} );
// rotar objeto
  move_f0 = setInterval(()=>{
    monte0.rotation.y += 0.005 // rotation del glb
  },50)

// agregar objeto
 t.scene.add(monte0);


//setear position del objeto chicharras
monte0.position.y = 0;
monte0.position.z = 4.5;
monte0.scale.set(1,1,1) 


////////////////////////////////////////////////frogo


t.DracoGLTFLoader.load( 'https://cdn.glitch.global/a3af49b0-ebd9-441b-9b47-705d75cef416/gremlin_frog.glb?v=1663464570578', function ( gltf )
{
    frogo = gltf.scene; 
} );
// rotar objeto
  move_fr = setInterval(()=>{
    frogo.rotation.y += 0.005 // rotation del glb
  },50)

// agregar objeto
 t.scene.add(frogo);


//setear position del objeto chicharras
frogo.position.y = 0.3;0.frogoposition.z = 3.5e0.sfrogocale.set(1,1,1) 


src(s0).out()


speed=1



hush()

// limpiar el objeto
t.scene.remove(monte2)

t.scene.remove(monte0)

 t.scene.remove(chicharra);

t.scene.remove(frogo);

////////////////////////////////////////////////

 src(o0).out(o0)


src(s0)
.diff(src(s1))
.modulate(s1)
.mask(src(o0).luma(0.7).blend(s1))
.out(o0)

src(s1)
//.scale([0.1,0.7].smooth(1).fast(0.9))
.modulate(o0,0.01)
//.luma(0.1)
.blend(o0,0.1)
.out(o0)


render(o0)


hush()


osc(5).rotate().modulate(noise(3)).out()

speed=0.01

//shape(4,.5).scale(1,innerHeight/innerWidth).out()

//CLIPS LAMARTA

s1.initVideo('https://i.imgur.com/gyOQHlr.mp4') //AWITA

s0.initVideo('https://i.imgur.com/xn3ONBM.mp4') //OLA

s1.initVideo('https://i.imgur.com/pOrh7YX.mp4') //TURBIO

s1.initVideo('https://i.imgur.com/7pQINKp.mp4') //ARBOLZOOM

s1.initVideo('https://i.imgur.com/xYm3AcO.mp4') //PIERNAS

s1.initVideo('https://i.imgur.com/hMxZNSu.mp4') //RANITA

s1.initVideo('https://i.imgur.com/WRLYHX2.mp4') //ESPEJO

s1.initVideo('https://i.imgur.com/Co5Jrxf.mp4') //PIEDRARIO

s1.initVideo('https://i.imgur.com/IkvDGxE.mp4') //ESTRUCTURA

s1.initVideo('https://i.imgur.com/FrFSIuJ.mp4') //MONUMENTO

s1.initVideo('https://i.imgur.com/GeaZ9ye.mp4') //MUROVERDE

s1.initVideo('https://i.imgur.com/xm3UAM6.mp4') //CAMINO

s1.initVideo('https://i.imgur.com/QiIgAA4.mp4') //HOJITAS

s0.initVideo('https://i.imgur.com/UyxGqv2.mp4') //MORPHO

s1.initVideo('https://i.imgur.com/qm8x9YH.mp4') //MORPHOSLOWMO

//CLIPS 3D

s1.initVideo('https://i.imgur.com/AmyAflJ.mp4') //RANCHO

s1.initVideo('https://i.imgur.com/S6k0BiH.mp4') //TIENDA

s1.initVideo('https://i.imgur.com/VrTc7kb.mp4') //CHICHARRA

s1.initVideo('https://i.imgur.com/jMBZG4w.mp4') //STACKPIEDRAS

s1.initVideo('https://i.imgur.com/27VvGO8.mp4') //MONOLITO

s1.initVideo('https://i.imgur.com/J187T2g.mp4') //PIEDRAS

s1.initVideo('https://i.imgur.com/T2f1YBD.mp4') //CHUNCHEMETAL

s1.initVideo('https://i.imgur.com/SJh2v99.mp4') //JOSERIO

s1.initVideo('https://i.imgur.com/AW7S8y0.mp4') //RANDYRIO

s2.initVideo('https://i.imgur.com/m3FvJUk.mp4') //JOHANN

s1.initVideo('https://i.imgur.com/3XljqeO.mp4') //PABLO

s1.initVideo('https://i.imgur.com/k72kfPa.mp4') //JOSE

s1.initVideo('https://i.imgur.com/EBU3AA2.mp4') //RANDY

s1.initVideo('https://i.imgur.com/igNDchL.mp4') //HOJA

s1.initVideo('https://i.imgur.com/qm8x9YH.mp4') //PIEDRAWRECKED


solid().out()

hush()

