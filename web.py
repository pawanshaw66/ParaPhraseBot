

from flask import Flask, render_template, request
from text_paraphasing import summarizer

web = Flask(__name__)
@web.route('/')

def index():
    return render_template('index.html')

@web.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary,original_txt, len_orig_txt, len_summary = summarizer(rawtext)
        return render_template('paraphrase.html',summary=summary, original_txt=original_txt,len_orig_txt=len_orig_txt,len_summary=len_summary)
    

if __name__=='__main__':
    web.run(debug=True)
    
    
 