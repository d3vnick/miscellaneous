// Just replace `div.fallback-text`, too lazy to create a constant

var titles = new Set();
document.querySelectorAll('div.fallback-text').forEach(el => {titles.add(el.textContent + '<br>')}); 
html = "";
titles.forEach(t => html += t)
var win = window.open("", "Titles", "width=500,height=700");
win.document.write(html);
