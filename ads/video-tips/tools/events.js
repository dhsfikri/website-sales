const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});const out={};
for(const v of [1,2,3,4,5,6,7]){await p.goto('file://'+path.resolve('ads/video-tips/tips.html')+'?v='+v+'&f=916');
 out[v]=await p.evaluate(()=>{const cfg=V[new URLSearchParams(location.search).get('v')];const ev=[];
  const n=hook.children.length;for(let i=0;i<n;i++)ev.push(['slam',0.2+i*0.2]);
  ev.push(['punch',0.0]);ev.push(['whoosh',2.3]);
  const m=x=>2.6+(x-4.0)/1.6;
  if(cfg.chat)cfg.chat.msgs.forEach(x=>{if(x.typing)ev.push(['typing',m(x.typing[0]),m(x.typing[1])]);ev.push([x.day||x.seen?'tick':'pop',m(x.t)]);});
  if(cfg.nums)cfg.nums.forEach(x=>ev.push(['swoosh',m(x.t)]));
  ev.push(['impact',7.0]);ev.push(['whoosh',9.45]);ev.push(['ding',10.0]);ev.push(['click',10.3]);return ev;});}
console.log(JSON.stringify(out));await b.close();})();
