const { chromium } = require('playwright'); const fs=require('fs');
const S=process.argv[2]; const tpl=fs.readFileSync(S+'/posts/tpl.html','utf8'); const D=JSON.parse(fs.readFileSync(S+'/posts/data.json','utf8'));
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1350}});
fs.mkdirSync(S+'/site/posts',{recursive:true});
for(const d of D){
 const tl=d.title.length>24?'font-size:56px':'';
 const sl={
  1:`<div class="s"><div class="frame"></div><div class="eb">${d.eb||'740 PUBLISHING · JETZT ERHÄLTLICH'}</div><img class="cover" src="cover_${d.k}.png"><div class="t" style="${tl}">${esc(d.title)}</div><div class="a">${esc(d.author)}</div></div>`,
  2:`<div class="s"><div class="frame"></div><div class="eb">WORUM GEHT'S?</div><div class="hook">${esc(d.hook)}</div><div class="rule"></div><div class="txt">${esc(d.text)}</div><div class="dots"><i></i><i class="on"></i><i></i></div></div>`,
  3:`<div class="s"><div class="frame"></div><img class="cv2" src="cover_${d.k}.png"><div class="big">Jetzt erhältlich</div><div class="fm">${d.formats.map(f=>'<span>'+f+'</span>').join('')}</div><div class="link">Link in der Bio</div><div class="sm">${esc(d.line)}</div><img class="logo" src="../site/logo.png"></div>`};
 for(const i of [1,2,3]){ fs.writeFileSync(S+'/posts/_t.html',tpl.replace('__BODY__',sl[i])); await p.goto('file://'+S+'/posts/_t.html'); await p.waitForTimeout(300); await p.screenshot({path:S+'/site/posts/'+d.k+'_'+i+'.jpg',type:'jpeg',quality:90}); }
}
await b.close();})();
