(function(){
  // Comparador
  var cmp=document.getElementById('cmp'),r=document.getElementById('cmpRange');
  if(r)r.addEventListener('input',function(){cmp.style.setProperty('--x',r.value+'%')});
  var pairs=document.querySelectorAll('#pairs button');
  pairs.forEach(function(b){b.addEventListener('click',function(){
    pairs.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    document.getElementById('cmpA').src='/keepr/img/'+b.dataset.a+'.jpg';
    document.getElementById('cmpB').src='/keepr/img/'+b.dataset.b+'.jpg';
    document.getElementById('tagA').textContent=b.dataset.ta;
    document.getElementById('tagB').textContent=b.dataset.tb;
    cmp.style.aspectRatio=b.dataset.r||'1400/933';
    cmp.style.maxWidth=b.dataset.r?'640px':'100%';
  })});

  // Carta de color (medida de la salida de Keepr)
  var IN=["735244","c29682","627a9d","576c43","8580b1","67bdaa","d67e2c","505ba6","c15a63","5e3c6c","9dbc40","e0a32e","383d96","469449","af363c","e7c71f","bb5695","0885a1","f3f3f2","c8c8c8","a0a0a0","7a7a79","555555","343434","141414","282828","3c3c3c","5a5a5a","7a7a7a","a0a0a0","c8c8c8","ebebeb"];
  var OUT={"Portra 400":["7a5437","c79672","5f81a4","57642d","868cb8","51b1a5","df7e00","4e6fb3","cb6a55","644d74","9aa600","e79900","3659a5","328315","ba4c1c","ebb400","c47299","0086a9","f1eee9","c7c4c1","a19f9c","7c7a77","585654","383633","1c1813","2d2a27","403d3b","5d5b59","7c7a78","a19f9c","c7c4c1","e9e6e3"],"Ektar 100":["7e471c","d69869","4f87b5","455e00","8b94ca","00bcb2","ec7800","3e75c8","df5e40","614778","9bac00","ee9c00","2560b8","008700","d03e00","ecb800","d971a5","0091ba","eceae6","cfcdcb","a9a8a6","7c7a77","4d4c4b","262625","070707","1a1a19","2f2e2e","535251","7c7b79","a9a8a6","cfcdcb","e7e5e2"],"Gold 200":["7c4e33","d09976","5f7da2","556e2c","8b82b7","51c5a8","e57b00","4e58af","d44f56","64366c","a1c400","eca600","37389f","2f9c23","c32221","eecb00","cd4a98","008ba6","f3f0e6","cfccc4","a8a59e","7f7c74","57534c","373127","201600","2d2619","3e3930","5c5952","7f7c75","a8a59e","cfccc4","edeae1"],"Pro 400H":["755a4c","c09c87","5c7b9b","53694b","8386ae","53afa8","d68d44","4c64a2","c3736a","604b6e","96af51","dda748","344b94","328852","b35948","e1c245","bd7396","007f9e","e8ebec","c0c4c5","9c9fa0","787b7c","54585a","34393b","121d21","272e31","3c4142","595d5e","787c7d","9c9fa0","c0c4c5","e1e4e5"],"Velvia":["794a1e","cfa475","547db7","48660c","8b88cb","4ec0b8","dd8a00","3b57c8","d2644a","5a3477","a6c100","e0b100","1b36b9","2e9800","c54b00","e2cd00","cd63aa","268abc","e3e3e2","cecece","acacac","7d7d7b","494949","1f1f1f","000000","121212","282828","505050","7d7d7d","acacac","cecece","e0e0e0"],"Tri-X":["575757","aeaeae","777777","5c5c5c","8c8c8c","adadad","a8a8a8","5d5d5d","8e8e8e","444444","b3b3b3","bebebe","3f3f3f","7b7b7b","727272","d0d0d0","8e8e8e","717171","e9e9e9","cecece","a9a9a9","7b7b7b","4c4c4c","252525","060606","191919","2e2e2e","525252","7b7b7b","a9a9a9","cecece","e4e4e4"]};
  function fill(id,arr){var el=document.getElementById(id);if(!el.children.length){arr.forEach(function(){el.appendChild(document.createElement('i'))})}arr.forEach(function(h,i){el.children[i].style.backgroundColor='#'+h})}
  var lp=document.getElementById('lutPick');
  if(lp){fill('pIn',IN.slice(0,18));fill('gIn',IN.slice(18));
  function show(n){fill('pOut',OUT[n].slice(0,18));fill('gOut',OUT[n].slice(18));document.getElementById('chartName').textContent=n;
    lp.querySelectorAll('button').forEach(function(b){b.setAttribute('aria-pressed',b.textContent===n?'true':'false')})}
  Object.keys(OUT).forEach(function(n,i){var b=document.createElement('button');b.type='button';b.id='lut'+i;b.textContent=n;b.addEventListener('click',function(){show(n)});lp.appendChild(b)});
  show('Portra 400');}

  // Muestras de grano (ruido generado con los parámetros de cada tipo)
  var G={tabular:[.85,.85,0,1,.45],cubic:[1,1,.45,1,0],harsh:[1.25,1.2,.65,1.5,0],soft:[1.15,.9,.2,1,.75],fine:[.75,.75,0,1,.25],dye:[1,1,.15,1,0]};
  function rnd(s){return function(){s=(s*16807)%2147483647;return s/2147483647}}
  document.querySelectorAll('#gtypes canvas').forEach(function(c,k){
    var p=G[c.dataset.g],x=c.getContext('2d'),w=c.width,h=c.height,R=rnd(1234+k*99);
    var img=x.createImageData(w,h),d=img.data,cell=Math.max(1,Math.round(p[0]*2)),amt=46*p[1]*p[3];
    var base=new Float32Array(w*h);
    for(var y=0;y<h;y+=cell)for(var xx=0;xx<w;xx+=cell){var v=(R()-.5)*2*amt;if(R()<p[2]*.35)v*=2.2;for(var j=0;j<cell&&y+j<h;j++)for(var i=0;i<cell&&xx+i<w;i++)base[(y+j)*w+xx+i]=v}
    for(var q=0;q<w*h;q++){var v=base[q];if(p[4]>0){var a=base[q-1]||0,b=base[q+1]||0,u=base[q-w]||0,dn=base[q+w]||0;v=v*(1-p[4])+(a+b+u+dn)/4*p[4]}
      var t=128+v,col=c.dataset.g==='dye'||c.dataset.g==='soft'?[t+6,t,t-8]:[t,t,t];d[q*4]=col[0];d[q*4+1]=col[1];d[q*4+2]=col[2];d[q*4+3]=255}
    x.putImageData(img,0,0);
  });

  // Formatos
  var F=[["35mm","f-35mm","24 × 36 mm · 36 cuadros","El de siempre. Ocho perforaciones por cuadro y números con flecha."],
    ["Medio cuadro","f-medio","18 × 24 mm · 72 cuadros","El doble de fotos por rollo, en vertical y en parejas."],
    ["XPan","f-xpan","24 × 65 mm · 21 cuadros","Panorámico sobre 35mm, con la imagen corriendo sobre las perforaciones."],
    ["Sprocket Rocket","f-sprocketrocket","24 × 72 mm","La foto pasa por encima de los sprockets. Las perforaciones se vuelven parte del cuadro."],
    ["110","f-110","13 × 17 mm · cartucho","Pocket Instamatic: cuadros diminutos con una sola perforación."],
    ["645","f-645","6 × 4,5 cm · 15 cuadros","Medio formato en 120, sin perforaciones y con el número en el papel."],
    ["6×6","f-6x6","6 × 6 cm · 12 cuadros","Cuadrado, como una Hasselblad o una Rolleiflex."],
    ["6×7","f-6x7","6 × 7 cm · 10 cuadros","La proporción ideal para imprimir en 8×10."],
    ["6×9","f-6x9","6 × 9 cm · 8 cuadros","Igual que 35mm, pero cuatro veces más negativo."],
    ["6×12","f-6x12","6 × 12 cm · 6 cuadros","Panorámico en 120, el de los paisajes largos."],
    ["4×5","f-4x5","4 × 5 in · hoja suelta","Placa con muescas en la esquina para saber de qué película es."],
    ["8×10","f-8x10","8 × 10 in · hoja suelta","El contacto mide lo mismo que el negativo."],
    ["Polaroid","f-polaroid","79 × 79 mm · marco 600","Con su marco ancho abajo y la química en el borde."],
    ["Instax","f-instax","46 × 62 mm · Mini","Pequeña, brillante, con esquinas redondas."]];
  var fp=document.getElementById('fmtPick');
  if(fp)F.forEach(function(f,i){var b=document.createElement('button');b.type='button';b.id='fmt'+i;b.textContent=f[0];b.setAttribute('aria-pressed',i?'false':'true');
    b.addEventListener('click',function(){var im=document.getElementById('fmtImg');im.src='/keepr/img/'+f[1]+'.jpg';im.alt='Hoja de contactos en '+f[0];
      document.getElementById('fmtName').textContent=f[0];document.getElementById('fmtDims').textContent=f[2];document.getElementById('fmtNote').textContent=f[3];
      fp.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')})});fp.appendChild(b)});

  // Revelado: cada bloque aparece y sus fotos se revelan como en la charola
  if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
    var els=document.querySelectorAll('.hero .wrap>div,.hero figure,.counts>div,.head,.tcard,section figure,.compare,.why,.facts>div,.stock,.gtype,.ink,.local h2,.local .grid>div,.plist li,.pager a,.end h2');
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(el){
      var sib=el.parentElement?Array.prototype.indexOf.call(el.parentElement.children,el):0;
      el.classList.add('rv');el.style.transitionDelay=Math.min(sib,5)*90+'ms';io.observe(el)});
  }
})();
