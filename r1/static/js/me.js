const html2pdfBundleMin = require("./html2pdf.bundle.min")

document.getElementById('pdf').addEventListener('click',function(){
    j=document.getElementById('wim')
    html2pdfBundleMin(j)
    console.log('clicked')}
)
