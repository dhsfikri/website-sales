const {chromium}=require('playwright');const path=require('path');const {spawn}=require('child_process');
(async()=>{const [v,f,out]=process.argv.slice(2);const H=f==='45'?1350:1920,FPS=30,D=12;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:H}});
await p.goto('file://'+path.resolve('ads/video-tips/tips.html')+'?v='+v+'&f='+f);await p.evaluate(()=>window.ready);await p.waitForTimeout(400);
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-r',String(FPS),out]);
for(let i=0;i<FPS*D;i++){await p.evaluate(t=>seek(t),i/FPS);const buf=await p.screenshot({type:'jpeg',quality:92});
 if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('ok',out);})();
